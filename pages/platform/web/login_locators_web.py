""" Locator patterns for elements on the login page of the Aspiration Web app. """
from selenium.webdriver.common.by import By

EMAIL_INPUT = (By.ID, 'signinEmail')
PASSWORD_INPUT = (By.ID, 'signinPassword')
LOGIN_BUTTON = (By.CSS_SELECTOR, 'button')
ERROR_MESSAGE = (By.XPATH, '//span[@dynamic-text="error.message"]')