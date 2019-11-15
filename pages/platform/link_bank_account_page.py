from abc import abstractmethod
from enum import Enum, IntEnum
from pages.base_pages import BasePage


class PlaidBank(Enum):
    """ Enum for selecting specific banks during the Plaid link account flow
    The members are bound to strings which match the strings used by Plaid to identify different Banks.
    The string value of the enum must match the name of the bank presented by Plaid """
    CHASE = 'Chase'
    WELLS_FARGO = 'Wells Fargo'
    US_BANK = 'US Bank'
    CITI = 'Citi'
    HOUNDSTOOTH = 'Houndstooth Bank'


class LinkBankAccountPage(BasePage, is_interface=True):
    """ Interface Page Class for the Plaid page of the Aspiration application """

    @abstractmethod
    def link_account_via_plaid(self, plaid_username, plaid_password, bank: PlaidBank,
                               account_type='checking'):
        """ Link a bank account to an Aspiration Product Account via Plaid """


class PlaidScore(IntEnum):
    """ User Plaid Score. The values represents to the possible scores a user can have """
    MICRODEPOSIT = -1
    SCORE_0 = 0
    SCORE_1 = 1
    SCORE_2 = 2
    SCORE_3 = 3
    SCORE_4 = 4

    @abstractmethod
    def submit_plaid_account_numbers(self, routing_number, account_number):
        """ Submit new customer's Plaid routing number and account number """


from pages.platform.android.link_bank_account_page_android import LinkBankAccountPageAndroid
from pages.platform.ios.link_bank_account_page_ios import LinkBankAccountPageiOS
from pages.platform.web.link_bank_account_page_web import LinkBankAccountPageWeb
