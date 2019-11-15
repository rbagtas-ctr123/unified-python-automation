from pages.base_pages import iOSPageType
from pages.elements.base_elements import BaseElement, TextElement

from pages.platform.pwif_page import PWIFPage, PWIFAmount
import pages.platform.ios.pwif_locators_ios as locators


class PWIFPageiOS(PWIFPage, iOSPageType):
    """ Implement functions of the Web PWIFPage """

    def choose_pwif_amount(self, pwif_amount):
        """ Select a Pay What is Fair amount then submit the form """
        raise NotImplementedError

    def enter_pwif_amount(self, pwif_amount):
        """ Type a PWIF amount then submit the form"""
        raise NotImplementedError

    def select_charity(self):
        """ Select a charity """
        raise NotImplementedError
