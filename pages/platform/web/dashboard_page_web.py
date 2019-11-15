"""Implement functions of the Web Dashboard Page"""

import pages.platform.web.dashboard_locators_web as locators
from pages.elements.base_elements import BaseElement
from pages.platform.dashboard_page import DashboardPage, ProductApplicationStatus, Products
from pages.base_pages import WebPageType
import utilities.utils as utils


class DashboardPageWeb(DashboardPage, WebPageType):
    """Implements functions of the Web Dashboard Page"""

    def wait_until_dashboard_displayed(self):
        """ Wait until the dashboard is displayed """
        BaseElement(self.driver, locators.WELCOME_MESSAGE).wait_until_displayed()
        takeover = BaseElement(self.driver, locators.MARKETING_TAKEOVER_BACKDROP)
        if takeover.displayed():
            BaseElement(self.driver, locators.DISMISS_TAKEOVER_LINK).click()
            takeover.wait_until_gone()
        
    def get_product_balance(self, product):
        """ Return the displayed balance of a user's chosen product """
        if product == Products.SPEND:
            product_balance = BaseElement(self.driver, locators.ASPIRATION_SPEND_BALANCE)    
        elif product == Products.SAVE:
            product_balance = BaseElement(self.driver, locators.ASPIRATION_SAVE_BALANCE)
        elif product == Products.REDWOOD:
            product_balance = BaseElement(self.driver, locators.ASPIRATION_REDWOOD_BALANCE)
        # elif product == Products.FLAGSHIP:
        #     product_balance = BaseElement(self.driver, locators.ASPIRATION_FLAGSHIP_BALANCE)
        else:
            raise ValueError(f"'{product}' is not a valid product")    
        return utils.decimal_from_string(product_balance.get_text())

    def continue_product_application(self, product):
        """ Continue a Product Application """
        self.wait_until_dashboard_displayed()
        if product == Products.SAVE:
            BaseElement(self.driver, locators.CONTINUE_SAVE_APPLICATION_BUTTON).click()
        elif product == Products.SPEND:
            BaseElement(self.driver, locators.CONTINUE_SPEND_SAVE_APPLICATION_BUTTON).click()
        elif product == Products.REDWOOD:
            BaseElement(self.driver, locators.CONTINUE_REDWOOD_APPLICATION_BUTTON).click()
        elif product == Products.FLAGSHIP:
            BaseElement(self.driver, locators.CONTINUE_FLAGSHIP_APPLICATION_BUTTON).click()
        else:
            raise ValueError(f"'{product}' is not a valid product")

    def get_product_status(self, product):
        """
        Return the status of the product
        If an unknown product is submitted, return DOES_NOT_EXIST
        """
        self.wait_until_dashboard_displayed()
        status_locators = {}
        if product == Products.SPEND:
            status_locators[ProductApplicationStatus.IN_PROGRESS] = \
                BaseElement(self.driver, locators.CONTINUE_SPEND_SAVE_APPLICATION_BUTTON)
            status_locators[ProductApplicationStatus.COMPLETED] = \
                BaseElement(self.driver, locators.VIEW_SPEND_ACCOUNT_BUTTON)
            status_locators[ProductApplicationStatus.PENDING] = \
                BaseElement(self.driver, locators.SPEND_SAVE_TELL_YOUR_FRIENDS_BUTTON)
        elif product == Products.SAVE:
            status_locators[ProductApplicationStatus.IN_PROGRESS] = \
                BaseElement(self.driver, locators.CONTINUE_SAVE_APPLICATION_BUTTON)
            status_locators[ProductApplicationStatus.COMPLETED] = \
                BaseElement(self.driver, locators.VIEW_SAVE_ACCOUNT_BUTTON)
            status_locators[ProductApplicationStatus.PENDING] = \
                BaseElement(self.driver, locators.SAVE_TELL_YOUR_FRIENDS_BUTTON)
        elif product == Products.REDWOOD:
            status_locators[ProductApplicationStatus.IN_PROGRESS] = \
                BaseElement(self.driver, locators.CONTINUE_REDWOOD_APPLICATION_BUTTON)
            status_locators[ProductApplicationStatus.COMPLETED] = \
                BaseElement(self.driver, locators.VIEW_REDWOOD_ACCOUNT_BUTTON)
            status_locators[ProductApplicationStatus.PENDING] = \
                BaseElement(self.driver, locators.REDWOOD_TELL_YOUR_FRIENDS_BUTTON)
        elif product == Products.FLAGSHIP:
            status_locators[ProductApplicationStatus.IN_PROGRESS] = \
                BaseElement(self.driver, locators.CONTINUE_FLAGSHIP_APPLICATION_BUTTON)
            status_locators[ProductApplicationStatus.COMPLETED] = \
                BaseElement(self.driver, locators.VIEW_FLAGSHIP_ACCOUNT_BUTTON)
            status_locators[ProductApplicationStatus.PENDING] = \
                BaseElement(self.driver, locators.FLAGSHIP_TELL_YOUR_FRIENDS_BUTTON)
        else:
            return ProductApplicationStatus.DOES_NOT_EXIST

        # Based on product given check which, if any, status that product has
        if status_locators[ProductApplicationStatus.IN_PROGRESS].displayed():
            return ProductApplicationStatus.IN_PROGRESS
        elif status_locators[ProductApplicationStatus.PENDING].displayed():
            return ProductApplicationStatus.PENDING
        elif status_locators[ProductApplicationStatus.COMPLETED].displayed():
            return ProductApplicationStatus.COMPLETED
        else:
            return ProductApplicationStatus.DOES_NOT_EXIST

    def wait_until_debit_card_tracker_displayed(self):
        """ Wait until the Debit Card Tracker is displayed """
        self.wait_until_dashboard_displayed()
        tracker = BaseElement(self.driver, locators.DEBIT_CARD_TRACKER)
        # Sometimes the tracker doesn't display right away, added a refresh to cover this case
        if tracker.not_displayed():
            self.driver.refresh()
        tracker.wait_until_displayed()
