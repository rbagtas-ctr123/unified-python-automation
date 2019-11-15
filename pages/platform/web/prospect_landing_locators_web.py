"""Locator patterns for the Prospect Landing page for the Web platform."""
from selenium.webdriver.common.by import By


# Get Started modal
GET_STARTED_EMAIL_INPUT = (By.XPATH, '//form//input[@type="email"]')
GET_STARTED_BUTTON = (By.XPATH, '//form//button')

# Get Started Home Header Button
HEADER_GET_STARTED_BUTTON = (By.XPATH, '//a[text()="Sign In"]//following-sibling::button')

# Get Started Body Button
GET_STARTED_HOME_BODY_BUTTON = (By.XPATH, '//div[@class="bottom-container"]//a[@class="btn-v3 btn-success"]'
                                          '[contains(text(),"Get Started")]')

# /get-account LOCATORS

# Get Started /get-account,/get-account-100 and /get-account-pride Body Button
GET_STARTED_GET_ACCOUNT_TOP_BODY_BUTTON = \
    (By.XPATH, '//div[@class="cta__QsPA2"]//button[contains(@class,"button__3hWCX")][contains(text(),"Get Started")]')
GET_STARTED_GET_ACCOUNT_MID_BODY_BUTTON = (By.XPATH, '//button[contains(text(),"Start with $10")]')
GET_STARTED_GET_ACCOUNT_BOTTOM_BODY_BUTTON = \
    (By.XPATH, '//div[@class="cta__2UMqJ"]//button[@class="button__3hWCX"][contains(text(),"Get Started")]')
GET_STARTED_ENTER_EMAIL_TOP_BODY_FIELD = \
    (By.XPATH, '//div[@class="cta__QsPA2"]//input[@placeholder="Enter Email Address"]')

# /get-account-100 LOCATORS
GET_STARTED_LOCATORS = (By.XPATH, '//button[@type="submit"]')

# /get-account-teslap2019
GET_STARTED_TESLA_ENTER_EMAIL_FIELD = \
    (By.XPATH, '//div[@class="teslaCta__q3LTQ"]//input[@placeholder="Enter Email Address"]')
GET_STARTED_TESLA_BUTTON = (By.XPATH, '//button[@class="button__3hWCX teslaPromoButton__22_QY"]')

# /save
GET_STARTED_SAVE_ENTER_EMAIL_FIELD = (By.XPATH, '//div[@class="cta__1YtaZ"]//input[@placeholder="Enter Email Address"]')
GET_STARTED_SAVE_BUTTON = (By.XPATH, '//button[@class="button__3hWCX customButton__3kPFA"]')
