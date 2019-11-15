""" Implement functions of the iOS Dashboard Page """

import pages.platform.ios.dashboard_locators_ios as locators
from pages.elements.base_elements import BaseElement
from pages.platform.dashboard_page import DashboardPage
from pages.base_pages import iOSPageType


class DashboardPageiOS(DashboardPage, iOSPageType):
    """ Implement functions of the iOS Dashboard Page """

    def wait_until_dashboard_displayed(self):
        """ Wait until the dashboard page is displayed """
        BaseElement(self.driver, locators.WELCOME_MESSAGE).wait_until_displayed()

    def get_spend_balance(self):
        """ Return the displayed balance of the user's Aspiration Spend Account """
        raise NotImplementedError

    def get_save_balance(self):
        """ Return the displayed balance of the user's Aspiration Save Account """
        raise NotImplementedError

    def get_product_status(self, product):
        """ Return the status of the supplied product """
        raise NotImplementedError

    def continue_product_application(self, product):
        """ Continue a Product Application """
        raise NotImplementedError
