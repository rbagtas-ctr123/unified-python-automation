""" Implement functions of the iOS InvestmentBuySell Page """
import pages.platform.ios.investment_buy_sell_locators_ios as locators
from pages.platform.investment_buy_sell_page import InvestmentBuySellPage
from pages.base_pages import iOSPageType


class InvestmentBuySellPageiOS(InvestmentBuySellPage, iOSPageType):

    def wait_until_investment_buy_sell_page_displayed(self):
        """ Wait until the navigation page is displayed """
        raise NotImplementedError

    def open_buy_sell_modal(self):
        """ Open modal to buy or sell shares """
        raise NotImplementedError

    def get_origin_bank_name(self):
        """ Retrieve name of bank being used to purchase shares """
        raise NotImplementedError

    def prepare_buy_order(self, amount):
        """ Input amount of shares to purchase """
        raise NotImplementedError

    def finish_purchase_order(self, submit=True):
        """ Submit or cancel purchase order """
        raise NotImplementedError

    def get_investment_place_order_details(self):
        """ return the results of the investment purchase preview """
        raise NotImplementedError

    def finish_place_order(self, submit=True):
        """ Final place order or cancel purchase order """
        raise NotImplementedError

    def wait_until_confirm_place_order_page_is_displayed(self):
        """ Wait until the place order confirmation page is displayed """
        raise NotImplementedError

    def wait_until_confirmation_page_is_displayed(self):
        """ Wait for confirmation page header to appear"""
        raise NotImplementedError

    def get_confirmation_details(self):
        """ return the results of the confirmation page """
        raise NotImplementedError

    def return_to_orders_page(self):
        """ return to investment orders page """
        raise NotImplementedError

    def get_line_item_summary_details(self):
        """ Get summary from an investment purchase/sale line item """
        raise NotImplementedError

    def open_summary_modal(self):
        """ Open modal that shows summary of a investment transaction """
        raise NotImplementedError

    def get_modal_summary_details(self):
        """ get summary details from receipt modal """
        raise NotImplementedError

    def cancel_scheduled_purchase_order(self):
        """ Cancel schedule purchase order"""
        raise NotImplementedError

    def get_cancel_confirmation_details(self):
        """ get cancel confirmation details """
        raise NotImplementedError

    def finish_cancel_order(self):
        """ Cancel order and be done """
        raise NotImplementedError

    def navigate_to_scheduled_tab(self):
        """ Navigate to the investment scheduled tab """
        raise NotImplementedError

    def scheduled_tab_is_empty(self):
        """ check that there are no scheduled orders """
        raise NotImplementedError
