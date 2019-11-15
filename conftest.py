"""PyTest fixtures for resource management"""

import pytest
import utilities.helpers.config_helpers as config_helpers
import utilities.helpers.driver_helpers as driver_helpers
from utilities.db_helpers.db_context_managers import WebDatabase, AccountOpeningGalileo, AccountManagement, \
    AccountOpeningAlloy, BankingDatabase


def pytest_addoption(parser):
    """Allow helpers access to the --env + --platform command line options"""
    supported_envs = ":".join(config_helpers.SUPPORTED_ENVIRONMENTS)
    supported_platforms = ":".join(driver_helpers.SUPPORTED_PLATFORMS)
    supported_layers = ":".join(config_helpers.SUPPORTED_LAYERS)
    supported_hosts = ":".join(driver_helpers.SUPPORTED_HOSTS)
    parser.addoption("--env", action="store", default=config_helpers.DEFAULT_ENVIRONMENT,
                     help=f'supported: {supported_envs}')
    parser.addoption('--platform', action='store', default=driver_helpers.DEFAULT_PLATFORM,
                     help=f'supported: {supported_platforms}')
    parser.addoption('--host', action='store', default=driver_helpers.DEFAULT_HOST,
                     help=f'supported: {supported_hosts}')
    parser.addoption('--layer', action='store', default=config_helpers.DEFAULT_LAYER,
                     help=f'supported: {supported_layers}')


@pytest.fixture(scope='session', params=config_helpers.requested_environments())
def env_config(request):
    """Returns a environment dictionary for the current environment"""
    return config_helpers.get_environment_config(request.param)


@pytest.fixture(scope='session')
def web_db_connection(env_config):
    """Manages a cursor to the web_db"""
    db_connection = WebDatabase(env_config)
    return db_connection


@pytest.fixture(scope='session')
def account_opening_alloy_db_connection(env_config):
    """Manages a cursor to the web_db"""
    db_connection = AccountOpeningAlloy(env_config)
    return db_connection


@pytest.fixture(scope='session')
def account_opening_galileo_db_connection(env_config):
    """Manages a cursor to the web_db"""
    db_connection = AccountOpeningGalileo(env_config)
    return db_connection


@pytest.fixture(scope='session')
def account_mgmt_db_connection(env_config):
    """Manages a cursor to the web_db"""
    db_connection = AccountManagement(env_config)
    return db_connection


@pytest.fixture(scope='session')
def banking_db_connection(env_config):
    """Manages a cursor to the web_db"""
    db_connection = BankingDatabase(env_config)
    return db_connection


@pytest.fixture(params=driver_helpers.requested_platforms())
def driver(request, env_config):
    """Manages drivers to fulfill what the --platform flag requests"""
    driver_instance = driver_helpers.generate_driver(request, env_config)

    yield driver_instance
    host = driver_helpers.requested_host()
    # Perform post-test logging while we still have the driver object available, if the test was executed
    if request.node.report_call:
        # Take a screenshot if the test failed
        if request.node.report_call.failed:
            driver_instance.get_screenshot_as_file("failure_" + request.node.name + ".png")
        # Send test results to SauceLabs if they were the test host
        if host == 'saucelabs':
            test_results = request.node.report_call
            driver_instance.execute_script("sauce:job-result={result}".format(result=test_results.outcome))
    driver_instance.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """ Attach the testreport for each test run to that run's request.node
        Each report is one of the 3 phases: 'setup', 'call', 'teardown' """
    report = (yield).get_result()
    setattr(item, "report_" + report.when, report)


def pytest_collection_modifyitems(items, config):
    """ deselect test items which do not match the requested environments & platforms
        if no environment or platform is marked for a test, the test will be considered valid for all options """

    deselection_items = []

    # deselect test items without a platform tag that matches any of the requested platforms
    for item in items:
        if item not in deselection_items:
            mark = item.get_closest_marker(name='platform')
            # Only restrict tests when a platform has been marked for the test
            if mark:
                marked_platforms = set(mark.args)
                # Deselect tests where a driver was requested for a non-supported platform
                if item.callspec.params['driver'] not in marked_platforms:
                    deselection_items.append(item)

    # deselect test items without an environment tag that matches the requested environment
    for item in items:
        if item not in deselection_items:
            mark = item.get_closest_marker(name='environment')
            # Only restrict tests when an environment has been marked for the test
            if mark:
                marked_environments = set(mark.args)
                # Deselect tests where a config was requested for a non-supported environment
                if item.callspec.params['env_config'] not in marked_environments:
                    deselection_items.append(item)

    # deselect test items with a layer tag which doesn't match any requested layer
    for item in items:
        if item not in deselection_items:
            mark = item.get_closest_marker(name='layer')
            if mark:
                marked_layers = set(mark.args)
                requested_layers = set(item.config.getoption('--layer').split(':'))
                # Deselect tests where a they are marked for a not-requested layer
                if not len(requested_layers.intersection(marked_layers)):
                    deselection_items.append(item)

    # remove all tests collected for deselection
    items[:] = [item for item in items if item not in deselection_items]
    config.hook.pytest_deselected(items=deselection_items)
