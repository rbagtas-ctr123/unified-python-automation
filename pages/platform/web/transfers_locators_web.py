"""This file contain the collection of locators for page elements on the
transfers page of the Aspiration web app"""
from selenium.webdriver.common.by import By

# Transfers Page
SCHEDULED_TAB = (By.XPATH, '//a[contains(text(), "Scheduled")]')
HISTORY_TAB = (By.XPATH, '//a[contains(text(), "History")]')
SCHEDULED_TAB_ACTIVE = (By.XPATH, '//h2[contains(text(), "Scheduled")]')
HISTORY_TAB_ACTIVE = (By.XPATH, '//h2[contains(text(), "History")]')
TRANSFER_MONEY_BUTTON = (By.XPATH, '//a[contains(text(), "Transfer Money")]')
# BANK-1669 todo: Need locators which make it more obvious when a transfer is scheduled vs. recurring
FIRST_SCHEDULED_TRANSFER_LINK = (By.CSS_SELECTOR, 'a[href*="scheduled"]')
FIRST_SCHEDULED_TRANSFER_DATE = (By.XPATH, '//h3[not (contains(text(), "Recurring Transfers"))]')
# BANK-1683 todo: need locators to identify the to, from, and amount fields
# FIRST_SCHEDULED_TRANSFER_AMOUNT = ()
# FIRST_SCHEDULED_TRANSFER_FROM = ()
# FIRST_SCHEDULED_TRANSFER_TO = ()
FIRST_HISTORY_TRANSFER_AMOUNT = (By.XPATH, '//div[@data-test-id="HistoryListItem-amount"]')

FROM_ACCOUNT_DROP_DOWN = (By.XPATH, '//option[text()="From"]/parent::select')
TO_ACCOUNT_DROP_DOWN = (By.XPATH, '//option[text()="To"]/parent::select')
AMOUNT_INPUT = (By.XPATH, '//input[@placeholder="Enter Amount"]')
TRANSFER_DATE_INPUT = (By.XPATH, '//input[@type="date"]')
FREQUENCY_DROP_DOWN = (By.XPATH, '//span[text()="Frequency"]/parent::label//select')

# Submit Transfer
SCHEDULE_TRANSFER_BUTTON = (By.XPATH, '//button[contains(text(), "Schedule Transfer")]')
CANCEL_BUTTON = (By.XPATH, '//button[contains(text(), "Cancel")]')

# Transfer Receipt Modal
RECEIPT_CLOSE_BUTTON = (By.XPATH, '//button[@title="Close"]')
# BANK-1661 todo:  these 'sibling' locators need better locators
RECEIPT_STATUS_TEXT = (By.XPATH, '//div/h3[contains(., "transfer")]')
RECEIPT_AMOUNT_TEXT = (By.XPATH, '//span[contains(., "Transfer amount")]/following-sibling::span')
RECEIPT_DATE_TEXT = (By.XPATH, '//span[contains(., "Transfer date")]/following-sibling::span')
RECEIPT_FROM_TEXT = (By.XPATH, '//span[contains(., "From:")]/following-sibling::span')
RECEIPT_TO_TEXT = (By.XPATH, '//span[contains(., "To:")]/following-sibling::span')

SCHEDULED_CANCEL_BUTTON = (By.XPATH, '//button[contains(text(), "Cancel")]')
CONFIRM_CANCEL_BUTTON = (By.XPATH, '//button[contains(text(), "Cancel")]')

WORKING_SPINNER = (By.XPATH, '//p[@data-test-id="LoaderWithMessage-message"]')
