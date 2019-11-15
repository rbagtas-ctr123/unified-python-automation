"""Helper functions to identify and generate UI drivers"""

import os
from selenium import webdriver as selenium_driver
from appium import webdriver as appium_driver
from configuration.device_config import ADDRESSES, ANDROID, IOS, MACBOOK
from utilities.helpers.config_helpers import define_arguments

SUPPORTED_PLATFORMS = {'chrome', 'firefox', 'android', 'ios'}
DEFAULT_PLATFORM = 'chrome'
SUPPORTED_HOSTS = {'local', 'saucelabs'}
DEFAULT_HOST = 'local'
SAUCE_APPIUM_VERSION = '1.9.1'


def requested_platforms():
    """Returns a list of platforms derived from the --platform flag set by command line
    Verifies that each requested browser is supported"""
                                        
    args = define_arguments()
    if args.platform:
        platforms_requested = args.platform.split(':')
    else:
        platforms_requested = [DEFAULT_PLATFORM]
    for platform in platforms_requested:
        if platform not in SUPPORTED_PLATFORMS:
            raise ValueError(f"--platform argument '{platform}' not within supported: '{SUPPORTED_PLATFORMS}'")
    return platforms_requested


def requested_host():
    """Returns a test host derived from the --host flag set by command line
    Verifies that the requested host is supported"""
    
    args = define_arguments()
    if args.host:
        host = args.host
        if host not in SUPPORTED_HOSTS:
            raise ValueError(f"--host argument '{host}' not within supported: '{SUPPORTED_HOSTS}'")
    else:
        host = DEFAULT_HOST
    return host


def get_saucelab_test_metadata(request):
    """ Gather test metadata from the pytest item.nodes to populate Saucelabs test results """
    test_info = dict()
    # Gets the test name which is the function name
    test_info['test_name'] = request.node.name
    marks = []
    # Collects all the marks from the test which are used as tags to categorize the tests in Saucelabs
    for mark in request.node.own_markers:
        marks.append(mark.name)
    test_info['marks'] = marks
    return test_info


def generate_driver(request, env_config):
    """ Generate a webdriver object connected to the requested platform & host """
    platform = request.param
    host = requested_host()
    if host == 'saucelabs':
        test_metadata = get_saucelab_test_metadata(request)
        driver = generate_driver_saucelabs(platform, env_config, test_metadata)
    # If host is not a remote host we default to creating the driver locally
    else:
        driver = generate_driver_local(platform, env_config)
    return driver


def generate_driver_local(platform, env_config):
    """ Generate a webdriver on a local host """
    driver = None
    if platform == 'chrome':
        chrome_options = selenium_driver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--proxy-server=socks5://' + ADDRESSES['vpc_tunnel_proxy'])
        driver = selenium_driver.Chrome(options=chrome_options)
    elif platform == 'firefox':
        proxy_pieces = ADDRESSES['vpc_tunnel_proxy'].split(':')
        profile = selenium_driver.FirefoxProfile()
        profile.set_preference('network.proxy.type', 1)
        profile.set_preference('network.proxy.socks', proxy_pieces[0])
        profile.set_preference('network.proxy.socks_port', int(proxy_pieces[1]))
        profile.update_preferences()
        driver = selenium_driver.Firefox(firefox_profile=profile)
    elif platform == 'safari':
        driver = selenium_driver.Safari()
        driver.maximize_window()
    elif platform == 'android':
        desired_capabilities = ANDROID['default']
        desired_capabilities['automationName'] = 'UiAutomator2'
        desired_capabilities['app'] = env_config['sauce_android_apk']
        driver = appium_driver.Remote(ADDRESSES['appiumUrl'], desired_capabilities)
    elif platform == 'ios':
        desired_capabilities = IOS['default']
        desired_capabilities['automationName'] = 'XCUITest'
        desired_capabilities['app'] = env_config['sauce_ios_ipa']
        driver = appium_driver.Remote(ADDRESSES['appiumUrl'], desired_capabilities)
    return driver


def generate_driver_saucelabs(platform, env_config, test_metadata):
    """ Generate a webdriver on a saucelabs device farm """
    caps = dict()
    caps['username'] = os.environ['SAUCE_USERNAME']
    caps['accesskey'] = os.environ['SAUCE_API_KEY']
    # Test metadata for cataloging tests in Saucelabs
    caps['name'] = test_metadata['test_name']
    caps['tags'] = test_metadata['marks']
    # Passes the Circle CI build number if present else must be an ad hoc test ran in Saucelabs
    caps['build'] = os.getenv('CIRCLE_BUILD_NUM', 'ad-hoc-test')
    # Automatically will target shared Sauce Connect Tunnel if SAUCE_TUNNEL_IDENTIFIER is present.
    if os.environ.get('SAUCE_TUNNEL_IDENTIFIER'):
        caps['tunnelIdentifier'] = os.environ.get('SAUCE_TUNNEL_IDENTIFIER')
    elif os.environ.get('SAUCE_USERNAME'):
        caps['tunnelIdentifier'] = (os.environ['SAUCE_USERNAME']+'_tunnel')
    else:
        ValueError('No Sauce Tunnel Identifier was provided!')
    driver = None
    if platform == 'chrome':
        caps.update(MACBOOK['default'])
        caps['browserName'] = 'chrome'
        caps['version'] = '75.0'
        driver = selenium_driver.Remote(command_executor=ADDRESSES['sauceUrl'],
                                        desired_capabilities=caps)
    elif platform == 'firefox':
        caps.update(MACBOOK['default'])
        caps['browserName'] = 'firefox'
        caps['version'] = '67.0'
        driver = selenium_driver.Remote(command_executor=ADDRESSES['sauceUrl'],
                                        desired_capabilities=caps)
    elif platform == 'safari':
        caps.update(MACBOOK['default'])
        caps['browserName'] = 'safari'
        caps['version'] = '12.0'
        driver = selenium_driver.Remote(command_executor=ADDRESSES['sauceUrl'],
                                        desired_capabilities=caps)
    elif platform == 'android':
        caps.update(ANDROID['default'])
        caps['appiumVersion'] = SAUCE_APPIUM_VERSION
        caps['app'] = env_config['sauce_android_apk']
        driver = appium_driver.Remote(command_executor=ADDRESSES['sauceUrl'],
                                      desired_capabilities=caps)
    elif platform == 'ios':
        caps.update(IOS['default'])
        caps['appiumVersion'] = SAUCE_APPIUM_VERSION
        caps['app'] = env_config['sauce_ios_ipa']
        driver = appium_driver.Remote(command_executor=ADDRESSES['sauceUrl'],
                                      desired_capabilities=caps)
    return driver


def close_current_browser_tab(driver):
    """ Close current browser tab """
    driver.close()


def switch_browser_tab(driver, window_index):
    """ Switch browser tab """
    driver.switch_to.window(driver.window_handles[window_index])
