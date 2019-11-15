import pages.platform.web.link_bank_account_locators_web as locators
from pages.platform.link_bank_account_page import LinkBankAccountPage, PlaidBank

from pages.base_pages import WebPageType
from pages.elements.base_elements import BaseElement, TextElement, IframeElement

class LinkBankAccountPageWeb(LinkBankAccountPage, WebPageType):
    """ Implement functions of the Web PlaidPage """

    def link_account_via_plaid(self, plaid_username, plaid_password, bank: PlaidBank,
                               account_type='checking'):
        """ Link a bank account to an Aspiration Product Account via Plaid """
        # Switch to Privacy iframe
        IframeElement(self.driver, locators.PLAID_IFRAME).switch_to_iframe(start_at_default_content=True)
        BaseElement(self.driver, locators.PLAID_PRIVACY_CONTINUE_BUTTON).click()
        # Switch to Select Bank iframe
        IframeElement(self.driver, locators.PLAID_IFRAME).switch_to_iframe(start_at_default_content=True)
        TextElement(self.driver, locators.BANK_SEARCH_INPUT).set_text(bank.value)
        BaseElement(self.driver, locators.bank_option(bank.value)).click()
        # Switch to login iframe
        IframeElement(self.driver, locators.PLAID_IFRAME).switch_to_iframe(start_at_default_content=True)
        TextElement(self.driver, locators.PLAID_LOGIN_USER_ID_INPUT).set_text(plaid_username)
        TextElement(self.driver, locators.PLAID_LOGIN_PASSWORD_INPUT).set_text(plaid_password)
        BaseElement(self.driver, locators.PLAID_LOGIN_CONTINUE_BUTTON).click()
        # Switch to link account iframe
        IframeElement(self.driver, locators.PLAID_IFRAME).switch_to_iframe(start_at_default_content=True)
        if account_type is 'checking':
            BaseElement(self.driver, locators.PLAID_LINK_CHECKING_OPTION).click()
        elif account_type is 'savings':
            BaseElement(self.driver, locators.PLAID_LINK_SAVINGS_OPTION).click()
        else:
            raise ValueError(f"'{account_type}' is not a valid account_type value")
        BaseElement(self.driver, locators.PLAID_LINK_ACCOUNT_CONTINUE_BUTTON).click()
        self.driver.switch_to.default_content()

    def submit_plaid_account_numbers(self, routing_number, account_number):
        """ Submit new customer's Plaid routing number and account number """
        IframeElement(self.driver, locators.PLAID_IFRAME).switch_to_iframe(start_at_default_content=True)
        TextElement(self.driver, locators.ROUTING_NUMBER_INPUT).set_text(routing_number)
        BaseElement(self.driver, locators.PLAID_LINK_ACCOUNT_CONTINUE_BUTTON).click()
        TextElement(self.driver, locators.ACCOUNT_NUMBER_INPUT).set_text(account_number)
        BaseElement(self.driver, locators.PLAID_LINK_ACCOUNT_CONTINUE_BUTTON).click()
        TextElement(self.driver, locators.ACCOUNT_NUMBER_INPUT).set_text(account_number)
        BaseElement(self.driver, locators.PLAID_LINK_ACCOUNT_CONTINUE_BUTTON).click()
        BaseElement(self.driver, locators.PLAID_SUCCESS_HEADER).wait_until_displayed()
        BaseElement(self.driver, locators.PLAID_LINK_ACCOUNT_CONTINUE_BUTTON).click()
        self.driver.switch_to.default_content()
