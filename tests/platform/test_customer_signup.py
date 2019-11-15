""" A collection of customer sign up tests for the Aspiration Platform """

import pytest

from pages.platform import ProspectLandingPage
from pages.platform import CustomerInfoPage
from pages.platform import CMAProductApplicationPage
from pages.platform import PWIFPage, PWIFAmount
from pages.platform import LinkBankAccountPage, PlaidBank
from pages.platform import DashboardPage, Products, ProductApplicationStatus, NavigationPage, TransfersPage, \
    SettingsPage

from utilities.helpers.data_generator_helper import generate_random_phone_number, generate_timestamped_email, \
    generate_random_string

from utilities.db_helpers.web_db_helpers import generate_unique_ssn


@pytest.mark.smoke
@pytest.mark.platform("chrome", "firefox")
@pytest.mark.environment("alpha")
class TestCustomerSignup:

    def test_new_sns_customer_creation(self, env_config, driver, web_db_connection):
        """ Create a new customer account, completes a Spend & Save Product Application, then validates Opening Deposit
         """
        customer_info = env_config['customer_info_new_customer_app']
        customer_info['email'] = generate_timestamped_email(
            env_config['customer_info_new_customer_app']['email_domain']
        )
        customer_info['phone_number'] = generate_random_phone_number()
        customer_info['first_name'] = generate_random_string(5, 10)
        customer_info['last_name'] = generate_random_string(5, 10)
        customer_info['date_of_birth'] = '06/01/1980'
        customer_info['ssn'] = generate_unique_ssn(web_db_connection, True)

        prospect_landing = ProspectLandingPage(driver)
        prospect_landing.enter(env_config['addresses']['prospect_lander'])
        prospect_landing.submit_get_started_email(customer_info['email'])
        opening_deposit = 50
        customer_info_page = CustomerInfoPage(driver)
        customer_info_page.submit_new_account_credentials(customer_info['email'], customer_info['password'])

        customer_info_page.submit_personal_info(customer_info)

        customer_info_page.submit_contact_details(customer_info)

        customer_info_page.review_your_info()

        cma_product_application_page = CMAProductApplicationPage(driver)
        cma_product_application_page.navigate_into_link_bank_account()

        link_bank_account_page = LinkBankAccountPage(driver)
        link_bank_account_page.link_account_via_plaid(
            env_config['customer_info_new_customer_app']['plaid_username'],
            env_config['customer_info_new_customer_app']['plaid_password'],
            PlaidBank.CHASE,
            'savings'
        )

        cma_product_application_page = CMAProductApplicationPage(driver)
        cma_product_application_page.submit_opening_deposit_amount(opening_deposit)

        cma_product_application_page.choose_recurring_deposit_options(False)

        pwif_page = PWIFPage(driver)
        pwif_page.choose_pwif_amount(PWIFAmount.MID_AMOUNT)

        cma_product_application_page.review_and_confirm_deposit_details()

        cma_product_application_page.confirm_and_submit_product_application(True)

        # Dashboard and validation
        dashboard_page = DashboardPage(driver)
        dashboard_page.wait_until_dashboard_displayed()
        assert dashboard_page.get_product_status(Products.SPEND) == ProductApplicationStatus.COMPLETED
        assert dashboard_page.get_product_status(Products.SAVE) == ProductApplicationStatus.COMPLETED
        dashboard_page.wait_until_debit_card_tracker_displayed()

        # Transfer Page and validation
        navigation_page = NavigationPage(driver)
        navigation_page.show_transfers()
        transfers_page = TransfersPage(driver)
        transfers_page.wait_until_transfers_displayed()
        opening_transfer = transfers_page.get_opening_deposit_amount()
        assert opening_transfer == opening_deposit
        navigation_page.navigate_to_settings_page()

        # Settings Page and validation
        settings_page = SettingsPage(driver)
        settings_page.wait_until_settings_displayed()
        pwif_setting = settings_page.get_pwif_amount()
        assert str(pwif_setting) == str(PWIFAmount.MID_AMOUNT.value)

    @pytest.mark.xfail  # GROW-1202
    def test_new_save_signup(self, env_config, driver, web_db_cursor):
        """ Create a new customer account, then completes a Save Product Application """
        #
        # # Contact/PII info for customer account
        customer_info = env_config['customer_info_new_customer_app']
        customer_info['email'] = generate_timestamped_email(
            env_config['customer_info_new_customer_app']['email_domain']
        )
        customer_info['phone_number'] = generate_random_phone_number()
        customer_info['first_name'] = generate_random_string(5, 10)
        customer_info['last_name'] = generate_random_string(5, 10)
        customer_info['date_of_birth'] = '06/01/1980'
        customer_info['ssn'] = generate_unique_ssn(web_db_cursor, True)

        # Navigate to /get-account Landing page
        prospect_landing = ProspectLandingPage(driver)
        prospect_landing.enter(env_config['addresses']['prospect_lander_save'])
        assert driver.current_url == env_config['addresses']['prospect_lander_save']
        prospect_landing.check_cta_buttons_via_get_account()
        prospect_landing.submit_save_email(customer_info['email'])
        print(customer_info['email'])

        # Sign up Page
        customer_info_page = CustomerInfoPage(driver)
        customer_info_page.submit_new_account_credentials(customer_info['email'], customer_info['password'])
        # Personal Info Page
        customer_info_page.submit_personal_info(customer_info)

        # Contact Details Page
        customer_info_page.submit_contact_details(customer_info)

        # Review Info Page
        customer_info_page.review_your_info()

        # Product Application Page / Plaid
        cma_product_application_page = CMAProductApplicationPage(driver)
        cma_product_application_page.navigate_into_link_bank_account()

        # Plaid Flow
        link_bank_account_page = LinkBankAccountPage(driver)
        link_bank_account_page.link_account_via_plaid(
            env_config['customer_info_new_customer_app']['plaid_username'],
            env_config['customer_info_new_customer_app']['plaid_password'],
            PlaidBank.CHASE, 'savings')

        # Product Application Page / Opening Deposit
        cma_product_application_page = CMAProductApplicationPage(driver)
        cma_product_application_page.submit_opening_deposit_amount(50)

        # Recurring Deposits
        cma_product_application_page.choose_recurring_deposit_options(False)

        # Submit PWIF
        pwif_page = PWIFPage(driver)
        pwif_page.choose_pwif_amount(PWIFAmount.MID_AMOUNT)

        # Product Application Page / Review Opening Deposit page
        cma_product_application_page.review_and_confirm_deposit_details()

        # Product Application Page / Submit Application page
        cma_product_application_page.confirm_and_submit_product_application(survey=False)

        # Dashboard and validation
        dashboard_page = DashboardPage(driver)
        dashboard_page.wait_until_dashboard_displayed()
        assert dashboard_page.get_product_status(Products.SAVE) == ProductApplicationStatus.COMPLETED
