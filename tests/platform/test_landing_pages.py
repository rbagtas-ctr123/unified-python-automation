import pytest
from pages.platform import CustomerInfoPage
from pages.platform.prospect_landing_page import ProspectLandingPage
from utilities.helpers.data_generator_helper import generate_timestamped_email


@pytest.mark.landers
@pytest.mark.regression
@pytest.mark.environment("alpha")
@pytest.mark.platform("chrome", "firefox")
class TestLandingPages:

    def test_get_account_page(self, env_config, driver, web_db_connection):
        """ Create a new customer account, via ~/get-account """
        # # Contact/PII info for customer account
        email = generate_timestamped_email(env_config['customer_info_new_customer_app']['email_domain'])
        password = env_config['customer_info_new_customer_app']['password']

        # Navigate to /get-account Landing page
        prospect_landing = ProspectLandingPage(driver)
        prospect_landing.enter(env_config['addresses']['prospect_lander_get_account'])
        assert driver.current_url == env_config['addresses']['prospect_lander_get_account']
        prospect_landing.check_cta_buttons_via_get_account()
        prospect_landing.submit_get_account_email(email)

        # Sign up Page
        customer_info_page = CustomerInfoPage(driver)
        customer_info_page.submit_new_account_credentials(email, password)
        customer_info_page.wait_until_personal_info_displayed()

    def test_get_account_100_page(self, env_config, driver, web_db_connection):
        """ Create a new customer account, via ~/get-account-100 """
        #
        # # Contact/PII info for customer account
        email = generate_timestamped_email(env_config['customer_info_new_customer_app']['email_domain'])
        password = env_config['customer_info_new_customer_app']['password']

        # Navigate to /get-account Landing page
        prospect_landing = ProspectLandingPage(driver)
        prospect_landing.enter(env_config['addresses']['prospect_lander_get_account_100'])
        assert driver.current_url == env_config['addresses']['prospect_lander_get_account_100']
        prospect_landing.check_cta_buttons_via_get_account()
        prospect_landing.submit_get_account_email(email)

        # Sign up Page
        customer_info_page = CustomerInfoPage(driver)
        customer_info_page.submit_new_account_credentials(email, password)
        customer_info_page.wait_until_personal_info_displayed()

    def test_pride_page(self, env_config, driver, web_db_connection):
        """ Create a new customer account, via ~/get-account-pride """
        #
        # # Contact/PII info for customer account
        email = generate_timestamped_email(env_config['customer_info_new_customer_app']['email_domain'])
        password = env_config['customer_info_new_customer_app']['password']

        # Navigate to /get-account Landing page
        prospect_landing = ProspectLandingPage(driver)
        prospect_landing.enter(env_config['addresses']['prospect_lander_get_account_pride'])
        assert driver.current_url == env_config['addresses']['prospect_lander_get_account_pride']
        prospect_landing.check_cta_buttons_via_get_account()
        prospect_landing.submit_get_account_email(email)

        # Sign up Page
        customer_info_page = CustomerInfoPage(driver)
        customer_info_page.submit_new_account_credentials(email, password)
        customer_info_page.wait_until_personal_info_displayed()

    def test_tesla_page(self, env_config, driver, web_db_connection):
        """ Create a new customer account, via ~/get-account-teslap2019 """
        #
        # # Contact/PII info for customer account
        email = generate_timestamped_email(env_config['customer_info_new_customer_app']['email_domain'])
        password = env_config['customer_info_new_customer_app']['password']

        # Navigate to /get-account Landing page
        prospect_landing = ProspectLandingPage(driver)
        prospect_landing.enter(env_config['addresses']['prospect_lander_tesla_page'])
        assert driver.current_url == env_config['addresses']['prospect_lander_tesla_page']
        prospect_landing.check_cta_buttons_via_get_account()
        prospect_landing.submit_get_account_tesla_email(email)

        # Sign up Page
        customer_info_page = CustomerInfoPage(driver)
        customer_info_page.submit_new_account_credentials(email, password)
        customer_info_page.wait_until_personal_info_displayed()
