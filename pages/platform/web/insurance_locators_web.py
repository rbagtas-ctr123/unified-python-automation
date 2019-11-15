from selenium.webdriver.common.by import By

INSURANCE_HEADER = (By.XPATH, '//h2[text()="Insurance Choices"]')

# todo: QA-340  Add data-test-id attribute to improve stability of locator
RENTERS_INSURANCE_BUTTON = (By.XPATH, '//h3[contains(text(), "Renter")]/following-sibling::div/a')
HOMEOWNER_INSURANCE_BUTTON = (By.XPATH, '//h3[contains(text(), "Homeowner")]/following-sibling::div/a')

LEMONADE_WEBSITE_HEADER = (By.XPATH, '//div[@class="logos"]')
