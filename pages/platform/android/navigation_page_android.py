""" Implement functions of the Android Dashboard Page """

import pages.platform.android.navigation_locators_android as locators
from pages.elements.base_elements import BaseElement
from pages.platform.navigation_page import NavigationPage
from pages.base_pages import AndroidPageType


class NavigationPageAndroid(NavigationPage, AndroidPageType):
    """ Implement functions of the Android Navigation Page """

    def wait_until_navigation_displayed(self):
        """ Wait until the navigation page is displayed """
        BaseElement(self.driver, locators.DRAWER_BUTTON).wait_until_displayed()

    def logout(self):
        """ Log out """
        BaseElement(self.driver, locators.DRAWER_BUTTON).click()
        BaseElement(self.driver, locators.VIEW_SETTINGS_BUTTON).click()

        # QA-279 todo: Remove this wait + touch scrolling when the UiAutomator locator works again
        BaseElement(self.driver, locators.USERNAME_TEXT).wait_until_displayed()
        self.touch_scroll_up()

        BaseElement(self.driver, locators.LOGOUT_BUTTON).click()
        BaseElement(self.driver, locators.ALERT_YES_BUTTON).click()

    def show_spend_transactions(self):
        """ Show spend transactions page """
        raise NotImplementedError

    def show_save_transactions(self):
        """ Show save transactions page """
        raise NotImplementedError

    def return_to_dashboard(self):
        """ Navigate back to the customer dashboard """
        location = BaseElement(self.driver, locators.LOCATION_TEXT)
        # Begin navigation if we are not already at the dashboard
        if location.get_text() != 'Account Summary':
            drawer_button = BaseElement(self.driver, locators.DRAWER_BUTTON)
            if drawer_button.not_displayed():
                # If the drawer button isn't displayed, then we need to click the back-button to make it appear
                back_button = BaseElement(self.driver, locators.NAVIGATE_UP_BUTTON)
                if back_button.displayed(5):
                    back_button.click()
            drawer_button.click()
            BaseElement(self.driver, locators.SUMMARY_BUTTON).click()
        location.wait_until_displayed()

    def show_transfers(self):
        """ Show the transfers page """
        BaseElement(self.driver, locators.DRAWER_BUTTON).click()
        BaseElement(self.driver, locators.MANAGE_BUTTON).click()
        BaseElement(self.driver, locators.TRANSFERS_BUTTON).click()
