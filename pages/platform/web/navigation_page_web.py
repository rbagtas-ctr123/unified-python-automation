""" Implement functions of the Web Navigation Page """

import pages.platform.web.navigation_locators_web as locators
from pages.elements.base_elements import BaseElement
from pages.platform.navigation_page import NavigationPage
from pages.base_pages import WebPageType


class NavigationPageWeb(NavigationPage, WebPageType):
    """ Implement functions of the Web Navigation Page """

    # TODO QA-258: Update to look for correct locators relevant to the navigation page
    def wait_until_navigation_displayed(self):
        """ Wait until the navigation page is displayed """
        BaseElement(self.driver, locators.LOGOUT_LINK).wait_until_displayed()

    def logout(self):
        """ Log out """
        logout_link = BaseElement(self.driver, locators.LOGOUT_LINK)
        logout_link.scroll_into_viewport()
        logout_link.click()

    def show_transfers(self):
        """ Show transfers page """
        BaseElement(self.driver, locators.TRANSFERS_LINK).click()

    def show_spend_transactions(self):
        """ Show spend transactions page """
        BaseElement(self.driver, locators.SPEND_PRODUCT_LINK).click()

    def show_save_transactions(self):
        """ Show save transactions page """
        BaseElement(self.driver, locators.SAVE_PRODUCT_LINK).click()

    def show_redwood_investment_orders(self):
        """ Show investment buy/sell page """
        BaseElement(self.driver, locators.REDWOOD_FUND_PRODUCT_LINK).click()
        BaseElement(self.driver, locators.REDWOOD_FUND_BUY_SELL_PRODUCT_LINK).click()

    def return_to_dashboard(self):
        """ Navigate back to the customer dashboard """
        BaseElement(self.driver, locators.DASHBOARD_BUTTON).click()
        self.wait_until_navigation_displayed()

    def navigate_to_settings_page(self):
        """ Navigate to Settings page """
        BaseElement(self.driver, locators.SETTINGS_LINK).click()

    def navigate_to_insurance_page(self):
        """ Navigate to Insurance page """
        BaseElement(self.driver, locators.INSURANCE_LINK).click()
