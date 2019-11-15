""" A collection of tests of the Dashboard functionality of the Aspiration platform """

import pytest
from utilities.helpers.api_helpers import get_galileo_balance
from pages.platform import LoginPage
from pages.platform.dashboard_page import DashboardPage, Products
from pages.platform.navigation_page import NavigationPage
from pages.platform.insurance_page import InsurancePage
from utilities.helpers.driver_helpers import close_current_browser_tab, switch_browser_tab


@pytest.mark.dashboard
@pytest.mark.regression
@pytest.mark.platform("chrome", "firefox", "android")
class TestDashboard:

    @pytest.mark.critical
    def test_sns_balances_display(self, env_config, driver):
        """ Confirm that a positive spend balance is displayed """
        user_config = env_config['customer_info_spend_save']
        login_page = LoginPage(driver)
        login_page.enter(env_config['addresses']['login'])
        login_page.submit_login(user_config['email'], user_config['password'])
        dashboard = DashboardPage(driver)
        dashboard.wait_until_dashboard_displayed()
        assert dashboard.get_product_balance(Products.SPEND) > 0
        assert dashboard.get_product_balance(Products.SAVE) > 0

    def test_save_balance_displays(self, env_config, driver):
        """ Confirm that a positive save balance is displayed """
        login_page = LoginPage(driver)
        login_page.enter(env_config['addresses']['login'])
        login_page.submit_login(env_config['customer_info_save']['email'],
                                env_config['customer_info_save']['password'])
        dashboard = DashboardPage(driver)
        dashboard.wait_until_dashboard_displayed()
        assert dashboard.get_product_balance(Products.SAVE) > 0

    @pytest.mark.environment("alpha")
    def test_spend_balance_accurate(self, env_config, driver):
        """ Confirm that the displayed spend balance matches what's in Galileo's records """
        login_page = LoginPage(driver)
        login_page.enter(env_config['addresses']['login'])
        login_page.submit_login(env_config['customer_info_spend_save']['email'],
                                env_config['customer_info_spend_save']['password'])

        dashboard = DashboardPage(driver)
        dashboard.wait_until_dashboard_displayed()
        assert dashboard.get_product_balance(Products.SPEND) == get_galileo_balance(
                                env_config['customer_info_spend_save']['spend_prn'])

    @pytest.mark.environment("alpha")
    def test_save_balance_accurate(self, env_config, driver):
        """ Confirm that the displayed save balance matches what's in Galileo's records """
        login_page = LoginPage(driver)
        login_page.enter(env_config['addresses']['login'])
        login_page.submit_login(env_config['customer_info_save']['email'],
                                env_config['customer_info_save']['password'])

        dashboard = DashboardPage(driver)
        dashboard.wait_until_dashboard_displayed()
        assert dashboard.get_product_balance(Products.SAVE) == get_galileo_balance(
                                env_config['customer_info_save']['prn'])
    
    @pytest.mark.critical
    def test_investment_balance_displays(self, env_config, driver):
        """ Confirm that a valid Investment Product balance is displayed """
        login_page = LoginPage(driver)
        login_page.enter(env_config['addresses']['login'])
        login_page.submit_login(env_config['customer_info_investment']['email'],
                                env_config['customer_info_investment']['password'])
        dashboard = DashboardPage(driver)
        dashboard.wait_until_dashboard_displayed()
        assert dashboard.get_product_balance(Products.REDWOOD) >= 0

    @pytest.mark.insurance
    def test_insurance_button_navigates_to_lemonade_website(self, env_config, driver):
        """ Confirm Lemonade Insurance page button navigates to Lemonade Website """
        login_page = LoginPage(driver)
        login_page.enter(env_config['addresses']['login'])
        login_page.submit_login(env_config['customer_info_spend_save']['email'],
                                env_config['customer_info_spend_save']['password'])
        dashboard_page = DashboardPage(driver)
        dashboard_page.wait_until_dashboard_displayed()
        navigation_page = NavigationPage(driver)
        navigation_page.navigate_to_insurance_page()
        insurance_page = InsurancePage(driver)

        lemonade_renters_url = "https://www.lemonade.com/l/aspiration?utm_source=aspiration&utm_campaign=app_cta" \
                               "&utm_content=renters&utm_term="

        lemonade_home_owners_url = "https://www.lemonade.com/l/aspiration?utm_source=aspiration&utm_campaign=app_cta" \
                                   "&utm_content=homeowners&utm_term="

        insurance_page.wait_until_insurance_displayed()
        insurance_page.navigate_to_lemonade_renters_page()
        insurance_page.wait_until_lemonade_insurance_page_displayed()
        current_url = driver.current_url
        assert lemonade_renters_url in current_url
        original_browser_tab_index = 0
        close_current_browser_tab(driver)
        switch_browser_tab(driver, original_browser_tab_index)
        insurance_page.navigate_to_lemonade_homeowners_page()
        insurance_page.wait_until_lemonade_insurance_page_displayed()
        current_url = driver.current_url
        assert lemonade_home_owners_url in current_url
