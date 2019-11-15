""" Locator patterns for elements on the login page of the Aspiration iOS app. """

from appium.webdriver.common.mobileby import MobileBy


LOGIN_ENTRY_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Log In')
EMAIL_INPUT = (MobileBy.ACCESSIBILITY_ID, 'Email address field')
PASSWORD_INPUT = (MobileBy.ACCESSIBILITY_ID, 'Password field')
INVALID_CREDENTIALS_MESSAGE = None
