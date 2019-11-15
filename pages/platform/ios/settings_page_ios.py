from pages.platform.settings_page import SettingsPage
from pages.base_pages import iOSPageType
import pages.platform.ios.settings_locators_ios as locators
from pages.elements.base_elements import BaseElement


class SettingsPageiOS(SettingsPage, iOSPageType):
    """ Implement functions of the Web SettingsPage """

    def wait_until_settings_displayed(self):
        """ Check whether the current page is on the Settings Page """
        raise NotImplementedError

    def get_pwif_amount(self):
        """ Return users current PWIF amount """
        raise NotImplementedError
