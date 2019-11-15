""" Locator patterns for elements on the dashboard page of the Aspiration Web app. """

from selenium.webdriver.common.by import By

WELCOME_MESSAGE = (By.CSS_SELECTOR, 'div.greeting > h3')
PRODUCT_BRICK = (By.CSS_SELECTOR, 'div.brick-product')
GIVING_BRICK = (By.CSS_SELECTOR, 'div.brick-giving')
PROFILE_IMAGE = (By.CSS_SELECTOR, 'div.greeting > div.profile_image')
ASPIRATION_SPEND_TITLE = (By.XPATH, '//div[contains(text(), "Aspiration Spend")]')
ASPIRATION_SPEND_BALANCE = (By.XPATH, '//div[contains(@class, "brick-account-depository") '
                            + 'and contains(.//div, "Aspiration Spend")]/'
                            + 'descendant::*/div[@class="amount ng-binding"]')
# Currently unused; for future potential tests.
ASPIRATION_SAVE_TITLE = (By.XPATH, '//div[contains(text(), "Aspiration Save")]')
ASPIRATION_SAVE_BALANCE = (By.XPATH, '//div[contains(@class, "brick-account-depository") '
                           + 'and contains(.//div, "Aspiration Save")]/'
                           + 'descendant::*/div[@class="amount ng-binding"]')
ASPIRATION_REDWOOD_BALANCE = (By.XPATH, '//div[contains(@class, "brick-account-investment") '
                              + 'and contains(.//div, "Redwood Fund")]/'
                              + 'descendant::*/div[@class="amount ng-binding"]')
VIEW_SAVE_BUTTON = (By.XPATH, '//div[contains(text(), "Aspiration Save")]/parent::*/following-sibling::button')

OTHER_PRODUCTS_BUTTON = (By.CSS_SELECTOR, 'div.brick-product > div.body > div.buttons > a.btn-v3')
WELCOME_BACK_MODAL_ADD_IMAGE_BUTTON = (By.XPATH, '//div[contains(@class, "modal-footer")]/button')
WELCOME_BACK_MODAL_SKIP_BUTTON = (By.XPATH, '//div[contains(@class, "modal-footer")]/a')
SETUP_LATER_MODAL = (By.XPATH, '//div[contains(@class, "modal-dialog")]')
SETUP_LATER_MODAL_BUTTON = (By.XPATH, '//div[contains(@class, "modal-dialog")]//button')
# Recurring Transfers Marketing Takeover
MARKETING_TAKEOVER_BACKDROP = (By.XPATH, '//div[contains(@uib-modal-backdrop, "modal-backdrop")]')
DISMISS_TAKEOVER_LINK = (By.XPATH, '//a[@ng-click="dismiss()"]')

INPROGRESS_APPLICATION_BRICK = \
    (By.XPATH, '//h4[@class="bricks-title" and contains(text(), "Applications in Progress")]')


CONTINUE_SPEND_SAVE_APPLICATION_BUTTON = (By.XPATH, '//div[text()="Spend & Save Account"]/parent::div'
                                                    '/following-sibling::button[text()="Continue Application"]')
CONTINUE_SAVE_APPLICATION_BUTTON = (By.XPATH, '//div[text()="Aspiration Save Account"]/parent::div'
                                              '/following-sibling::button[text()="Continue Application"]')
CONTINUE_REDWOOD_APPLICATION_BUTTON = (By.XPATH, '//div[contains(text()="Redwood")]/parent::div'
                                                 '/following-sibling::button[text()="Continue Application"]')
CONTINUE_FLAGSHIP_APPLICATION_BUTTON = (By.XPATH, '//div[contains(text()="Flagship")]/parent::div'
                                                  '/following-sibling::button[text()="Continue Application"]')

VIEW_SPEND_ACCOUNT_BUTTON = (By.XPATH, '//div[text()="Aspiration Spend"]/parent::div'
                                       '/following-sibling::button[text()="View Account"]')
VIEW_SAVE_ACCOUNT_BUTTON = (By.XPATH, '//div[text()="Aspiration Save"]/parent::div'
                                      '/following-sibling::button[text()="View Account"]')
VIEW_REDWOOD_ACCOUNT_BUTTON = (By.XPATH, '//div[contains(text()="Redwood")]/parent::div'
                                         '/following-sibling::button[text()="View Account"]')
VIEW_FLAGSHIP_ACCOUNT_BUTTON = (By.XPATH, '//div[contains(text()="Flagship")]/parent::div'
                                          '/following-sibling::button[text()="View Account"]')

SPEND_SAVE_TELL_YOUR_FRIENDS_BUTTON = (By.XPATH, '//div[text()="Spend & Save Account"]/parent::div'
                                                 '/following-sibling::button[text()="Tell your friends"]')
SAVE_TELL_YOUR_FRIENDS_BUTTON = (By.XPATH, '//div[text()="Aspiration Save Account"]/parent::div'
                                           '/following-sibling::button[text()="Tell your friends"]')
REDWOOD_TELL_YOUR_FRIENDS_BUTTON = (By.XPATH, '//div[contains(text()="Redwood")]/parent::div'
                                              '/following-sibling::button[text()="Tell your friends"]')
FLAGSHIP_TELL_YOUR_FRIENDS_BUTTON = (By.XPATH, '//div[contains(text()="Flagship")]/parent::div'
                                               '/following-sibling::button[text()="Tell your friends"]')
# Debit Card Tracker
DEBIT_CARD_TRACKER = (By.XPATH, '//div[@class="card-activation-container"]')
