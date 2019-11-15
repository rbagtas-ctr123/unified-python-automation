"""Locator patterns for the Pay What Is Fair page for the Web platform."""
from selenium.webdriver.common.by import By


def pwif_amount_button(amount):
    return By.XPATH, f'//button[@value="{amount}"]'


# Pay What Is Fair
# MONTHLY_FEE_SLIDER = (By.XPATH, '//rzslider')
PWIF_NEXT_BUTTON = (By.XPATH, '//button[@title="Next"]')
PWIF_OTHER_AMOUNT = (By.XPATH, '//input[@placeholder="Other Amount"]')
