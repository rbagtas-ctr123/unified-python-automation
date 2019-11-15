"""Implement functions of the Web Insurance Page"""

from abc import abstractmethod
from pages.base_pages import BasePage

class InsurancePage(BasePage, is_interface=True):
    """Implements functions of the Web Insurance Page"""

    @abstractmethod
    def wait_until_insurance_displayed(self):
        """ Wait until the Insurance page is displayed """

    @abstractmethod
    def navigate_to_lemonade_renters_page(self):
        """ Open a new tab to Lemonade's aspiration page using the Renter Insurance button """

    @abstractmethod
    def navigate_to_lemonade_homeowners_page(self):
        """ Open a new tab to Lemonade's aspiration page using the Homeowner Insurance button """

    @abstractmethod
    def wait_until_lemonade_insurance_page_displayed(self):
        """ Wait until Lemonade website is displayed and switch the tab back to default"""


from pages.platform.android.insurance_page_android import InsurancePageAndroid
from pages.platform.ios.insurance_page_ios import InsurancePageiOS
from pages.platform.web.insurance_page_web import InsurancePageWeb
