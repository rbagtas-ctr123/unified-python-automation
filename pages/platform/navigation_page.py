""" Interface Page Class for the Navigation page of the Aspiration application

    File must import all implementation subclasses to ensure they are registered during test collection
    Those imports must be after the interface class to avoid circular references during import
"""

from abc import abstractmethod
from pages.base_pages import BasePage


class NavigationPage(BasePage, is_interface=True):
    """ Interface Page Class for the Dashboard page of the Aspiration application """

    @abstractmethod
    def wait_until_navigation_displayed(self):
        """ Check  whether the current page is the dashboard.
            Return true if navigation elements appear
            Return false if they do not """

    @abstractmethod
    def logout(self):
        """ Log out """

    @abstractmethod
    def show_transfers(self):
        """ Show transfers page """

    @abstractmethod
    def show_spend_transactions(self):
        """ Show spend transactions page """

    @abstractmethod
    def show_save_transactions(self):
        """ Show save transactions page """

    @abstractmethod
    def show_redwood_investment_orders(self):
        """ Show investment buy/sell page """

    @abstractmethod
    def return_to_dashboard(self):
        """ Navigate back to the customer dashboard """

    @abstractmethod
    def navigate_to_settings_page(self):
        """ Navigate to Settings page """

    @abstractmethod
    def navigate_to_insurance_page(self):
        """ Navigate to Insurance page """


from pages.platform.android.navigation_page_android import NavigationPageAndroid
from pages.platform.ios.navigation_page_ios import NavigationPageiOS
from pages.platform.web.navigation_page_web import NavigationPageWeb
