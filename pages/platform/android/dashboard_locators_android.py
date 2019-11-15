""" Locator patterns for elements on the dashboard page of the Aspiration Android app. """

from appium.webdriver.common.mobileby import MobileBy

PROFILE_IMAGE = (MobileBy.ID, 'com.aspiration.app.alpha:id/imgProfileAvatarAccountSnapshot')
WELCOME_MESSAGE = (MobileBy.ID, 'com.aspiration.app.alpha:id/tvWelcomeBackAccountSnapshot')

# Product Info
PRODUCT_BRICK = (MobileBy.ID, 'com.aspiration.app.alpha:id/accountProductsRecyclerView')
SPEND_ACCOUNT_TEXT = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().resourceId'
                                                    '("com.aspiration.app.alpha:id/accountProductsRecyclerView")).'
                                                    'scrollIntoView(new UiSelector().resourceId'
                                                    '("com.aspiration.app.alpha:id/product_row").fromParent'
                                                    '(new UiSelector().resourceId'
                                                    '("com.aspiration.app.alpha:id/product_name").text'
                                                    '("Aspiration Spend")))')
SPEND_BALANCE_TEXT = (MobileBy.XPATH, '//android.widget.TextView[@text="Aspiration Spend"]/parent::*/'
                                      'parent::*/android.widget.RelativeLayout/android.widget.TextView')
SAVE_ACCOUNT_TEXT = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().resourceId'
                                                   '("com.aspiration.app.alpha:id/accountProductsRecyclerView")).'
                                                   'scrollIntoView(new UiSelector().resourceId'
                                                   '("com.aspiration.app.alpha:id/product_row").fromParent'
                                                   '(new UiSelector().resourceId'
                                                   '("com.aspiration.app.alpha:id/product_name").text'
                                                   '("Aspiration Save")))')
SAVE_BALANCE_TEXT = (MobileBy.XPATH, '//android.widget.TextView[@text="Aspiration Save"]/parent::*/'
                                     'parent::*/android.widget.RelativeLayout/android.widget.TextView')
