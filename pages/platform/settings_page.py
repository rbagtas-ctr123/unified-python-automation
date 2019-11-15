from pages.base_pages import BasePage
from abc import abstractmethod


class SettingsPage(BasePage, is_interface=True):
    """ Interface Page Class for the SettingsPage  """

    @abstractmethod
    def wait_until_settings_displayed(self):
        """ Check whether the current page is on the Settings Page """

    @abstractmethod
    def get_pwif_amount(self):
        """  Return users current PWIF amount """


from pages.platform.android.settings_page_android import SettingsPageAndroid
from pages.platform.ios.settings_page_ios import SettingsPageiOS
from pages.platform.web.settings_page_web import SettingsPageWeb
