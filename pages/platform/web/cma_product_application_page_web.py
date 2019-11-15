from pages.base_pages import WebPageType
from pages.elements.base_elements import BaseElement, TextElement

from pages.platform.cma_product_application_page import CMAProductApplicationPage
import pages.platform.web.cma_product_application_locators_web as locators


class CMAProductApplicationPageWeb(CMAProductApplicationPage, WebPageType):
    """ Implement functions of the Web CMAProductApplicationPage """

    def submit_opening_deposit_amount(self, deposit_amount):
        """ Submit an opening deposit amount for the new product """
        TextElement(self.driver, locators.DEPOSIT_INPUT).set_text(deposit_amount)
        BaseElement(self.driver, locators.NEXT_BUTTON).click()

    # todo GROW-1598:Create Recurring Deposit Functionality for Automation
    def choose_recurring_deposit_options(self, opt_in=False):
        """ Submit the recurring deposit form or skip setting up a recurring deposit """
        if opt_in:
            raise NotImplementedError
        else:
            BaseElement(self.driver, locators.NEXT_BUTTON).click()
            TextElement(self.driver, locators.RECURRING_DEPOSIT_TITLE).wait_until_not_displayed()

    def navigate_into_link_bank_account(self):
        """ Confirm we can navigate into linking a bank, then do it """
        BaseElement(self.driver, locators.LINK_BANK_ACCOUNT_NEXT_BUTTON).click()

    def review_and_confirm_deposit_details(self):
        """
        Review the deposit and continues to Application Submission page
        Confirms the Application Submission step displays after confirmation
        """
        BaseElement(self.driver, locators.REVIEW_YOUR_DEPOSIT_TITLE).wait_until_displayed()
        BaseElement(self.driver, locators.NEXT_BUTTON).click()
        BaseElement(self.driver, locators.SUBMIT_APPLICATION_BUTTON).wait_until_displayed()

    def confirm_and_submit_product_application(self, survey):
        """ Submit the Product Application """
        if survey is True:
            BaseElement(self.driver, locators.SUBMIT_APPLICATION_BUTTON).click()
            BaseElement(self.driver, locators.SURVEY_MODAL_NEXT_STEPS_BUTTON).wait_until_displayed()
            self.complete_attribution_survey()
            BaseElement(self.driver, locators.GET_STARTED_MY_DASHBOARD_BUTTON).click()
        else:
            BaseElement(self.driver, locators.SUBMIT_APPLICATION_BUTTON).click()
            BaseElement(self.driver, locators.CONGRATS_SAVE_MODAL_EXIT_BUTTON).wait_until_displayed()
            BaseElement(self.driver, locators.CONGRATS_SAVE_MODAL_EXIT_BUTTON).click()
            BaseElement(self.driver, locators.REFERRAL_MODAL_EXIT_BUTTON).wait_until_displayed()
            BaseElement(self.driver, locators.REFERRAL_MODAL_EXIT_BUTTON).click()
            BaseElement(self.driver, locators.REFERRAL_MODAL_EXIT_BUTTON).wait_until_not_displayed()
            BaseElement(self.driver, locators.SKIP_PHOTO_MODAL_BUTTON).click()
            BaseElement(self.driver, locators.GOT_IT_THANKS_MODAL_CONTINUE_BUTTON).click()

    def complete_attribution_survey(self):
        """ Select an option on the Attribution Survey and complete the survey """
        BaseElement(self.driver, locators.SURVEY_TV_OPTION).click()
        BaseElement(self.driver, locators.SURVEY_MODAL_NEXT_STEPS_BUTTON).click()
