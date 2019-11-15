""" Locator patterns for elements on the Investment Buy/Sell page of the Aspiration web app. """
from selenium.webdriver.common.by import By

BUY_SELL_HEADER = (By.XPATH, "//h2[contains(text(), 'Buy/Sell')]")
HISTORY_TAB = (By.XPATH, "//div[contains(text(), 'History')]")
SCHEDULED_TAB = (By.XPATH, "//div[contains(text(), 'Scheduled')]")
INVESTMENT_ORDER_DATE = (By.XPATH, "//h3[contains(@class, 'title')]")
INVESTMENT_ORDER_DESCRIPTION = (By.XPATH, "//span[contains(@ng-bind-html, 'txn.friendlyDescription')]")
INVESTMENT_ORDER_AMOUNT = (By.XPATH, "//div[contains(@class, 'amount')]")
INVESTMENT_ORDER_RECEIPT_MODAL_DATE = (By.XPATH, "//h4[contains(@class, 'modal-headline')]")
INVESTMENT_ORDER_RECEIPT_MODAL_DESCRIPTION = (By.XPATH, "//h4[contains(@class, 'modal-title')]")
INVESTMENT_ORDER_RECEIPT_MODAL_AMOUNT = (By.XPATH, "//td[contains(@class, 'value green')]")
INVESTMENT_ORDER_RECEIPT_MODAL_CONFIRMATION_NUMBER = \
    (By.XPATH, "//td[contains(text(), 'Confirmation Number')]/following-sibling::td[contains(@class, 'value')]")
INVESTMENT_ORDER_RECEIPT_MODAL_STATUS = (By.XPATH, "//td[contains(@class, 'name pending')]")
INVESTMENT_ORDER_RECEIPT_MODAL_CANCEL_BUTTON = (By.XPATH, "//a[contains(text(), 'Cancel')]")
INVESTMENT_ORDER_BUY_SELL_BUTTON = (By.XPATH, "//button[contains(text(), 'Buy / Sell')]")
INVESTMENT_ORDER_BUY_SELL_MODAL_FUND_TYPE = (By.XPATH, "//strong[contains(@class, 'ng-binding')]")
INVESTMENT_ORDER_BUY_SELL_MODAL_BUY_BUTTON = \
    (By.XPATH, "//button[contains(text(), 'Buy') and contains(@ng-class, 'option')]")
INVESTMENT_ORDER_BUY_SELL_MODAL_HEADER = (By.XPATH, "//h3[contains(text(), 'Create an Order')]")
INVESTMENT_ORDER_BUY_SELL_MODAL_SELL_BUTTON = \
    (By.XPATH, "//button[contains(text(), 'Sell') and contains(@ng-class, 'option')]")
INVESTMENT_ORDER_BUY_SELL_MODAL_BANK_NAME = (By.XPATH, "//div[contains(@class, 'property-field')]")
INVESTMENT_ORDER_BUY_MODAL_AMOUNT = (By.XPATH, "//input[contains(@placeholder, 'Amount')]")
INVESTMENT_ORDER_BUY_SELL_MODAL_PLACE_ORDER_BUTTON = \
    (By.XPATH, "//button[contains(text(), 'Go to Aspiration Funds and Place My Order')]")
INVESTMENT_ORDER_BUY_SELL_MODAL_CANCEL_BUTTON = (By.XPATH, "//a[contains(text(), 'Cancel this order')]")
INVESTMENT_ORDER_SCHEDULED_IS_EMPTY = \
    (By.XPATH, "//span[contains(text(), 'You don’t have any upcoming scheduled orders.')]")

# This is new page that confirms you are placing an order. It is part of the investment buy/sell flow
INVESTMENT_PLACE_ORDER_AMOUNT = (By.XPATH, "//p[contains(text(), 'You are buying')]/span[1]")
INVESTMENT_PLACE_ORDER_FUND_SYMBOL = (By.XPATH, "//p[contains(text(), 'You are buying')]/span[2]")
INVESTMENT_PLACE_ORDER_FUND_NAME = (By.XPATH, "//p[contains(text(), 'You are buying')]/span[3]")
INVESTMENT_PLACE_ORDER_FUND_YEAR = (By.XPATH, "//p[contains(text(), 'You are buying')]/b")
INVESTMENT_PLACE_ORDER_AMOUNT_CONFIRMATION = (By.XPATH, "//p[contains(text(), 'will be debited from your')]/span[1]")
INVESTMENT_PLACE_ORDER_ORIGIN_BANK = (By.XPATH, "//p[contains(text(), 'will be debited from your')]/span[2]")
INVESTMENT_PLACE_ORDER_PROCEED_BUTTON = \
    (By.XPATH, "//div[contains(text(), 'Place my order and return to the Aspiration Financial website.')]")
INVESTMENT_PLACE_ORDER_CANCEL_BUTTON = (By.XPATH, "//a[contains(text(), 'Cancel')]")

# This is an order confirmation page, which is still logically part of buying or selling an order
INVESTMENT_CONFIRMATION_HEADER = (By.XPATH, "//h2[contains(text(), 'Order Confirmation')]")
INVESTMENT_CONFIRMATION_ACTION = (By.XPATH, "//td[contains(text(), 'Action')]/following-sibling::td")
INVESTMENT_CONFIRMATION_SYMBOL = (By.XPATH, "//td[contains(text(), 'Symbol')]/following-sibling::td")
INVESTMENT_CONFIRMATION_DESCRIPTION = (By.XPATH, "//td[contains(text(), 'Description')]/following-sibling::td")
INVESTMENT_CONFIRMATION_PAYMENT_METHOD = (By.XPATH, "//td[contains(text(), 'Payment Method')]/following-sibling::td")
INVESTMENT_CONFIRMATION_PAYMENT_AMOUNT = (By.XPATH, "//td[contains(text(), 'Amount')]/following-sibling::td")
INVESTMENT_CONFIRMATION_PAYMENT_TRADE_DATE = (By.XPATH, "//td[contains(text(), 'Trade Date')]/following-sibling::td")
INVESTMENT_CONFIRMATION_PAYMENT_TRADE_YEAR = \
    (By.XPATH, "//td[contains(text(), 'Year of contribution')]/following-sibling::td")
INVESTMENT_CONFIRMATION_NUMBER = (By.XPATH, "//p[contains(text(), 'Order confirmation number')]/b")
INVESTMENT_ORDER_GO_TO_STATUS = (By.XPATH, "//button[contains(text(), 'Go to Order Status')]")

# This page shows the order status again before directing a user back to the buy/sell page
INVESTMENT_CANCEL_ORDER_AMOUNT = (By.XPATH, "//p[contains(text(), 'Buy')]/b[1]")
INVESTMENT_CANCEL_ORDER_SYMBOL = (By.XPATH, "//p[contains(text(), 'Buy')]/b[2]")
INVESTMENT_CANCEL_ORDER_FUND = (By.XPATH, "//p[contains(text(), 'Buy')]/b[3]")
INVESTMENT_CANCEL_ORDER_BUTTON = \
    (By.XPATH, "//div[contains(text(), 'Cancel my order and return to the Aspiration Financial website.')]")
