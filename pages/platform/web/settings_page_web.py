from pages.platform.settings_page import SettingsPage
from pages.base_pages import WebPageType
import utilities.utils as utils
import pages.platform.web.settings_locators_web as locators
from pages.elements.base_elements import BaseElement


class SettingsPageWeb(SettingsPage, WebPageType):
    """ Implement functions of the Web SettingsPage """

    def wait_until_settings_displayed(self):
        """ Check whether the current page is on the Settings Page """
        BaseElement(self.driver, locators.SETTINGS_HEADER_TEXT).wait_until_displayed()
        BaseElement(self.driver, locators.FEE_SETTINGS_TAB).wait_until_displayed()

    def get_pwif_amount(self):
        """ Return users current PWIF amount """
        BaseElement(self.driver, locators.FEE_SETTINGS_TAB).click()
        fee_amount_text = BaseElement(self.driver, locators.FEE_AMOUNT)
        fee_amount_text.wait_until_displayed()
        pwif_amount = utils.decimal_from_string(fee_amount_text.get_text())
        return pwif_amount
