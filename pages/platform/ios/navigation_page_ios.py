""" Implement functions of the iOS Navigation Page """

import pages.platform.ios.navigation_locators_ios as locators
from pages.elements.base_elements import BaseElement
from pages.platform.navigation_page import NavigationPage
from pages.base_pages import iOSPageType


class NavigationPageiOS(NavigationPage, iOSPageType):
    """ Implement functions of the iOS Navigation Page """

    def wait_until_navigation_displayed(self):
        """ Wait until the navigation page is displayed """
        BaseElement(self.driver, locators.SUMMARY_BUTTON).wait_until_displayed()
        BaseElement(self.driver, locators.IMPACT_BUTTON).wait_until_displayed()
        BaseElement(self.driver, locators.SETTINGS_BUTTON).wait_until_displayed()
        BaseElement(self.driver, locators.MANAGE_BUTTON).wait_until_displayed()

    def logout(self):
        """ Log out """
        BaseElement(self.driver, locators.HEADER_PROFILE_IMAGE).click()
        BaseElement(self.driver, locators.LOGOUT_BUTTON).click()

    def show_transfers(self):
        """ Show transfers page """
        raise NotImplementedError

    def show_spend_transactions(self):
        """ Show spend transactions page """
        raise NotImplementedError

    def show_save_transactions(self):
        """ Show save transactions page """
        raise NotImplementedError

    def return_to_dashboard(self):
        """ Navigate back to the customer dashboard """
        raise NotImplementedError
