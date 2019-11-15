""" Implement functions of the Admin Web LoginPage """

import pages.admin.login_locators_web as locators
from pages.elements.base_elements import BaseElement, TextElement, WindowElement
from pages.admin.login_page import AdminLoginPage
from pages.base_pages import WebPageType


class LoginPageWeb(AdminLoginPage, WebPageType):
    """ Implement functions of the Web LoginPage """

    def enter_page(self, address):
        """ Enter the login page
            Loads the page URL """
        self.driver.get(address)

    def get_to_google_login(self):
        """ Wait for admin screen to load, click google icon and wait for modal to display"""
        BaseElement(self.driver, locators.ADMIN_ICON).wait_until_displayed()
        BaseElement(self.driver, locators.GOOGLE_SIGN_IN_BUTTON).wait_until_displayed()
        BaseElement(self.driver, locators.GOOGLE_SIGN_IN_BUTTON).click()
        WindowElement(self.driver).wait_until_window_switched(locators.GOOGLE_EMAIL_OR_PHONE_INPUT)
        BaseElement(self.driver, locators.GOOGLE_EMAIL_OR_PHONE_INPUT).wait_until_displayed()
        BaseElement(self.driver, locators.GOOGLE_SIGN_IN_NEXT_BUTTON).wait_until_displayed()

    def submit_credentials_to_google(self, email):
        """ Open google modal and submit email to sign in through google """
        TextElement(self.driver, locators.GOOGLE_EMAIL_OR_PHONE_INPUT).set_text(email)
        BaseElement(self.driver, locators.GOOGLE_SIGN_IN_NEXT_BUTTON).click()
        BaseElement(self.driver, locators.OKTA_USERNAME_INPUT).wait_until_displayed()
        BaseElement(self.driver, locators.OKTA_PASSWORD_INPUT).wait_until_displayed()
        BaseElement(self.driver, locators.OKTA_SIGN_IN_BUTTON).wait_until_displayed()

    def submit_credentials_to_okta(self, username, password):
        """ Submit credentials to okta and attempt to login """
        TextElement(self.driver, locators.OKTA_USERNAME_INPUT).set_text(username)
        TextElement(self.driver, locators.OKTA_PASSWORD_INPUT).set_text(password)
        BaseElement(self.driver, locators.OKTA_SIGN_IN_BUTTON).click()
        BaseElement(self.driver, locators.GOOGLE_ACCOUNT_VERIFICATION_TEXT).wait_until_displayed()

    def approve_google_authorization(self):
        """ Click continue button to verify use of new credentials
        This is the final step before the dashboard appears"""
        BaseElement(self.driver, locators.GOOGLE_ACCOUNT_CONTINUE_BUTTON).click()
        WindowElement(self.driver).wait_until_one_window_exists()

    def complete_google_authorization(self, email, username, password):
        """submit credentials through google, okta, and verify device"""
        self.submit_credentials_to_google(email)
        self.submit_credentials_to_okta(username, password)
        self.approve_google_authorization()
