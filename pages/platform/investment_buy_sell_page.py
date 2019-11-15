""" Interface Page Class for the InvestmentBuySellPage of the Aspiration application

    File must import all implementation subclasses to ensure they are registered during test collection
    Those imports must be after the interface class to avoid circular references during import
"""

from abc import abstractmethod
from pages.base_pages import BasePage


class InvestmentBuySellPage(BasePage, is_interface=True):
    """ Interface Page Class for the InvestmentBuySell page of the Aspiration application """

    # Known investment fund names
    REDWOOD_FUND_NAME = "Redwood Fund"
    REDWOOD_IRA_FUND_NAME = "IRA - Redwood Fund"
    FLAGSHIP_FUND_NAME = "Flagship Fund"
    FLAGSHIP_IRA_FUND_NAME = "IRA - Flagship Fund"

    # Known Investment fund symbols
    REDWOOD_SYMBOL = "REDWX"
    FLAGSHIP_SYMBOL = "ASPFX"

    # Investment Actions
    BUY = "Buy"
    SELL = "Sell"

    @abstractmethod
    def wait_until_investment_buy_sell_page_displayed(self):
        """ Wait until the navigation page is displayed """

    @abstractmethod
    def open_buy_sell_modal(self):
        """ Open modal to buy or sell shares """

    @abstractmethod
    def get_origin_bank_name(self):
        """ Retrieve name of bank being used to purchase shares """

    @abstractmethod
    def prepare_buy_order(self, amount):
        """ Input amount of shares to purchase """

    @abstractmethod
    def finish_purchase_order(self, submit=True):
        """ Submit or cancel purchase order """

    @abstractmethod
    def get_investment_place_order_details(self):
        """ return the results of the investment purchase preview """

    @abstractmethod
    def finish_place_order(self, submit=True):
        """ Final place order or cancel purchase order """

    @abstractmethod
    def wait_until_confirm_place_order_page_is_displayed(self):
        """ Wait until the place order confirmation page is displayed """

    @abstractmethod
    def wait_until_confirmation_page_is_displayed(self):
        """ Wait for confirmation page header to appear"""

    @abstractmethod
    def get_confirmation_details(self):
        """ return the results of the confirmation page """

    @abstractmethod
    def return_to_orders_page(self):
        """ return to investment orders page """

    @abstractmethod
    def get_line_item_summary_details(self):
        """ Get summary from an investment purchase/sale line item """

    @abstractmethod
    def open_summary_modal(self):
        """ Open modal that shows summary of a investment transaction """

    @abstractmethod
    def get_modal_summary_details(self):
        """ get summary details from receipt modal """

    @abstractmethod
    def cancel_scheduled_purchase_order(self):
        """ Cancel schedule purchase order"""

    @abstractmethod
    def get_cancel_confirmation_details(self):
        """ get cancel confirmation details """

    @abstractmethod
    def finish_cancel_order(self):
        """ Cancel order and be done """

    @abstractmethod
    def navigate_to_scheduled_tab(self):
        """ Navigate to the investment scheduled tab """

    @abstractmethod
    def scheduled_tab_is_empty(self):
        """ check that there are no scheduled orders """


from pages.platform.android.investment_buy_sell_page_android import InvestmentBuySellPageAndroid
from pages.platform.ios.investment_buy_sell_page_ios import InvestmentBuySellPageiOS
from pages.platform.web.investment_buy_sell_page_web import InvestmentBuySellPageWeb
