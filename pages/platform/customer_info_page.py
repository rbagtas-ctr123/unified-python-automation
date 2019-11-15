from abc import abstractmethod
from pages.base_pages import BasePage


class CustomerInfoPage(BasePage, is_interface=True):
    """ Interface Page Class for the Customer Info Page """

    @abstractmethod
    def submit_new_account_credentials(self, email: str, password: str):
        """ Enter an email and password then submit the credentials """

    @abstractmethod
    def submit_personal_info(self, customer_personal_info: dict):
        """ Complete and Submit the Personal Information page
        :param customer_personal_info: a dictionary with the following keys:
                first_name
                last_name
                date_of_birth
                ssn
        """

    @abstractmethod
    def submit_contact_details(self, customer_contact_details: dict):
        """ Complete and Submit the Contact Detail page
                :param customer_contact_details: a dictionary with the following keys:
                address
                city
                state
                zipcode
                phone
        """

    @abstractmethod
    def review_your_info(self):
        """ Confirm the Customer Info """

    @abstractmethod
    def wait_until_personal_info_displayed(self):
        """ Wait until the Personal Info page is displayed """


from pages.platform.android.customer_info_page_android import CustomerInfoPageAndroid
from pages.platform.ios.customer_info_page_ios import CustomerInfoPageiOS
from pages.platform.web.customer_info_page_web import CustomerInfoPageWeb
