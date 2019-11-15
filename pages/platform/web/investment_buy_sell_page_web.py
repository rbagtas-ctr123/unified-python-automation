""" Implement functions of the Web InvestmentBuySellPage """

from pages.elements.base_elements import BaseElement, TextElement
import pages.platform.web.investment_buy_sell_locators_web as locators
from pages.platform.investment_buy_sell_page import InvestmentBuySellPage
from pages.base_pages import WebPageType


class InvestmentBuySellPageWeb(InvestmentBuySellPage, WebPageType):
    """ Implement functions of the Web Investment Buy Sell Page """

    def wait_until_investment_buy_sell_page_displayed(self):
        """ Wait until the investment buy/sell page is displayed """
        BaseElement(self.driver, locators.BUY_SELL_HEADER).wait_until_displayed()

    def navigate_to_scheduled_tab(self):
        # FIXME: QA-344 this needs to verify it landed in the write place but angular is a mess
        """ Navigate to the investment scheduled tab """
        BaseElement(self.driver, locators.SCHEDULED_TAB).click()

    def scheduled_tab_is_empty(self):
        """ check that there are no scheduled orders """
        return BaseElement(self.driver, locators.INVESTMENT_ORDER_SCHEDULED_IS_EMPTY).displayed(5)

    def get_line_item_summary_details(self):
        """ Get summary from an investment purchase/sale line item """
        summary_details = {
            "bank": BaseElement(self.driver, locators.INVESTMENT_ORDER_DESCRIPTION).get_text(),
            "amount": BaseElement(self.driver, locators.INVESTMENT_ORDER_AMOUNT).get_text()
        }
        return summary_details

    # TODO: QA-345 could we possibly combine methods that handle line items (transfers, transactions, and investments)
    def open_summary_modal(self):
        """ Open modal that shows summary of a investment transaction """
        BaseElement(self.driver, locators.INVESTMENT_ORDER_DESCRIPTION).click()
        BaseElement(self.driver, locators.INVESTMENT_ORDER_RECEIPT_MODAL_STATUS).wait_until_displayed()

    def get_modal_summary_details(self):
        """ get summary details from receipt modal """
        bank = BaseElement(self.driver, locators.INVESTMENT_ORDER_RECEIPT_MODAL_DESCRIPTION)
        bank.wait_until_displayed()
        modal_details = {
            "bank": bank.get_text(),
            "amount": BaseElement(self.driver, locators.INVESTMENT_ORDER_RECEIPT_MODAL_AMOUNT).get_text()
        }
        return modal_details

    def open_buy_sell_modal(self):
        """ Open modal to buy or sell shares """
        BaseElement(self.driver, locators.INVESTMENT_ORDER_BUY_SELL_BUTTON).click()
        BaseElement(self.driver, locators.INVESTMENT_ORDER_BUY_SELL_MODAL_HEADER).wait_until_displayed()

    def get_origin_bank_name(self):
        """ Retrieve name of bank being used to purchase shares """
        bank_name = BaseElement(self.driver, locators.INVESTMENT_ORDER_BUY_SELL_MODAL_BANK_NAME).get_text()
        return bank_name

    # TODO: QA-346 Add more options if/when IRA purchase functionality is added
    def prepare_buy_order(self, amount):
        """ Input amount of shares to purchase """
        TextElement(self.driver, locators.INVESTMENT_ORDER_BUY_MODAL_AMOUNT).set_text(str(amount))

    def finish_purchase_order(self, submit=True):
        """ Submit or cancel purchase order """
        if submit:
            BaseElement(self.driver, locators.INVESTMENT_ORDER_BUY_SELL_MODAL_PLACE_ORDER_BUTTON).click()
        else:
            BaseElement(self.driver, locators.INVESTMENT_ORDER_BUY_SELL_MODAL_CANCEL_BUTTON).click()

    def cancel_scheduled_purchase_order(self):
        """ Cancel schedule purchase order"""
        BaseElement(self.driver, locators.INVESTMENT_ORDER_BUY_SELL_MODAL_CANCEL_BUTTON).click()

    # This is a new page to confirm the order before finalizing it
    def wait_until_confirm_place_order_page_is_displayed(self):
        """ Wait until the place order confirmation page is displayed """
        BaseElement(self.driver, locators.INVESTMENT_PLACE_ORDER_AMOUNT).wait_until_displayed()
        BaseElement(self.driver, locators.INVESTMENT_PLACE_ORDER_FUND_SYMBOL).wait_until_displayed()
        BaseElement(self.driver, locators.INVESTMENT_PLACE_ORDER_FUND_NAME).wait_until_displayed()

    def get_investment_place_order_details(self):
        """ return the results of the investment purchase preview """
        purchase_preview = {
            "amount": BaseElement(self.driver, locators.INVESTMENT_PLACE_ORDER_AMOUNT).get_text(),
            "fund_symbol": BaseElement(self.driver, locators.INVESTMENT_PLACE_ORDER_FUND_SYMBOL).get_text(),
            "fund_name": BaseElement(self.driver, locators.INVESTMENT_PLACE_ORDER_FUND_NAME).get_text(),
            "amount_confirmation":
                BaseElement(self.driver, locators.INVESTMENT_PLACE_ORDER_AMOUNT_CONFIRMATION).get_text(),
            "origin_bank": BaseElement(self.driver, locators.INVESTMENT_PLACE_ORDER_ORIGIN_BANK).get_text()
        }
        return purchase_preview

    def finish_place_order(self, submit=True):
        """ Final place order or cancel purchase order """
        if submit:
            BaseElement(self.driver, locators.INVESTMENT_PLACE_ORDER_PROCEED_BUTTON).click()
        else:
            BaseElement(self.driver, locators.INVESTMENT_PLACE_ORDER_CANCEL_BUTTON).click()

    # This is a new page confirming the details of the placed order
    def wait_until_confirmation_page_is_displayed(self):
        """ Wait for confirmation page header to appear"""
        BaseElement(self.driver, locators.INVESTMENT_CONFIRMATION_HEADER).wait_until_displayed(30)

    def get_confirmation_details(self):
        """ return the results of the confirmation page """
        confirmation_details = {
            "action": BaseElement(self.driver, locators.INVESTMENT_CONFIRMATION_ACTION).get_text(),
            "symbol": BaseElement(self.driver, locators.INVESTMENT_CONFIRMATION_SYMBOL).get_text(),
            "description": BaseElement(self.driver, locators.INVESTMENT_CONFIRMATION_DESCRIPTION).get_text(),
            "payment_method": BaseElement(self.driver, locators.INVESTMENT_CONFIRMATION_PAYMENT_METHOD).get_text(),
            "amount": BaseElement(self.driver, locators.INVESTMENT_CONFIRMATION_PAYMENT_AMOUNT).get_text()
        }
        return confirmation_details

    def return_to_orders_page(self):
        """ return to investment orders page"""
        BaseElement(self.driver, locators.INVESTMENT_ORDER_GO_TO_STATUS).click()

    # Methods for Cancel confirmation page
    def get_cancel_confirmation_details(self):
        """ get cancel confirmation details """
        confirmation_details = {
            "amount": BaseElement(self.driver, locators.INVESTMENT_CANCEL_ORDER_AMOUNT).get_text(),
            "fund_symbol": BaseElement(self.driver, locators.INVESTMENT_CANCEL_ORDER_SYMBOL).get_text(),
            "fund_name": BaseElement(self.driver, locators.INVESTMENT_CANCEL_ORDER_FUND).get_text()
        }
        return confirmation_details

    def finish_cancel_order(self):
        """ Cancel order and be done """
        BaseElement(self.driver, locators.INVESTMENT_CANCEL_ORDER_BUTTON).click()
