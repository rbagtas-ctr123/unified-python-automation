""" Implement functions of the Web TransactionsPage """

from pages.elements.base_elements import BaseElement
import pages.platform.web.transactions_locators_web as locators
from pages.platform.transactions_page import TransactionsPage
from pages.base_pages import WebPageType
import utilities.utils as utils


class TransactionsPageWeb(TransactionsPage, WebPageType):
    """ Implement functions of the Web TransactionsPage """

    def wait_until_transaction_page_displayed(self, account):
        """ Wait until requested transactions page is displayed """
        BaseElement(self.driver, locators.AVAILABLE_BALANCE_TEXT).wait_until_displayed()
        transaction_line_item = BaseElement(self.driver, locators.FIRST_TRANSACTION_LINE_ITEM)
        transaction_no_activity_message = BaseElement(self.driver, locators.TRANSACTION_NO_ACTIVITY_MESSAGE)

        if not transaction_line_item.displayed() or not transaction_no_activity_message.displayed():
            return None

    def get_most_recent_transaction_summary(self):
        """ Return summarized details of most recent transaction, or None if no transactions are displayed
        Data is returned as a 'Transaction' object """

        transaction_description = BaseElement(self.driver, locators.FIRST_TRANSACTION_DESCRIPTION)
        transaction_amount = BaseElement(self.driver, locators.FIRST_TRANSACTION_AMOUNT)
        transaction_running_balance = BaseElement(self.driver, locators.FIRST_TRANSACTION_RUNNING_BALANCE)
        transaction_no_activity = BaseElement(self.driver, locators.TRANSACTION_NO_ACTIVITY_MESSAGE)
        if transaction_description.displayed(5):
            transaction_details = \
                {'description': transaction_description.get_text(),
                 'amount': utils.remove_whitespace_from_string(transaction_amount.get_text()),
                 'balance': transaction_running_balance.get_text()}
        elif transaction_no_activity.displayed(5):
            transaction_details = \
                {'description': transaction_no_activity.get_text(),
                 'amount': None,
                 'balance': None}
        else:
            return None
        return transaction_details

    def open_transaction_modal_details(self):
        """ Open the most recent transaction modal """
        transaction_modal_description = BaseElement(self.driver, locators.FIRST_TRANSACTION_DESCRIPTION)
        transaction_modal_description.click()
        BaseElement(self.driver, locators.TRANSACTION_MODAL_DESCRIPTION).wait_until_displayed()

    def get_transaction_modal_details(self):
        """ Return details of displayed transaction in modal
        Data is returned as a 'Transaction' object """
        transaction_modal_description = BaseElement(self.driver, locators.TRANSACTION_MODAL_DESCRIPTION)
        transaction_modal_amount = BaseElement(self.driver, locators.TRANSACTION_MODAL_AMOUNT)
        transaction_modal_date = BaseElement(self.driver, locators.TRANSACTION_MODAL_DATE)
        transaction_modal_details = \
            {'description': transaction_modal_description.get_text(),
             'amount': utils.remove_whitespace_from_string(transaction_modal_amount.get_text()),
             'date': transaction_modal_date.get_text()}
        return transaction_modal_details

    def get_transaction_details(self):
        """ Return details of displayed transaction
        Data is returned as a 'Transaction' object """
        raise NotImplementedError

    def close_transaction_details(self):
        """ Close viewed transaction details and return to the transaction summary """
        raise NotImplementedError

    def get_number_of_transactions(self):
        """ Return the number of Transaction summaries shown and the total number of pages shown in pagination """
        raise NotImplementedError
