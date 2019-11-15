from abc import abstractmethod
from pages.base_pages import BasePage


class ProspectLandingPage(BasePage, is_interface=True):
    """ Interface Page Class for the Prospect Landing page """

    @abstractmethod
    def enter(self, address: str):
        """
        Enter the Sign Up flow
        For web platform, this means loading a Landing page via the URL
        For mobile platforms, this means selecting the Sign Up option on the main activity
        """

    @abstractmethod
    def submit_get_started_email(self, email: str):
        """ Open Get Started Model and submit email """

    @abstractmethod
    def check_cta_buttons_via_get_account(self):
        """" verifies all get started CTAs are present"""

    @abstractmethod
    def submit_get_account_email(self, email: str):
        """ Enter and submit email from ~/get-account, ~/get-account-100, ~/get-account-pride """

    @abstractmethod
    def submit_get_account_tesla_email(self, email: str):
        """ Enter and submit email from ~/get-account-teslap2019 """

    @abstractmethod
    def submit_save_email(self, email: str):
        """ Enter and submit email from ~/save """


from pages.platform.web.prospect_landing_page_web import ProspectLandingPageWeb
