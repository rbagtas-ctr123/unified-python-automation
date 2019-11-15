
import pages.platform.web.insurance_locators_web as locators
from pages.elements.base_elements import BaseElement, WindowElement
from pages.platform.insurance_page import InsurancePage
from pages.base_pages import WebPageType


class InsurancePageWeb(InsurancePage, WebPageType):
    """Implements functions of the Web Insurance Page"""

    def wait_until_insurance_displayed(self):
        """ Wait until the Insurance page is displayed """
        BaseElement(self.driver, locators.INSURANCE_HEADER).wait_until_displayed()

    def navigate_to_lemonade_renters_page(self):
        """ Open a new tab to Lemonade's aspiration page using the Renter Insurance button """
        BaseElement(self.driver, locators.RENTERS_INSURANCE_BUTTON).click()

    def navigate_to_lemonade_homeowners_page(self):
        """ Open a new tab to Lemonade's aspiration page using the Homeowner Insurance button """
        BaseElement(self.driver, locators.HOMEOWNER_INSURANCE_BUTTON).click()

    def wait_until_lemonade_insurance_page_displayed(self):
        """ Wait until Lemonade website is displayed and switch the tab back to default"""
        WindowElement(self.driver).wait_until_window_switched(locators.LEMONADE_WEBSITE_HEADER)
        BaseElement(self.driver, locators.LEMONADE_WEBSITE_HEADER).wait_until_displayed()
