import pages.platform.android.link_bank_account_locators_android as locators
from pages.platform.link_bank_account_page import LinkBankAccountPage, PlaidBank
from pages.base_pages import AndroidPageType


class LinkBankAccountPageAndroid(LinkBankAccountPage, AndroidPageType):
    """ Implement functions of the Web PlaidPage """

    def link_account_via_plaid(self, plaid_username, plaid_password, bank: PlaidBank, account_type='checking'):
        """ Link a bank account to an Aspiration Product Account via Plaid """
        raise NotImplementedError

    def submit_plaid_account_numbers(self, routing_number, account_number):
        """ Submit new customer's Plaid routing number and account number """
        raise NotImplementedError
