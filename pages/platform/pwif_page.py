from abc import abstractmethod
from pages.base_pages import BasePage
from enum import Enum


class PWIFAmount(Enum):
    LOW_AMOUNT = 0.99
    MID_AMOUNT = 4.99
    HIGH_AMOUNT = 9.99


class PWIFPage(BasePage, is_interface=True):
    """ Interface Page Class for the PWIF page of the Aspiration application """

    @abstractmethod
    def choose_pwif_amount(self, pwif_amount):
        """ Select a Pay What is Fair amount then submit the form """

    @abstractmethod
    def enter_pwif_amount(self, pwif_amount):
        """ Type a PWIF amount then submit the form"""

    @abstractmethod
    def select_charity(self):
        """ Select a charity """


from pages.platform.android.pwif_page_android import PWIFPageAndroid
from pages.platform.ios.pwif_page_ios import PWIFPageiOS
from pages.platform.web.pwif_page_web import PWIFPageWeb
