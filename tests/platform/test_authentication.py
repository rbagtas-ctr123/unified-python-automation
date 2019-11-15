""" A collection of tests covering the login functionality of the Aspiration platform """

import pytest
from pages.platform import LoginPage, NavigationPage, DashboardPage
from pages.platform.login_page import LoginStatus

WRONG_PASSWORD = 'BAD_PASSWORD'


@pytest.mark.authentication
@pytest.mark.regression
class TestAuthentication:

    @pytest.mark.critical
    def test_login_logout(self, env_config, driver):
        """ Confirm a user can successfully log in and log out """
        login = LoginPage(driver)
        login.enter(env_config['addresses']['login'])
        login.submit_login(env_config['customer_info_spend_save']['email'],
                           env_config['customer_info_spend_save']['password'])
        dashboard = DashboardPage(driver)
        dashboard.wait_until_dashboard_displayed()
        navigation = NavigationPage(driver)
        navigation.logout()
        login.wait_until_login_ready()

    @pytest.mark.smoke
    def test_failed_login(self, env_config, driver):
        """ Confirm the error message appears when attempting to log in with the wrong password """
        login = LoginPage(driver)
        login.enter(env_config['addresses']['login'])
        login.submit_login(env_config['customer_info_spend_save']['email'], WRONG_PASSWORD)
        assert login.get_login_status() == LoginStatus.INVALID_CREDENTIALS
