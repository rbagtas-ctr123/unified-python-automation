""" Interface Page Class for the Login page of the Admin20 application

    File must import all implementation subclasses to ensure they are registered during test collection
    Those imports must be after the interface class to avoid circular references during import
"""

from abc import abstractmethod
from pages.base_pages import BasePage


class AdminLoginPage(BasePage, is_interface=True):
    """ Interface Page Class for the Login page of the Aspiration application """

    @abstractmethod
    def enter_page(self, address):
        """ Enter the login page
            Loads the page URL """

    @abstractmethod
    def get_to_google_login(self):
        """ Wait for admin screen to load, click google icon and wait for modal to display"""

    @abstractmethod
    def complete_google_authorization(self, email, username, password):
        """submit credentials through google, okta, and verify device"""

import pages.admin.login_page_web
