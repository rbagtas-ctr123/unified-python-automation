""" Implement functions of the iOS LoginPage """

import pages.platform.ios.login_locators_ios as locators
from pages.elements.base_elements import BaseElement, TextElement
from pages.platform.login_page import LoginPage
from pages.base_pages import iOSPageType
from selenium.webdriver.common.keys import Keys


class LoginPageiOS(LoginPage, iOSPageType):
    """ Implement functions of the iOS LoginPage """

    def enter(self, address):
        """ Enter the login page
            For web platform, this means loading the login page URL
            For mobile platforms, this means selecting the login option on the main activity """
        self.driver.launch_app()
        BaseElement(self.driver, locators.LOGIN_ENTRY_BUTTON).click()

    def submit_login(self, email, password):
        """ Submit credentials to attempt a user login """
        self.wait_until_login_ready()
        TextElement(self.driver, locators.EMAIL_INPUT).set_text(email)
        TextElement(self.driver, locators.PASSWORD_INPUT).set_text(password)
        TextElement(self.driver, locators.PASSWORD_INPUT).send_keypress(Keys.RETURN)

    def wait_until_invalid_credentials_message_displayed(self):
        """ Wait for Invalid Credentials message to appear.  Throw an exception if it does not """
        raise NotImplementedError

    def wait_until_login_ready(self):
        """ Wait for the login elements to display.
            Throw an exception if any do not display. """
        TextElement(self.driver, locators.EMAIL_INPUT).wait_until_displayed()
        TextElement(self.driver, locators.PASSWORD_INPUT).wait_until_displayed()

    def get_login_status(self):
        """ Return the status of Login page """
