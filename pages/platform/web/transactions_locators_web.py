""" Locator patterns for elements on the Transaction page of the Aspiration web app. """
from selenium.webdriver.common.by import By

# Transaction Page
TRANSACTION_NO_ACTIVITY_MESSAGE = (By.XPATH, '//div[contains(text(), "There is no activity on your account.")]')
AVAILABLE_BALANCE_TEXT = \
    (By.XPATH, '//dt[contains(text(), "Available Balance")]')
FIRST_TRANSACTION_RUNNING_BALANCE = \
    (By.XPATH, '//a[contains(@href, "?page=1&id=")][1]//div[@data-test-id="HistoryListItem-amount"]/following-sibling::div')
FIRST_TRANSACTION_LINE_ITEM = (By.XPATH, '//a[contains(@href, "?page=1&id=")][1]')
FIRST_TRANSACTION_DESCRIPTION = \
    (By.XPATH, '//a[contains(@href, "?page=1&id=")][1]//div[@data-test-id="HistoryListItem-title"]')
FIRST_TRANSACTION_AMOUNT = \
    (By.XPATH, '//a[contains(@href, "?page=1&id=")][1]//div[@data-test-id="HistoryListItem-amount"]')
TRANSACTION_MODAL_DESCRIPTION = (By.XPATH, '//*[@data-test-id="TransactionModal-title"]')
TRANSACTION_MODAL_DATE = (By.XPATH, '//*[@data-test-id="TransactionModal-title"]/following-sibling::h4')
TRANSACTION_MODAL_AMOUNT = (By.XPATH, '//*[@data-test-id="TransactionModal-title"]/following-sibling::h5')

