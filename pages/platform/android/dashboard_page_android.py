""" Implement functions of the Android Dashboard Page """

import pages.platform.android.dashboard_locators_android as locators
from pages.elements.base_elements import BaseElement
from pages.platform.dashboard_page import DashboardPage
from pages.base_pages import AndroidPageType
from decimal import Decimal as Decimal
import re


class DashboardPageAndroid(DashboardPage, AndroidPageType):
    """ Implement functions of the Web Dashboard Page """

    def wait_until_dashboard_displayed(self):
        """ Wait until the dashboard page is displayed
            Because the emulator is slow logging in, we must allow a longer wait time
        """
        BaseElement(self.driver, locators.PROFILE_IMAGE).wait_until_displayed(20)
        BaseElement(self.driver, locators.WELCOME_MESSAGE).wait_until_displayed(20)
        BaseElement(self.driver, locators.PRODUCT_BRICK).wait_until_displayed(20)

    def get_product_balance(self, product):
        """ Return the displayed balance of a user's chosen product """
        raise NotImplementedError

    def get_spend_balance(self):
        """ Return the displayed balance of the user's Aspiration Spend Account """
        BaseElement(self.driver, locators.SPEND_ACCOUNT_TEXT).wait_until_displayed()
        # Manually scrolling up is necessary because even seeing the label might still hide amount
        self.touch_scroll_up()
        element = BaseElement(self.driver, locators.SPEND_BALANCE_TEXT)
        return Decimal(re.sub(r'[^\d.]', '', element.get_text()))

    def get_save_balance(self):
        """ Return the displayed balance of the user's Aspiration Save Account """
        BaseElement(self.driver, locators.SAVE_ACCOUNT_TEXT).wait_until_displayed()
        # Manually scrolling up is necessary because even seeing the label might still hide amount
        self.touch_scroll_up()
        element = BaseElement(self.driver, locators.SAVE_BALANCE_TEXT)
        return Decimal(re.sub(r'[^\d.]', '', element.get_text()))

    def get_product_status(self, product):
        """ Return the status of the supplied product """
        raise NotImplementedError

    def continue_product_application(self, product):
        """ Continue a Product Application """
        raise NotImplementedError
