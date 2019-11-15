""" Tests covering the transactions functionality of the Aspiration platform. """

import pytest
from pages.platform import LoginPage, NavigationPage, TransactionsPage, DashboardPage


@pytest.mark.transactions
@pytest.mark.regression
@pytest.mark.platform("android", "chrome", "firefox")
class TestTransactions:

    @pytest.mark.critical
    def test_cma_transaction_details_display(self, env_config, driver):
        """ Confirm CMA transaction data is displayed on the Transaction Page """

        user_details = env_config['customer_info_spend_save']
        login_page = LoginPage(driver)
        login_page.enter(env_config['addresses']['login'])
        login_page.submit_login(user_details['email'], user_details['password'])
        dashboard = DashboardPage(driver)
        dashboard.wait_until_dashboard_displayed()
        navigation = NavigationPage(driver)
        navigation.show_spend_transactions()
        transactions_page = TransactionsPage(driver)

        # view transaction details
        transactions_page.wait_until_transaction_page_displayed(transactions_page.SPEND_ACCOUNT)
        transaction_details = transactions_page.get_most_recent_transaction_summary()
        assert '$' in transaction_details['amount']
        assert len(transaction_details['description']) > 0

        # view transaction modal details
        transactions_page.open_transaction_modal_details()
        transaction_modal_details = transactions_page.get_transaction_modal_details()
        assert transaction_details['description'] == transaction_modal_details['description']
        assert transaction_details['amount'] == transaction_modal_details['amount']
