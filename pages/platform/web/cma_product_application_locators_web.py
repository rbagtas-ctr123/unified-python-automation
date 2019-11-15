"""Locator patterns for the CMA Product Application page for the Web platform."""
from selenium.webdriver.common.by import By

# Recurring NEXT Button that appears in many of the pages in the sign up flow
NEXT_BUTTON = (By.XPATH, '//button[@type="submit"]')

# Opening Deposit
DEPOSIT_INPUT = (By.XPATH, '//div[@label="Deposit Amount"]//input')

# Recurring Deposit
RECURRING_DEPOSIT_TITLE = (By.XPATH, '//h2[text()="Recurring Deposit"]')

# Link Bank Account
BACK_TO_PAY_WHAT_IS_FAIR_LINK = (By.XPATH, '//a[contains(text(),"Back to Pay What Is Fair")]')
LINK_BANK_ACCOUNT_NEXT_BUTTON = (By.XPATH, '//div[contains(text(), "Next")]/parent::button')

# Review Your Deposit
REVIEW_YOUR_DEPOSIT_TITLE = (By.XPATH, '//h2[contains(text(),"Review Your Deposit")]')

# Submit Your Application
SUBMIT_APPLICATION_HEADER_TEXT = (By.XPATH, '//h2[contains(text(), "Submit Your Application")]')
SUBMIT_APPLICATION_BUTTON = (By.XPATH, '//button[@title="Submit Application"]')

# Attribution Survey
SURVEY_TV_OPTION = (By.XPATH, '//button[contains(text(), "TV")]')
SURVEY_RADIO_OPTION = (By.XPATH, '//button[contains(text(), "Radio")]')
SURVEY_PODCAST_OPTION = (By.XPATH, '//button[contains(text(), "Podcast")]')
SURVEY_SOCIAL_MEDIA_OPTION = (By.XPATH, '//button[contains(text(), "Social Media")]')
SURVEY_BLOG_OPTION = (By.XPATH, '//button[contains(text(), "Blog")]')
SURVEY_FRIEND_OPTION = (By.XPATH, '//button[contains(text(), "Friend")]')
SURVEY_MODAL_TITLE = (By.XPATH, '//h4[contains(text(), "Congratulations! Your account is open!")]')
SURVEY_MODAL_NEXT_STEPS_BUTTON = (By.XPATH, '//button[contains(text(), "Next Steps")]')
SURVEY_MODAL_EXIT_BUTTON = (By.XPATH, '//span[@class="close-link"]')

# Get Started
GET_STARTED_MY_DASHBOARD_BUTTON = (By.XPATH, '//header//a[contains(text(), "My Dashboard")]')

# Closing Congrats Modal for Save account
CONGRATS_SAVE_MODAL_EXIT_BUTTON = (By.XPATH, '//span[@class="close-link"]')

# Closing Referral Modal for Save account:
REFERRAL_MODAL_EXIT_BUTTON = (By.XPATH, '//a[@class="btn-close"]')

# Skip Photo Modal for Save account:
SKIP_PHOTO_MODAL_BUTTON = (By.XPATH, '//a[contains(@class,"dismiss-link")]')

# Got It Thanks Modal
GOT_IT_THANKS_MODAL_CONTINUE_BUTTON = (By.XPATH, '//button[@class="btn-v3 btn--block btn--blue"]')
