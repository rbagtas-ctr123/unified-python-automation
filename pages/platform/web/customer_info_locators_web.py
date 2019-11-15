"""Locator patterns for the Personal Information page for the Web platform."""
from selenium.webdriver.common.by import By

# Create An Account
EMAIL_INPUT = (By.ID, 'create-an-account-email')
PASSWORD_INPUT = (By.XPATH, '//div[@label="Password"]//input[not(@id="password")]')
TERMS_CHECKBOX_AGREEMENT_TEXT = (By.XPATH, '//div[@theme="checkboxonly"]/span[2]')
TERMS_CHECKBOX = (By.XPATH, '//span[contains(text(), "I agree to the following")]/preceding-sibling::span')
TERMS_MODAL = (By.XPATH, '//h3["Client Acknowledgement"]')
TERMS_MODAL_SUBMIT_BUTTON = (By.XPATH, '//button[contains(text(), "Got it, thanks!")]')
MODAL_FADE = (By.XPATH, '//div[@class="modal-backdrop fade ng-scope ng-animate ng-leave ng-leave-active"]')
ASPIRATION_HOME_LOGO = (By.XPATH, '//span[@class="logo icon icon-logo ng-scope"]')
SOCIAL_MEDIA_LINKS = (By.XPATH, '//div[@class="social-links"]')
SUBMIT_USER_CREDENTIALS_BUTTON = (By.XPATH, '//button[@type="submit"]')

# Personal Information page
FIRST_NAME_INPUT = (By.XPATH, '//span[contains(text(), "First Name")]/preceding-sibling::input')
MIDDLE_NAME_INPUT = (By.XPATH, '//span[contains(text(), "Middle Name")]/preceding-sibling::input')
LAST_NAME_INPUT = (By.XPATH, '//span[contains(text(), "Last Name")]/preceding-sibling::input')
DOB_INPUT = (By.XPATH, '//div[@type="date"]//input')
SSN_INPUT = (By.XPATH, '//input[@placeholder="SSN"]')
CONFIRM_SSN_INPUT = (By.XPATH, '//input[@placeholder="Confirm SSN"]')
DISABLED_NEXT_BUTTON = (By.XPATH, '//button[@type="submit" and @disabled="disabled"]')
NEXT_BUTTON = (By.XPATH, '//button[@type="submit" and not(@disabled="disabled")]')
SSN_INVALID_MESSAGE = (By.XPATH, '//div[contains(@class,"alert alert-danger")]')

# Contact Detail
PERMANENT_ADDRESS_INPUT = (By.XPATH, '//input[@name="billing-address-line1"]')
PERMANENT_CITY_INPUT = (By.XPATH, '//input[@name="billing-city"]')
PERMANENT_STATE_INPUT = (By.XPATH, '//input[@data-test-id="state"]')
PERMANENT_ZIPCODE_INPUT = (By.XPATH, '//input[@name="billing-postal"]')
PHONE_NUMBER_INPUT = (By.XPATH, '//input[@name="billing-phone"]')
CONTACT_DETAILS_NEXT_BUTTON = (By.XPATH, '//button[@title="Next"]')
VERIFY_ADDRESS_BUTTON = (By.XPATH, '//span[@class="checkmark"]/parent::button')

# Review Your Info
RYI_PAGE_TITLE = (By.XPATH, '//h2[contains(text(), "Review Your Info")]')
RYI_VERIFY_INFO_BUTTON = (By.XPATH, '//button[@type="submit"]')
