""" Locator patterns for elements on the login page of the Aspiration Android app. """
from appium.webdriver.common.mobileby import MobileBy


LOGIN_ENTRY_BUTTON = (MobileBy.ID, 'com.aspiration.app.alpha:id/tvButtonLogin')
EMAIL_INPUT = (MobileBy.ID, 'com.aspiration.app.alpha:id/email')
PASSWORD_INPUT = (MobileBy.ID, "com.aspiration.app.alpha:id/password")
LOGIN_SUBMIT_BUTTON = (MobileBy.ID, "com.aspiration.app.alpha:id/imgBtnLogin")
INVALID_CREDENTIALS_MESSAGE = (MobileBy.ID, "com.aspiration.app.alpha:id/tvEmailPasswordErrorLabel")
