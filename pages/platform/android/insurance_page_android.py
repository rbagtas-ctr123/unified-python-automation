""" Implement functions of the Android Insurance Page """
import pages.platform.android.insurance_locators_android as locators
from pages.elements.base_elements import BaseElement
from pages.platform.insurance_page import InsurancePage
from pages.base_pages import AndroidPageType


class InsurancePageAndroid(InsurancePage, AndroidPageType):
    """Implements functions of the Web Insurance Page"""

    def wait_until_insurance_displayed(self):
        """ Wait until the Insurance page is displayed """
        raise NotImplementedError

    def navigate_to_lemonade_renters_page(self):
        """ Open a new tab to Lemonade's aspiration page using the Renter Insurance button """
        raise NotImplementedError

    def navigate_to_lemonade_homeowners_page(self):
        """ Open a new tab to Lemonade's aspiration page using the Homeowner Insurance button """
        raise NotImplementedError

    def wait_until_lemonade_insurance_page_displayed(self):
        """ Wait until Lemonade website is displayed and switch the tab back to default"""
        raise NotImplementedError
