from selenium.webdriver.common.by import By

FEE_SETTINGS_TAB = (By.XPATH, '//a[@href="/settings/pwif/settings"]')
FEE_AMOUNT = (By.XPATH, '//td[contains(text(),"Fee Amount")]/following-sibling::td')
SETTINGS_HEADER_TEXT = (By.XPATH, '//h2[contains(@class, "settings-title") and text()="Settings"]')
