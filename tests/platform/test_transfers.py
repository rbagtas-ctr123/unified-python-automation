""" Tests covering the ACH + Internal transfers functionality of the Aspiration platform. """

import pytest
from utilities.db_helpers.web_db_helpers import get_latest_db_transfer, get_latest_specific_db_audit_trail, \
    clear_db_transfers
import utilities.utils as utils
from pages.platform import LoginPage, NavigationPage, TransfersPage, TransferStatus, DashboardPage, Products
# BANK-1871 todo: remove datetime when we no longer have to wait an arbitrary time for the app to update its balances
import datetime

# The largest transfer amount we will attempt per transfer
MAXIMUM_TRANSFER_AMOUNT = 5


@pytest.mark.transfers
@pytest.mark.regression
@pytest.mark.platform("android", "chrome", "firefox")
class TestTransfers:

    # QA-317 To-Do : turn off skip when we discover why calendar is not appearing reliably
    @pytest.mark.critical
    def test_schedule_and_cancel_ach_deposit(self, env_config, driver):
        """ Schedule & cancel an ACH deposit from an external account into the customer's Spend product """

        user_config = env_config['customer_info_spend_save']
        login_page = LoginPage(driver)
        login_page.enter(env_config['addresses']['login'])
        login_page.submit_login(user_config['email'], user_config['password'])
        dashboard = DashboardPage(driver)
        dashboard.wait_until_dashboard_displayed()
        navigation = NavigationPage(driver)
        navigation.show_transfers()
        transfers_page = TransfersPage(driver)
        transfers_page.wait_until_transfers_displayed()
        transfers_page.cancel_all_scheduled_transfers()

        # create transfer
        transfer_amount = utils.generate_random_dollar_amount(MAXIMUM_TRANSFER_AMOUNT)
        transfers_page.prepare_transfer(transfer_amount, transfers_page.SPEND_ACCOUNT, user_config["linked_account"])
        transfers_page.schedule_transfer(days_in_future=31)
        transfers_page.submit_transfer_request()
        preview_details = transfers_page.transfer_request_result()
        assert preview_details["status"] == TransferStatus.SCHEDULED
        assert preview_details['amount'] == transfer_amount
        assert transfers_page.SPEND_ACCOUNT in preview_details['from']
        assert user_config["linked_account"] in preview_details['to']
        transfers_page.dismiss_transfer_result()

        # Bank-1781 todo:  We must navigate back to the dashboard first to see the scheduled transfer display
        navigation.return_to_dashboard()
        navigation.show_transfers()
        transfers_page.wait_until_transfers_displayed()
        transfers_page.show_scheduled_transfers()

        # verify scheduled transfer displays
        expected_date = utils.future_business_day(31)
        expected_month_day = (expected_date.strftime('%B') + ' ' + str(expected_date.day)).lower()
        scheduled_details = transfers_page.next_scheduled_transfer_summary()
        assert expected_month_day in scheduled_details['date'].lower()

        # BANK-1683 To-Do: Verify the summary once the locators allow it
        # assert transfer_amount == scheduled_details['amount']
        # assert transfers_page.SPEND_ACCOUNT in scheduled_details['from']
        # assert user_config["linked_account"] == scheduled_details['to']
        transfers_page.cancel_all_scheduled_transfers()

    @pytest.mark.environment("alpha")
    def test_verify_db_records_ach_deposit(self, env_config, driver, web_db_connection):
        """ confirm DB records and audits the creation of an ACH deposit transfer """

        user_config = env_config['customer_info_spend_save']
        login_page = LoginPage(driver)
        login_page.enter(env_config['addresses']['login'])
        login_page.submit_login(user_config['email'], user_config['password'])
        dashboard = DashboardPage(driver)
        dashboard.wait_until_dashboard_displayed()
        navigation = NavigationPage(driver)
        navigation.show_transfers()
        transfers_page = TransfersPage(driver)
        transfers_page.cancel_all_scheduled_transfers()

        # create transfer
        transfer_amount = utils.generate_random_dollar_amount(MAXIMUM_TRANSFER_AMOUNT)
        transfers_page.prepare_transfer(transfer_amount, transfers_page.SPEND_ACCOUNT, user_config["linked_account"])
        transfers_page.schedule_transfer(days_in_future=4)
        transfers_page.submit_transfer_request()
        transfers_page.dismiss_transfer_result()

        # verify scheduled transfer in the database
        transfer_data = get_latest_db_transfer(web_db_connection, user_config['user_id'], user_config["linked_account"])
        assert transfer_data.status == TransferStatus.SCHEDULED
        audit_data = get_latest_specific_db_audit_trail(web_db_connection, user_config['user_id'], 'ACH transfer')
        assert audit_data.audit_trail == ('ACH transfer from {0} to {1} with id {2} created'.format(
            transfers_page.SPEND_ACCOUNT,
            user_config["linked_account"],
            transfer_data.id))
        clear_db_transfers(web_db_connection, user_config['user_id'])

    # BANK-2039 To-Do: remove xfail when https://aspirationpartners.atlassian.net/browse/BANK-2039 is fixed
    @pytest.mark.xfail
    # BANK-1869 todo: re-enable test in production when phantom transfer records bug will not overwhelm monitoring
    @pytest.mark.environment("alpha")
    @pytest.mark.critical
    def test_instant_internal_transfers(self, env_config, driver):
        """ Perform instant transfers between Spend and Save accounts """

        user_config = env_config['customer_info_spend_save']
        login_page = LoginPage(driver)
        login_page.enter(env_config['addresses']['login'])
        login_page.submit_login(user_config['email'], user_config['password'])
        dashboard = DashboardPage(driver)
        dashboard.wait_until_dashboard_displayed()
        initial_spend_balance = dashboard.get_product_balance(Products.SPEND)
        initial_save_balance = dashboard.get_product_balance(Products.SAVE)
        navigation = NavigationPage(driver)
        navigation.show_transfers()
        transfers_page = TransfersPage(driver)
        transfers_page.wait_until_transfers_displayed()

        # create first instant transfer
        transfer_amount = utils.generate_random_dollar_amount(MAXIMUM_TRANSFER_AMOUNT)
        transfers_page.prepare_transfer(transfer_amount, transfers_page.SPEND_ACCOUNT, transfers_page.SAVE_ACCOUNT)
        transfers_page.schedule_transfer(days_in_future=0)
        transfers_page.submit_transfer_request()
        preview_details = transfers_page.transfer_request_result()
        assert preview_details["status"] == TransferStatus.COMPLETED
        transfers_page.dismiss_transfer_result()

        # transfer funds back
        transfers_page.prepare_transfer(transfer_amount, transfers_page.SAVE_ACCOUNT, transfers_page.SPEND_ACCOUNT)
        transfers_page.schedule_transfer(days_in_future=0)
        transfers_page.submit_transfer_request()
        preview_details = transfers_page.transfer_request_result()

        # BANK-1871 todo: remove when we no longer have to wait an arbitrary time for the app to update its balances
        confirmation_time = datetime.datetime.now() + datetime.timedelta(seconds=20)

        assert preview_details["status"] == TransferStatus.COMPLETED
        transfers_page.dismiss_transfer_result()

        # Verify the post-transfer amounts
        navigation.return_to_dashboard()

        # BANK-1871 todo: remove when we no longer have to wait an arbitrary time for the app to update its balances
        # Keep leaving & returning to the dashboard looking for updated balances until the confirmation time passes
        after_spend_balance = dashboard.get_product_balance(Products.SPEND)
        after_save_balance = dashboard.get_product_balance(Products.SAVE)
        while (after_spend_balance != initial_spend_balance) or (after_save_balance != initial_save_balance) and \
                datetime.datetime.now() < confirmation_time:
            navigation.show_transfers()
            navigation.return_to_dashboard()
            after_spend_balance = dashboard.get_product_balance(Products.SPEND)
            after_save_balance = dashboard.get_product_balance(Products.SAVE)

        assert dashboard.get_product_balance(Products.SPEND) == initial_spend_balance
        assert dashboard.get_product_balance(Products.SAVE) == initial_save_balance
