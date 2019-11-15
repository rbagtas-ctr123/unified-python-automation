import pages.platform.web.customer_info_locators_web as locators
from pages.platform.customer_info_page import CustomerInfoPage
from pages.base_pages import WebPageType
from pages.elements.base_elements import BaseElement, TextElement
from utilities.helpers.config_helpers import construct_a_b_test_control_url
from selenium.webdriver.common.keys import Keys


class CustomerInfoPageWeb(CustomerInfoPage, WebPageType):
    """Fills out the Personal Information and Contact Details for a new customer account"""

    def submit_new_account_credentials(self, email: str, password: str):
        """ Enter an email and password then submit the credentials """
        BaseElement(self.driver, locators.TERMS_CHECKBOX_AGREEMENT_TEXT).wait_until_displayed()
        self.driver.get(construct_a_b_test_control_url(self.driver.current_url))
        TextElement(self.driver, locators.EMAIL_INPUT).set_text(email)
        TextElement(self.driver, locators.PASSWORD_INPUT).set_text(password)
        BaseElement(self.driver, locators.TERMS_CHECKBOX_AGREEMENT_TEXT).click()
        BaseElement(self.driver, locators.TERMS_MODAL_SUBMIT_BUTTON).click()
        BaseElement(self.driver, locators.TERMS_MODAL).wait_until_not_displayed()
        BaseElement(self.driver, locators.SUBMIT_USER_CREDENTIALS_BUTTON).click()

    def submit_personal_info(self, customer_personal_info: dict):
        """ Complete and Submit the Personal Information page
        :param customer_personal_info: a dictionary that must have the following keys:
            first_name, last_name, date_of_birth, ssn
        """
        if type(customer_personal_info) is not dict:
            raise TypeError('customer_info is expected to be a dictionary object. Type given was: {}'.
                            format(type(customer_personal_info)))
        TextElement(self.driver, locators.DOB_INPUT).wait_until_displayed()
        TextElement(self.driver, locators.FIRST_NAME_INPUT).set_text(customer_personal_info['first_name'])
        TextElement(self.driver, locators.LAST_NAME_INPUT).click()
        TextElement(self.driver, locators.LAST_NAME_INPUT).set_text(customer_personal_info['last_name'])
        TextElement(self.driver, locators.DOB_INPUT).set_text(customer_personal_info['date_of_birth'])
        BaseElement(self.driver, locators.NEXT_BUTTON).click()
        BaseElement(self.driver, locators.DISABLED_NEXT_BUTTON).wait_until_displayed()
        TextElement(self.driver, locators.SSN_INPUT).set_text(customer_personal_info['ssn'])
        BaseElement(self.driver, locators.NEXT_BUTTON).click()
        TextElement(self.driver, locators.PERMANENT_ADDRESS_INPUT).wait_until_displayed()

    def submit_contact_details(self, customer_contact_details: dict):
        """ Complete and Submit the Contact Detail page
        :param customer_contact_details: a dictionary with the following keys:
            address, city, state, zipcode, phone
        """
        if type(customer_contact_details) is not dict:
            raise TypeError('customer_info is expected to be a dictionary object. Type given was: {}'.
                            format(type(customer_contact_details)))
        TextElement(self.driver, locators.PERMANENT_ADDRESS_INPUT).\
            set_text(customer_contact_details['address_line_one'])
        TextElement(self.driver, locators.PERMANENT_ADDRESS_INPUT).send_keypress(Keys.TAB)
        TextElement(self.driver, locators.PERMANENT_CITY_INPUT).set_text(customer_contact_details['city'])
        TextElement(self.driver, locators.PERMANENT_STATE_INPUT).set_text(customer_contact_details['state'])
        TextElement(self.driver, locators.PERMANENT_ZIPCODE_INPUT).set_text(customer_contact_details['zipcode'])
        TextElement(self.driver, locators.PHONE_NUMBER_INPUT).click()
        TextElement(self.driver, locators.PHONE_NUMBER_INPUT).set_text(customer_contact_details['phone_number'])
        BaseElement(self.driver, locators.CONTACT_DETAILS_NEXT_BUTTON).click()
        BaseElement(self.driver, locators.VERIFY_ADDRESS_BUTTON).click()
        BaseElement(self.driver, locators.RYI_PAGE_TITLE).wait_until_displayed()

    def review_your_info(self):
        """ Confirm the Customer Info """
        confirm_info_button = BaseElement(self.driver, locators.RYI_VERIFY_INFO_BUTTON)
        confirm_info_button.click()

    def wait_until_personal_info_displayed(self):
        """ Wait until the Personal Info page is displayed """
        TextElement(self.driver, locators.DOB_INPUT).wait_until_displayed()
