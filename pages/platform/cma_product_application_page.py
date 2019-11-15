from abc import abstractmethod
from pages.base_pages import BasePage


class CMAProductApplicationPage(BasePage, is_interface=True):
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

    @abstractmethod
    def submit_opening_deposit_amount(self, deposit_amount):
        """ Submit an opening deposit amount for the new product """

    @abstractmethod
    def choose_recurring_deposit_options(self, opt_in=False):
        """ Submit the recurring deposit form or skip setting up a recurring deposit """

    @abstractmethod
    def navigate_into_link_bank_account(self):
        """ Confirm we can navigate into linking a bank, then do it """

    @abstractmethod
    def review_and_confirm_deposit_details(self):
        """
        Review the deposit and continues to Application Submission page
        Confirms the Application Submission step displays after confirmation
        """

    @abstractmethod
    def confirm_and_submit_product_application(self, survey):
        """ Submit the Product Application """

    @abstractmethod
    def complete_attribution_survey(self):
        """ Select an option on the Attribution Survey and complete the survey """


from pages.platform.web.cma_product_application_page_web import CMAProductApplicationPageWeb
from pages.platform.ios.cma_product_application_page_ios import CMAProductApplicationPageiOS
from pages.platform.android.cma_product_application_page_android import CMAProductApplicationPageAndroid
