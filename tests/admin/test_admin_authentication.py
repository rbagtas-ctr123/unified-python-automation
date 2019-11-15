"""A collection of tests covering the login functionality of the Admin20 app."""

import pytest
from pages.admin import AdminLoginPage, AdminDashboardPage

@pytest.mark.admin
class TestAdminAuthentication:
    """A collection of tests for the authentication process of the Admin20 application"""
    def test_admin_login(self, env_config, driver):
        """This tests a user entering correct credentials
        and successfully logging in"""
        login = AdminLoginPage(driver)
        login.enter_page(env_config['addresses']['admin_20'])
        login.get_to_google_login()
        login.complete_google_authorization(env_config['customer_info_admin']['email'],
                                            env_config['customer_info_admin']['okta_username'],
                                            env_config['customer_info_admin']['okta_password'])

        dashboard = AdminDashboardPage(driver)
        dashboard.wait_until_dashboard_displayed()
