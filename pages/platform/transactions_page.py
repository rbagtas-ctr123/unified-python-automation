""" Interface Page Class for the TransactionsPage page of the Aspiration application

    File must import all implementation subclasses to ensure they are registered during test collection
    Those imports must be after the interface class to avoid circular references during import
"""

from abc import abstractmethod
from pages.base_pages import BasePage
from dataclasses import dataclass
from decimal import Decimal
from datetime import date


@dataclass
class Transaction:
    """ Container of transaction information """
    transaction_date: date
    transaction_type: str
    description: str
    amount: Decimal


class TransactionsPage(BasePage, is_interface=True):
    """ Interface Page Class for the TransactionsPage page of the Aspiration application """

    # Labels of known account types
    SPEND_ACCOUNT = 'Aspiration Spend'
    SAVE_ACCOUNT = 'Aspiration Save'

    # Labels of known transaction types
    DEPOSIT = 'Deposit'
    WITHDRAWAL = 'Withdrawal'

    @abstractmethod
    def wait_until_transaction_page_displayed(self, account):
        """ Wait until requested transactions page is displayed """

    @abstractmethod
    def get_most_recent_transaction_summary(self):
        """ Return summarized details of last transaction, or None if no transactions are displayed
        Data is returned as a 'Transaction' object """

    @abstractmethod
    def get_number_of_transactions(self):
        """ Return the number of Transaction summaries shown and the total number of pages shown in pagination """

    @abstractmethod
    def open_transaction_modal_details(self):
        """ Open the most recent transaction modal """

    @abstractmethod
    def get_transaction_modal_details(self):
        """ Return details of displayed transaction in modal
        Data is returned as a 'Transaction' object """

    @abstractmethod
    def close_transaction_details(self):
        """ Close viewed transaction details and return to the transaction summary """


from pages.platform.android.transactions_page_android import TransactionsPageAndroid
from pages.platform.ios.transactions_page_ios import TransactionsPageiOS
from pages.platform.web.transactions_page_web import TransactionsPageWeb
