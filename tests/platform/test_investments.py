""" Tests covering the investment functionality of the Aspiration platform. """

import pytest
import utilities.utils as utils
from pages.platform import LoginPage, NavigationPage, DashboardPage, InvestmentBuySellPage


# The largest investment amount we will attempt per purchase
MAXIMUM_PURCHASE_AMOUNT = 10


@pytest.mark.investment
@pytest.mark.regression
@pytest.mark.platform("chrome", "firefox")
class TestInvestments:

    # FIXME: cannot run this in prod until account is funded
    @pytest.mark.environment("alpha")
    @pytest.mark.critical
    def test_schedule_and_cancel_investment_buy_order(self, env_config, driver):
        """ Schedule & cancel an investment order from the redwood fund """
        user_config = env_config['customer_info_investment']
        login_page = LoginPage(driver)
        login_page.enter(env_config['addresses']['login'])
        login_page.submit_login(user_config['email'], user_config['password'])
        dashboard = DashboardPage(driver)
        dashboard.wait_until_dashboard_displayed()
        navigation = NavigationPage(driver)
        navigation.show_redwood_investment_orders()
        investment_page = InvestmentBuySellPage(driver)
        action = investment_page.BUY
        investment_page.wait_until_investment_buy_sell_page_displayed()
        # TODO: Clear canceled orders
        # Verify there are no scheduled orders
        investment_page.navigate_to_scheduled_tab()
        assert investment_page.scheduled_tab_is_empty(), "There is already a scheduled investment order. " \
                                                         "Please delete it and run the test again"

        # Submit purchase request
        investment_page.open_buy_sell_modal()
        bank = investment_page.get_origin_bank_name()
        purchase_amount = utils.generate_random_dollar_amount(MAXIMUM_PURCHASE_AMOUNT)
        investment_page.prepare_buy_order(purchase_amount)
        investment_page.finish_purchase_order()

        # Confirm and place purchase order
        place_order_details = investment_page.get_investment_place_order_details()
        purchase_amount_string = str(purchase_amount)
        assert purchase_amount_string in place_order_details["amount"]
        assert investment_page.REDWOOD_SYMBOL == place_order_details["fund_symbol"]
        assert investment_page.REDWOOD_FUND_NAME in place_order_details["fund_name"]
        assert purchase_amount_string in place_order_details["amount_confirmation"]
        assert bank in place_order_details["origin_bank"]
        investment_page.finish_place_order()

        # Review order confirmation
        investment_page.wait_until_confirmation_page_is_displayed()
        confirmation_details = investment_page.get_confirmation_details()
        assert action in confirmation_details["action"]
        assert investment_page.REDWOOD_SYMBOL == confirmation_details["symbol"]
        assert investment_page.REDWOOD_FUND_NAME in confirmation_details["description"]
        assert bank in confirmation_details["payment_method"]
        assert purchase_amount_string in confirmation_details["amount"]
        investment_page.return_to_orders_page()

        # Navigate to scheduled purchases and confirm receipt modal
        investment_page.wait_until_investment_buy_sell_page_displayed()
        investment_page.navigate_to_scheduled_tab()
        line_item_summary_details = investment_page.get_line_item_summary_details()
        assert bank in line_item_summary_details["bank"]
        assert purchase_amount_string in line_item_summary_details["amount"]
        investment_page.open_summary_modal()
        receipt_modal_details = investment_page.get_modal_summary_details()
        assert bank in receipt_modal_details["bank"]
        assert purchase_amount_string in receipt_modal_details["amount"]

        # Cancel order, will direct to a new confirm cancel page
        investment_page.cancel_scheduled_purchase_order()
        cancel_confirmation_details = investment_page.get_cancel_confirmation_details()
        assert purchase_amount_string in cancel_confirmation_details["amount"]
        assert investment_page.REDWOOD_SYMBOL == cancel_confirmation_details["fund_symbol"]
        assert investment_page.REDWOOD_FUND_NAME in cancel_confirmation_details["fund_name"]
        investment_page.finish_cancel_order()
        investment_page.wait_until_investment_buy_sell_page_displayed()
