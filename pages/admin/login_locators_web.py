""" Constants representing Web locators for elements on the login page """

from selenium.webdriver.common.by import By

ADMIN_ICON = (By.CSS_SELECTOR, '.admin-icon')
GOOGLE_SIGN_IN_BUTTON = (By.CSS_SELECTOR, '.google-icon')
GOOGLE_EMAIL_OR_PHONE_INPUT = (By.CSS_SELECTOR, 'input[aria-label="Email or phone"]')
GOOGLE_SIGN_IN_NEXT_BUTTON = (By.ID, 'identifierNext')
GOOGLE_ACCOUNT_VERIFICATION_TEXT = (By.XPATH, '//content[contains (text(), "Verify it\'s you")]')
# The only unique path to this button traverses, the html is from google's site, not our own
GOOGLE_ACCOUNT_CONTINUE_BUTTON = (By.XPATH,
                                  '//*[contains (@role, "button")]/descendant::*[contains (text(), "Continue")]')
OKTA_USERNAME_INPUT = (By.ID, 'okta-signin-username')
OKTA_PASSWORD_INPUT = (By.ID, 'okta-signin-password')
OKTA_SIGN_IN_BUTTON = (By.ID, 'okta-signin-submit')
