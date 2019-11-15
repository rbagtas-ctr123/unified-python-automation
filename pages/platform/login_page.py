""" Interface Page Class for the Login page of the Aspiration application

    File must import all implementation subclasses to ensure they are registered during test collection
    Those imports must be after the interface class to avoid circular references during import
"""

from abc import abstractmethod
from pages.base_pages import BasePage
from enum import Enum

class LoginStatus(Enum):
    """ Enum representing the possible status of login """
    EMAIL_ALREADY_EXITS = 1
    INVALID_CREDENTIALS = 2
    LOCKED_USER = 3
    UNKNOWN_PROMPT = 4
    NO_MESSAGE_PROMPT = 5
    NOT_AT_LOGIN_PAGE = 6


class LoginPage(BasePage, is_interface=True):
    """ Interface Page Class for the Login page of the Aspiration application """

    @abstractmethod
    def enter(self, address):
        """ Enter the login page
            For web platform, this means loading the login page URL
            For mobile platforms, this means selecting the login option on the main activity """

    @abstractmethod
    def submit_login(self, email, password):
        """ Submit credentials to attempt a user login """

    @abstractmethod
    def wait_until_invalid_credentials_message_displayed(self):
        """ Wait for Invalid Credentials message to appear.  Throw an exception if it does not """

    @abstractmethod
    def wait_until_login_ready(self):
        """ Wait for the login elements to display.  Throw an exception if any do not display. """

    @abstractmethod
    def get_login_status(self):
        """ Return the status of Login page """


from pages.platform.android.login_page_android import LoginPageAndroid
from pages.platform.ios.login_page_ios import LoginPageiOS
from pages.platform.web.login_page_web import LoginPageWeb
