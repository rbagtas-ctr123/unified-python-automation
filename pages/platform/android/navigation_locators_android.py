"""Locator patterns for elements on the navigation page of the Aspiration Android app."""

from appium.webdriver.common.mobileby import MobileBy


DRAWER_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Open navigation drawer')
NAVIGATE_UP_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Navigate up')
LOCATION_TEXT = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceIdMatches(\"com.aspiration.app.alpha:'
                                               'id/toolbar.*\").childSelector(new UiSelector().'
                                               'className(\"android.widget.TextView\"))')

# Drawer Items
SUMMARY_BUTTON = (MobileBy.ID, "com.aspiration.app.alpha:id/viewMenuItemSummary")
MANAGE_BUTTON = (MobileBy.ID, "com.aspiration.app.alpha:id/viewMenuItemManage")
IMPACT_BUTTON = (MobileBy.ID, "com.aspiration.app.alpha:id/viewMenuItemImpact")
VIEW_SETTINGS_BUTTON = (MobileBy.ID, "com.aspiration.app.alpha:id/viewMenuItemSettings")
# Settings
USERNAME_TEXT = (MobileBy.ID, "com.aspiration.app.alpha:id/tvSettingsUserName")
FEEDBACK_LABEL = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches(\"FEEDBACK & SUPPORT\")')
LOGOUT_BUTTON = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().resourceId('
                                               '\"com.aspiration.app.alpha:id/scrollViewSettings\")).'
                                               'scrollIntoView(new UiSelector().'
                                               'resourceId(\"com.aspiration.app.alpha:id/btnSettingsLogout\"))')
# Manage Items
CHECK_DEPOSITS_BUTTON = (MobileBy.ID, "com.aspiration.app.alpha:id/containercheckDeposits")
TRANSFERS_BUTTON = (MobileBy.ID, "com.aspiration.app.alpha:id/containerTransfers")
PAYMENTS_BUTTON = (MobileBy.ID, "com.aspiration.app.alpha:id/containerPayments")
# Alert Modal
ALERT_YES_BUTTON = (MobileBy.ID, "com.aspiration.app.alpha:id/alert_yes_button")
