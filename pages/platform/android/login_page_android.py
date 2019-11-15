""" Implement functions of the Android LoginPage """

import pages.platform.android.login_locators_android as locators
from pages.elements.base_elements import BaseElement, TextElement
from pages.platform.login_page import LoginPage
from pages.base_pages import AndroidPageType


class LoginPageAndroid(LoginPage, AndroidPageType):
    """ Implement functions of the Android LoginPage """

    def enter(self, address):
        """ Enter the login page
            For web platform, this means loading the login page URL
            For mobile platforms, this means selecting the login option on the main activity """
        entry_button = BaseElement(self.driver, locators.LOGIN_ENTRY_BUTTON)
        entry_button.wait_until_displayed()
        entry_button.click()

    def submit_login(self, email, password):
        """ Submit credentials to attempt a user login """
        self.wait_until_login_ready()
        TextElement(self.driver, locators.EMAIL_INPUT).set_text(email)
        TextElement(self.driver, locators.PASSWORD_INPUT).set_text(password)
        BaseElement(self.driver, locators.LOGIN_SUBMIT_BUTTON).click()

    def wait_until_invalid_credentials_message_displayed(self):
        """ Wait for Invalid Credentials message to appear.  Throw an exception if it does not """
        BaseElement(self.driver, locators.INVALID_CREDENTIALS_MESSAGE).wait_until_displayed()

    def wait_until_login_ready(self):
        """ Wait for the login elements to display.
            Throw an exception if any do not display. """
        TextElement(self.driver, locators.EMAIL_INPUT).wait_until_displayed()
        TextElement(self.driver, locators.PASSWORD_INPUT).wait_until_displayed()
        BaseElement(self.driver, locators.LOGIN_SUBMIT_BUTTON).wait_until_displayed()

    def get_login_status(self):
        """ Return the status of Login page """
        raise NotImplementedError
