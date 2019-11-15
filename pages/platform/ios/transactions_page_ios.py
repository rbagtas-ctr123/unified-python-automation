""" Implement functions of the iOS TransactionsPage """

import pages.platform.ios.transactions_locators_ios as locators
from pages.platform.transactions_page import TransactionsPage
from pages.base_pages import iOSPageType


class TransactionsPageiOS(TransactionsPage, iOSPageType):
    """ Implement functions of the iOS TransactionsPage """

    def wait_until_transactions_displayed(self, account):
        """ Wait until requested transactions page is displayed """
        raise NotImplementedError

    def get_last_transaction_summary(self):
        """ Return summarized details of last transaction, or None if no transactions are displayed
        Data is returned as a 'Transaction' object """
        raise NotImplementedError

    def view_last_transaction_details(self):
        """ Open the last transaction """
        raise NotImplementedError

    def get_transaction_details(self):
        """ Return details of displayed transaction
        Data is returned as a 'Transaction' object """
        raise NotImplementedError

    def close_transaction_details(self):
        """ Close viewed transaction details and return to the transaction summary """
        raise NotImplementedError
