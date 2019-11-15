""" Locator patterns for elements on the Transfers page of the Aspiration Android app. """

from appium.webdriver.common.mobileby import MobileBy

# Transfers Activity
FIRST_TIME_ALERT_TEXT = (MobileBy.ID, 'com.aspiration.app.alpha:id/transferFirstTimeInfoText')
GOT_IT_TEXT = (MobileBy.ID, 'com.aspiration.app.alpha:id/transferFirstTimeGotItLabel')
INITIATE_TRANSFER_BUTTON = (MobileBy.ID, 'com.aspiration.app.alpha:id/fabAccountTransfers')
HISTORY_TAB = (MobileBy.ACCESSIBILITY_ID, 'History')
SCHEDULED_TAB = (MobileBy.ACCESSIBILITY_ID, 'Scheduled')

# Scheduled transfers tab
SCHEDULED_TRANSFER_DATE = (MobileBy.ID, 'com.aspiration.app.alpha:id/tvDateHeader')
SCHEDULED_TRANSFER_FROM = (MobileBy.ID, 'com.aspiration.app.alpha:id/tvTransactionStatus')
SCHEDULED_TRANSFER_TO = (MobileBy.ID, 'com.aspiration.app.alpha:id/tvTransactionDescription')
SCHEDULED_TRANSFER_AMOUNT = (MobileBy.ID, 'com.aspiration.app.alpha:id/tvTransactionAmount')

# Transfer receipt
RECEIPT_CLOSE_BUTTON = (MobileBy.ID, 'com.aspiration.app.alpha:id/receiptClose')
RECEIPT_STATUS_TEXT = (MobileBy.ID, 'com.aspiration.app.alpha:id/receiptHeader')
RECEIPT_AMOUNT_TEXT = (MobileBy.ID, 'com.aspiration.app.alpha:id/receiptAmount')
RECEIPT_DATE_TEXT = (MobileBy.ID, 'com.aspiration.app.alpha:id/receiptDate')
RECEIPT_FROM_TEXT = (MobileBy.ID, 'com.aspiration.app.alpha:id/receiptFrom')
RECEIPT_TO_TEXT = (MobileBy.ID, 'com.aspiration.app.alpha:id/receiptTo')
RECEIPT_CONFIRMATION_TEXT = (MobileBy.ID, 'com.aspiration.app.alpha:id/receiptConfirmation')
RECEIPT_CANCEL_BUTTON = (MobileBy.ID, 'com.aspiration.app.alpha:id/receiptTransferCancel')
ALERT_YES_BUTTON = (MobileBy.ID, 'com.aspiration.app.alpha:id/alert_yes_button')
ALERT_NO_BUTTON = (MobileBy.ID, 'com.aspiration.app.alpha:id/alert_no_button')

# choose banking product modal
CHOOSE_SPEND_BUTTON = (MobileBy.ID, 'com.aspiration.app.alpha:id/chooseProductSpendContainer')
CHOOSE_SAVE_BUTTON = (MobileBy.ID, 'com.aspiration.app.alpha:id/chooseProductSaveContainer')
CHOOSE_CANCEL_BUTTON = (MobileBy.ID, 'com.aspiration.app.alpha:id/chooseProductCancelButton')

# Transfer money screen
NEXT_STEP_BUTTON = (MobileBy.ID, 'com.aspiration.app.alpha:id/nextStep')
DEPOSIT_INTO_BUTTON = (MobileBy.ID, 'com.aspiration.app.alpha:id/transfer_into_radio_button')
WITHDRAWAL_OUT_BUTTON = (MobileBy.ID, 'com.aspiration.app.alpha:id/transfer_out_radio_button')
CHOOSE_BANK_INPUT = (MobileBy.ID, 'com.aspiration.app.alpha:id/account_edit_text')
def account_picker(account_name):
    return MobileBy.ANDROID_UIAUTOMATOR, f'new UiSelector().textContains("{account_name}")'
AMOUNT_INPUT = (MobileBy.ID, 'com.aspiration.app.alpha:id/transfer_amount_edit_text')
CANCEL_PICKER_BUTTON = (MobileBy.ID, 'com.aspiration.app.alpha:id/account_picker_cancel_button')

# Schedule Transfer
PREVIEW_BUTTON = (MobileBy.ID, 'com.aspiration.app.alpha:id/previewScheduledTransfer')
NEAREST_DATE_BUTTON = (MobileBy.ID, 'com.aspiration.app.alpha:id/com.aspiration.app.alpha:id/rbTransferNearestDate')
SPECIFIC_DATE_BUTTON = (MobileBy.ID, 'com.aspiration.app.alpha:id/rbTransferSpecificDate')
SELECT_DATE_BUTTON = (MobileBy.ID, 'com.aspiration.app.alpha:id/editTextDate')

# Pick Day
MONTH_YEAR_TEXT = (MobileBy.ID, 'com.aspiration.app.alpha:id/calendar_date_display')
NEXT_MONTH_BUTTON = (MobileBy.ID, 'com.aspiration.app.alpha:id/calendar_next_button')
PREVIOUS_MONTH_BUTTON = (MobileBy.ID, 'com.aspiration.app.alpha:id/calendar_prev_button')
def date_button(date): return MobileBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{date}")'
CHOOSE_DATE_BUTTON = (MobileBy.ID, 'com.aspiration.app.alpha:id/calendar_picker_choose_button')
CANCEL_CALENDAR_BUTTON = (MobileBy.ID, 'com.aspiration.app.alpha:id/calendar_picker_cancel_button')
HOLIDAY_TEXT = (MobileBy.ID, 'com.aspiration.app.alpha:id/tvHolidayDescription')

# Preview Transfers
SCHEDULE_TRANSFER_BUTTON = (MobileBy.ID, 'com.aspiration.app.alpha:id/schedule_transfer_button')
