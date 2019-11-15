""" Constants representing Web locators for elements on the dashboard page """

from selenium.webdriver.common.by import By

DASHBOARD_HEADER = (By.CSS_SELECTOR, '.page-header')
DASHBOARD_FRAME = (By.CSS_SELECTOR, 'iframe[title=dashboard]')
