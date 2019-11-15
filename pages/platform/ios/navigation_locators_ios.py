"""Locator patterns for elements on the navigation page of the Aspiration iOS app."""

from appium.webdriver.common.mobileby import MobileBy

HEADER_PROFILE_IMAGE = (MobileBy.ACCESSIBILITY_ID, "navbar_profile_image")
LOGOUT_BUTTON = (MobileBy.ACCESSIBILITY_ID, "Log Out")
ALERT_YES_BUTTON = (MobileBy.ID, "com.aspiration.app.alpha:id/alert_yes_button")
SUMMARY_BUTTON = (MobileBy.ACCESSIBILITY_ID, "Summary")
MANAGE_BUTTON = (MobileBy.ACCESSIBILITY_ID, "Manage")
IMPACT_BUTTON = (MobileBy.ACCESSIBILITY_ID, "Impact")
SETTINGS_BUTTON = (MobileBy.ACCESSIBILITY_ID, "Settings")
