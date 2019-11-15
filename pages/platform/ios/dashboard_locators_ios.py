""" Locator patterns for elements on the dashboard page of the Aspiration iOS app. """

from appium.webdriver.common.mobileby import MobileBy

PROFILE_IMAGE = (MobileBy.XPATH,
                 '//XCUIElementTypeStaticText[contains(@name, "Welcome")]/..//XCUIElementTypeOther/XCUIElementTypeImage'
                 )
WELCOME_MESSAGE = (MobileBy.XPATH, '//XCUIElementTypeStaticText[contains(@name, "Welcome")]')
ACCOUNT_SUMMARY = (MobileBy.XPATH, '//XCUIElementTypeNavigationBar[@name="Account Summary"]')
