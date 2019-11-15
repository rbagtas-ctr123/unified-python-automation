from pages.base_pages import AndroidPageType
from pages.elements.base_elements import BaseElement, TextElement
from pages.platform.pwif_page import PWIFPage, PWIFAmount
import pages.platform.android.pwif_locators_android as locators


class PWIFPageAndroid(PWIFPage, AndroidPageType):
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
