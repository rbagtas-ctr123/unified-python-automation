from pages.base_pages import AndroidPageType

from pages.platform.cma_product_application_page import CMAProductApplicationPage
import pages.platform.android.cma_product_application_locators_android as locators


class CMAProductApplicationPageAndroid(CMAProductApplicationPage, AndroidPageType):
    """
    Interface page for the CMA Spend & Save Application or Save Application
    Typically the following is performed in this order:
     - Submits an Opening Deposit
     - Navigates into Link a Bank Account
     - Accepts the Opening Deposit
     - Submits the CMA application
     - Completes Attribution survey
     - Navigates to Aspiration Dashboard
    """

    def submit_opening_deposit_amount(self, deposit_amount):
        """ Submit an opening deposit amount for the new product """
        raise NotImplementedError

    def choose_recurring_deposit_options(self, opt_in=False):
        """ Submit the recurring deposit form or skip setting up a recurring deposit """
        raise NotImplementedError

    def navigate_into_link_bank_account(self):
        """ Confirm we can navigate into linking a bank, then do it """
        raise NotImplementedError

    def review_and_confirm_deposit_details(self):
        """
        Review the deposit and continues to Application Submission page
        Confirms the Application Submission step displays after confirmation
        """
        raise NotImplementedError

    def confirm_and_submit_product_application(self, survey):
        """ Submit the Product Application """
        raise NotImplementedError

    def complete_attribution_survey(self):
        """ Select an option on the Attribution Survey and complete the survey """
        raise NotImplementedError
