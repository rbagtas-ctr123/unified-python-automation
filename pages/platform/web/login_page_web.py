""" Implement functions of the Web LoginPage """

import pages.platform.web.login_locators_web as locators
from pages.elements.base_elements import BaseElement, TextElement
from pages.platform.login_page import LoginPage, LoginStatus
from pages.base_pages import WebPageType


class LoginPageWeb(LoginPage, WebPageType):
    """ Implement functions of the Web LoginPage """

    def enter(self, address):
        """ Enter the login page
            For web platform, this means loading the login page URL
            For mobile platforms, this means selecting the login option on the main activity """
        self.driver.get(address)

    def submit_login(self, email, password):
        """ Submit credentials to attempt a user login """
        self.wait_until_login_ready()
        TextElement(self.driver, locators.EMAIL_INPUT).set_text(email)
        TextElement(self.driver, locators.PASSWORD_INPUT).set_text(password)
        BaseElement(self.driver, locators.LOGIN_BUTTON).click()

    def wait_until_invalid_credentials_message_displayed(self):
        """ Wait for Invalid Credentials message to appear.  Throw an exception if it does not """
        BaseElement(self.driver, locators.ERROR_MESSAGE).wait_until_displayed()

    def wait_until_login_ready(self):
        """ Wait for the login elements to display.  Throw an exception if any do not display. """
        BaseElement(self.driver, locators.LOGIN_BUTTON).wait_until_displayed()
        TextElement(self.driver, locators.EMAIL_INPUT).wait_until_displayed()
        TextElement(self.driver, locators.PASSWORD_INPUT).wait_until_displayed()

    def get_login_status(self):
        """ Return the status of Login page """
        login_page_displayed = TextElement(self.driver, locators.EMAIL_INPUT).displayed(3)
        error_message = BaseElement(self.driver, locators.ERROR_MESSAGE)
        if not login_page_displayed:
            return LoginStatus.NOT_AT_LOGIN_PAGE
        elif error_message.displayed(3):
            return self.get_error_message_status()
        else:
            return LoginStatus.NO_MESSAGE_PROMPT

    def get_error_message_status(self):
        """ Return Login error message """
        used_email_partial_text = "already created"
        invalid_credentials_partial_text = "don’t recognize the email/password"
        locked_user_partial_text = "currently locked"
        error_message = BaseElement(self.driver, locators.ERROR_MESSAGE)
        if used_email_partial_text in error_message.get_text():
            return LoginStatus.EMAIL_ALREADY_EXITS
        elif invalid_credentials_partial_text in error_message.get_text():
            return LoginStatus.INVALID_CREDENTIALS
        elif locked_user_partial_text in error_message.get_text():
            return LoginStatus.LOCKED_USER
        else:
            return LoginStatus.UNKNOWN_PROMPT
