
ADDRESSES = {
    'vpc_tunnel_proxy': '127.0.0.1:8889',
    'sauceUrl': 'http://ondemand.saucelabs.com/wd/hub',
    'appiumUrl': 'http://localhost:4723/wd/hub'
}

MACBOOK = {
    'default': {
        'acceptInsecureCerts': True,
        'acceptSslCerts': True,
        'platform': 'macOS 10.14'
    }
}

ANDROID = {
    'default': {
        'deviceName': 'Samsung Galaxy S9 Plus WQHD GoogleAPI Emulator',
        'udid': 'emulator-5554',
        'deviceOrientation': 'portrait',
        'platformName': 'Android',
        'platformVersion': '8.0',
        'browserName': ''
    }
}

IOS = {
    'default': {
        'deviceName': 'iPhone X Simulator',
        'deviceOrientation': 'portrait',
        'platformName': 'iOS',
        'platformVersion': '12.0',
        'browserName': ''
    }
}
