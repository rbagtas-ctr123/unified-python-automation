import pages.platform.web.prospect_landing_locators_web as locators
from pages.platform.prospect_landing_page import ProspectLandingPage
from pages.base_pages import WebPageType
from pages.elements.base_elements import BaseElement, TextElement


class ProspectLandingPageWeb(ProspectLandingPage, WebPageType):
    """Interface class for setting up a user's account by submitting an email and password for their account."""

#  Landing url  method
    def enter(self, address: str):
        """ Enter the Sign Up flow """
        self.driver.get(address)

    def submit_get_started_email(self, email: str):
        """ Open Get Started Model and submit email """
        BaseElement(self.driver, locators.HEADER_GET_STARTED_BUTTON).click()
        BaseElement(self.driver, locators.GET_STARTED_BUTTON).wait_until_displayed()
        TextElement(self.driver, locators.GET_STARTED_EMAIL_INPUT).set_text(email)
        BaseElement(self.driver, locators.GET_STARTED_BUTTON).click()

#  ~/get-account steps
    def check_cta_buttons_via_get_account(self):
        """ Verifies buttons are currently present"""
        BaseElement(self.driver, locators.GET_STARTED_GET_ACCOUNT_TOP_BODY_BUTTON).displayed()
        BaseElement(self.driver, locators.GET_STARTED_GET_ACCOUNT_MID_BODY_BUTTON).displayed()
        BaseElement(self.driver, locators.GET_STARTED_GET_ACCOUNT_BOTTOM_BODY_BUTTON).displayed()

    def submit_get_account_email(self, email: str):
        """Initiates Sign Up Flow for ~/get-account, ~/get-account-100, ~/get-account-pride"""
        BaseElement(self.driver, locators.GET_STARTED_GET_ACCOUNT_TOP_BODY_BUTTON).wait_until_displayed()
        TextElement(self.driver, locators.GET_STARTED_ENTER_EMAIL_TOP_BODY_FIELD).set_text(email)
        BaseElement(self.driver, locators.GET_STARTED_GET_ACCOUNT_TOP_BODY_BUTTON).click()

    def submit_get_account_tesla_email(self, email: str):
        """ Initiates Sign Up Flow for ~/get-account-teslap2019 """
        BaseElement(self.driver, locators.GET_STARTED_TESLA_ENTER_EMAIL_FIELD).wait_until_displayed()
        TextElement(self.driver, locators.GET_STARTED_TESLA_ENTER_EMAIL_FIELD).set_text(email)
        BaseElement(self.driver, locators.GET_STARTED_TESLA_BUTTON).click()

    def submit_save_email(self, email: str):
        """ Initiates Sign Up Flow for ~/get-account-teslap2019 """
        BaseElement(self.driver, locators.GET_STARTED_SAVE_ENTER_EMAIL_FIELD).wait_until_displayed()
        TextElement(self.driver, locators.GET_STARTED_SAVE_ENTER_EMAIL_FIELD).set_text(email)
        BaseElement(self.driver, locators.GET_STARTED_SAVE_BUTTON).click()
