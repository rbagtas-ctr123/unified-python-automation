from pages.base_pages import WebPageType
from pages.elements.base_elements import BaseElement, TextElement

from pages.platform.pwif_page import PWIFPage, PWIFAmount
import pages.platform.web.pwif_locators_web as locators


class PWIFPageWeb(PWIFPage, WebPageType):
    """ Implement functions of the Web PWIFPage """

    def choose_pwif_amount(self, pwif_amount):
        """ Select a Pay What is Fair amount then submit the form """
        if type(pwif_amount) is PWIFAmount:
            pwif_amount = pwif_amount.value
        pwif_amount_button = locators.pwif_amount_button(pwif_amount)
        BaseElement(self.driver, pwif_amount_button).click()
        BaseElement(self.driver, locators.PWIF_NEXT_BUTTON).wait_until_displayed()
        BaseElement(self.driver, locators.PWIF_NEXT_BUTTON).click()

    def enter_pwif_amount(self, pwif_amount):
        """ Type a PWIF amount then submit the form"""
        TextElement(self.driver, locators.PWIF_OTHER_AMOUNT).set_text(pwif_amount)
        BaseElement(self.driver, locators.PWIF_NEXT_BUTTON).wait_until_displayed()
        BaseElement(self.driver, locators.PWIF_NEXT_BUTTON).click()

    def select_charity(self):
        """ Select a charity """
        raise NotImplementedError
