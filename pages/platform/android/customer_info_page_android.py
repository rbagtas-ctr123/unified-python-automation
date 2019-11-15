import pages.platform.android.customer_info_locators_android as locators
from pages.platform.customer_info_page import CustomerInfoPage
from pages.base_pages import AndroidPageType


class CustomerInfoPageAndroid(CustomerInfoPage, AndroidPageType):
    """Fills out the Personal Information and Contact Details for a new customer account"""

    def submit_new_account_credentials(self, email: str, password: str):
        """ Enter an email and password then submit the credentials """
        raise NotImplementedError

    def submit_personal_info(self, customer_personal_info: dict):
        """ Complete and Submit the Personal Information page
        :param customer_personal_info: a dictionary that must have the following keys:
            first_name, last_name, date_of_birth, ssn
        """
        raise NotImplementedError

    def submit_contact_details(self, customer_contact_details: dict):
        """ Complete and Submit the Contact Detail page
        :param customer_contact_details: a dictionary with the following keys:
            address, city, state, zipcode, phone
        """
        raise NotImplementedError

    def review_your_info(self):
        """ Confirm the Customer Info """
        raise NotImplementedError

    def wait_until_personal_info_displayed(self):
        """ Wait until the Personal Info page is displayed """
        raise NotImplementedError
