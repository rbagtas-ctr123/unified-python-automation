""" Locator patterns for elements on the dashboard page of the Aspiration Web app. """

from selenium.webdriver.common.by import By


# Sidebar Links
SPEND_PRODUCT_LINK = (By.XPATH, '//a[contains(text(), "Aspiration Spend")]')
SAVE_PRODUCT_LINK = (By.XPATH, '//a[contains(text(), "Aspiration Save")]')
REDWOOD_IRA_PRODUCT_LINK = (By.XPATH, '//a[contains(text(), "IRA - Redwood Fund (REDWX)")]')
REDWOOD_IRA_BUY_SELL_PRODUCT_OPTION_LINK = (By.XPATH, '//a[contains(text(), "Buy/Sell Redwood IRA")]')
REDWOOD_IRA_PRODUCT_LINK = (By.XPATH, '//a[contains(text(), "IRA - Redwood Fund (REDWX)")]')
REDWOOD_IRA_BUY_SELL_PRODUCT_OPTION_LINK = (By.XPATH, '//a[contains(text(), "Buy/Sell Redwood IRA")]')
REDWOOD_FUND_PRODUCT_LINK = (By.XPATH, '//a[contains(text(), "Redwood Fund (REDWX)")]')
REDWOOD_FUND_BUY_SELL_PRODUCT_LINK = (By.XPATH, '//a[contains(text(), "Buy/Sell Redwood")]')
TRANSFERS_LINK = (By.XPATH, '//a[contains(text(), "Transfers")]')
SETTINGS_LINK = (By.XPATH, '//a[@href="/settings"]')
INSURANCE_LINK = (By.XPATH, '//a[@href="https://my.alpha.aspiration.com/new/offers"]')

# QA-316 todo: Logout link locator to be updated when react is deployed to dashboard
LOGOUT_LINK = (By.XPATH, '//a[@ng-click="doAction(userLink)" and contains(text(), "Log Out")]')

# Get Started
DASHBOARD_BUTTON = (By.CSS_SELECTOR, 'a[title="Dashboard"]')
