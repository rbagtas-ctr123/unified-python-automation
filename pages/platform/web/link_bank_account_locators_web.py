"""Locator patterns for the Plaid Page for the Web platform."""
from selenium.webdriver.common.by import By


def bank_option(bank_text):
    return By.XPATH, f"//span[contains(text(), '{bank_text}')]"


# Privacy Pane
PLAID_IFRAME = (By.XPATH, '//iframe[contains(@style, "display: block;") and contains(@id, "plaid-link-iframe")]')
PLAID_PRIVACY_HEADER = (By.XPATH, '//h2/span[contains(text(), "Aspiration uses Plaid to")]/..')
PLAID_PRIVACY_CONTINUE_BUTTON = (By.XPATH, '//button[contains(text(), "Continue")]')

# Select Bank Pane
PLAID_SELECT_BANK_HEADER = (By.XPATH, '//h1[contains(text(), "Select your bank")]')
BANK_SEARCH_INPUT = (By.XPATH, '//input[@placeholder="Search"]')

ROUTING_NUMBER_INPUT = (By.ID, "routing")
ACCOUNT_NUMBER_INPUT = (By.ID, "account")
PLAID_SUCCESS_HEADER = (By.XPATH, "//h1[contains(text(), 'Success')]")

# Login Pane
PLAID_LOGIN_HEADER = (By.XPATH, '//h1[contains(text(), "Enter your credentials")]')
PLAID_LOGIN_USER_ID_INPUT = (By.ID, 'username')
PLAID_LOGIN_PASSWORD_INPUT = (By.ID, 'password')
PLAID_LOGIN_CONTINUE_BUTTON = (By.XPATH, '//div[@id="plaid-link-container"]//button[@type="submit"]')

# Select Account Pane
PLAID_LINK_ACCOUNT_HEADER = (By.XPATH, '//h1[contains(text(), "Select your account")]')
PLAID_LINK_SAVINGS_OPTION = (By.XPATH, '//div[@class="AccountItem"]//span[contains(text(), "Plaid Saving")]/..')
PLAID_LINK_CHECKING_OPTION = (By.XPATH, '//div[@class="AccountItem"]//span[contains(text(), "Plaid Checking")]/..')
PLAID_LINK_ACCOUNT_CONTINUE_BUTTON = (By.XPATH, '//button[contains(text(), "Continue")]')
