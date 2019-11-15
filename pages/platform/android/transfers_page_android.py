""" Implement functions of the Android TransfersPage """

from pages.platform.transfers_page import TransfersPage, TransferStatus
from pages.elements.base_elements import AndroidBaseElement as BaseElement, AndroidTextElement as TextElement
from pages.base_pages import AndroidPageType
import pages.platform.android.transfers_locators_android as locators
import utilities.utils as utils
from utilities.utils import future_business_day


class TransfersPageAndroid(TransfersPage, AndroidPageType):
    """ Implement functions of the Android TransfersPage """

    def wait_until_transfers_displayed(self):
        """ Check  whether the current page is the transfers page
            Dismiss any First-Visit tutorial hints
        """
        BaseElement(self.driver, locators.HISTORY_TAB).wait_until_displayed()
        BaseElement(self.driver, locators.SCHEDULED_TAB).wait_until_displayed()
        first_time_alert = BaseElement(self.driver, locators.FIRST_TIME_ALERT_TEXT)
        if first_time_alert.displayed(0.5):
            BaseElement(self.driver, locators.FIRST_TIME_ALERT_TEXT).click()
            first_time_alert.wait_until_not_displayed()

    def show_scheduled_transfers(self):
        """ Show scheduled transfers """
        scheduled_tab = BaseElement(self.driver, locators.SCHEDULED_TAB)
        scheduled_tab.click()
        scheduled_tab.wait_until_selected()

    def open_next_scheduled_transfer(self):
        """ Preview the next scheduled transfer """
        BaseElement(self.driver, locators.SCHEDULED_TRANSFER_TO).click()
        BaseElement(self.driver, locators.RECEIPT_STATUS_TEXT).wait_until_displayed()

    def transfer_preview_details(self):
        """ return the results of a previewed transfer """
        transfer_preview_details = dict()
        status = BaseElement(self.driver, locators.RECEIPT_STATUS_TEXT).get_text()
        if "completed" in status:
            transfer_preview_details["status"] = TransferStatus.COMPLETED
        if "not yet begun" in status:
            transfer_preview_details["status"] = TransferStatus.SCHEDULED
        amount = BaseElement(self.driver, locators.RECEIPT_AMOUNT_TEXT).get_text()
        transfer_preview_details["amount"] = utils.decimal_from_string(amount)
        transfer_preview_details["from"] = BaseElement(self.driver, locators.RECEIPT_FROM_TEXT).get_text()
        transfer_preview_details["to"] = BaseElement(self.driver, locators.RECEIPT_TO_TEXT).get_text()
        transfer_preview_details["date"] = BaseElement(self.driver, locators.RECEIPT_DATE_TEXT).get_text()
        transfer_preview_details["confirmation"] = BaseElement(self.driver,
                                                               locators.RECEIPT_CONFIRMATION_TEXT).get_text()
        return transfer_preview_details

    def close_previewed_transfer(self):
        """ close the previewed transfer """
        close_confirmation_button = BaseElement(self.driver, locators.RECEIPT_CLOSE_BUTTON)
        close_confirmation_button.click()
        BaseElement(self.driver, locators.RECEIPT_STATUS_TEXT).wait_until_not_displayed()
        BaseElement(self.driver, locators.SCHEDULED_TAB).wait_until_displayed()
        self.wait_until_transfers_displayed()

    def cancel_previewed_transfer(self):
        """ cancel the previewed transfer """
        BaseElement(self.driver, locators.RECEIPT_CANCEL_BUTTON).click()
        BaseElement(self.driver, locators.ALERT_YES_BUTTON).click()
        BaseElement(self.driver, locators.RECEIPT_STATUS_TEXT).wait_until_not_displayed()
        self.wait_until_transfers_displayed()

    def cancel_all_scheduled_transfers(self):
        """ Cancel all scheduled transfers """
        self.show_scheduled_transfers()
        while BaseElement(self.driver, locators.SCHEDULED_TRANSFER_DATE).displayed(3):
            self.open_next_scheduled_transfer()
            self.cancel_previewed_transfer()

    def prepare_transfer(self, transfer_amount, from_account, to_account):
        """ Prepare a funds transfer with the specified details and advance to the scheduling step """
        BaseElement(self.driver, locators.INITIATE_TRANSFER_BUTTON).click()

        # Determine which aspiration account to use
        if to_account == TransfersPage.SPEND_ACCOUNT:
            BaseElement(self.driver, locators.CHOOSE_SPEND_BUTTON).click()
            withdraw = False
        elif to_account == TransfersPage.SAVE_ACCOUNT:
            BaseElement(self.driver, locators.CHOOSE_SAVE_BUTTON).click()
            withdraw = False
        elif from_account == TransfersPage.SPEND_ACCOUNT:
            BaseElement(self.driver, locators.CHOOSE_SPEND_BUTTON).click()
            withdraw = True
        elif from_account == TransfersPage.SAVE_ACCOUNT:
            BaseElement(self.driver, locators.CHOOSE_SAVE_BUTTON).click()
            withdraw = True
        else:
            raise ValueError(f"At least one of the accounts for a transfer must be one of: Save, Spend")

        # Dynamically generate account locator
        if withdraw:
            BaseElement(self.driver, locators.WITHDRAWAL_OUT_BUTTON).click()
            second_account_locator = BaseElement(self.driver, locators.account_picker(to_account))
        else:
            second_account_locator = BaseElement(self.driver, locators.account_picker(from_account))

        # Choose the 2nd bank
        BaseElement(self.driver, locators.CHOOSE_BANK_INPUT).click()
        second_account_locator.click()
        # Input amount in a way which activates the "Next Step" button
        amount = TextElement(self.driver, locators.AMOUNT_INPUT)
        amount.click()
        amount.set_text(str(transfer_amount))
        self.driver.execute_script("mobile: performEditorAction", {'action': 'done'})
        BaseElement(self.driver, locators.NEXT_STEP_BUTTON).click()
        # Ensure we've advanced to the scheduling activity
        BaseElement(self.driver, locators.PREVIEW_BUTTON).wait_until_displayed()

    def schedule_transfer(self, days_in_future=0):
        """ Schedule a prepared transfer
            days_in_future is the minimum days in the future to attempt to schedule transfer
        """
        if days_in_future > 0:
            BaseElement(self.driver, locators.SPECIFIC_DATE_BUTTON).click()
            transfer_date = future_business_day(days_in_future)
            month_year = transfer_date.strftime('%B') + ' ' + str(transfer_date.year)
            day = str(transfer_date.day)
            BaseElement(self.driver, locators.SELECT_DATE_BUTTON).click()
            month_heading = BaseElement(self.driver, locators.MONTH_YEAR_TEXT)
            next_month_button = BaseElement(self.driver, locators.NEXT_MONTH_BUTTON)
            # Click "Next Month" until the desired month / year is displayed, or we reach the end of the calendar
            while (month_heading.get_text() != month_year) and month_heading.displayed():
                next_month_button.click()
            if month_heading.get_text() != month_year:
                raise ValueError('Could not find "' + month_year + '" in calendar widget')
            # Dynamically generate the date locator
            BaseElement(self.driver, locators.date_button(day)).click()
            BaseElement(self.driver, locators.CHOOSE_DATE_BUTTON).click()
            month_heading.wait_until_not_displayed()
        BaseElement(self.driver, locators.PREVIEW_BUTTON).click()
        BaseElement(self.driver, locators.SCHEDULE_TRANSFER_BUTTON).wait_until_displayed()

    def submit_transfer_request(self):
        """ Submit a prepared and scheduled transfer request """
        BaseElement(self.driver, locators.SCHEDULE_TRANSFER_BUTTON).click()
        BaseElement(self.driver, locators.RECEIPT_STATUS_TEXT).wait_until_displayed()

    def transfer_request_result(self):
        """ return the results of a just submitted transfer request """
        return self.transfer_preview_details()

    def dismiss_transfer_result(self):
        """ Dismiss the results displayed after a transfer is scheduled or performed """
        self.close_previewed_transfer()

    def next_scheduled_transfer_summary(self):
        """ Return summarized details of next scheduled transfer, or None if no transfer is scheduled """
        next_transfer = BaseElement(self.driver, locators.SCHEDULED_TRANSFER_DATE)
        if next_transfer.displayed(5):
            transfer_details = {'date': BaseElement(self.driver, locators.SCHEDULED_TRANSFER_DATE).get_text()}
        else:
            return None
        transfer_details['amount'] = utils.decimal_from_string(BaseElement(self.driver,
                                                               locators.SCHEDULED_TRANSFER_AMOUNT).get_text())
        from_text = BaseElement(self.driver, locators.SCHEDULED_TRANSFER_FROM).get_text()
        to_text = BaseElement(self.driver, locators.SCHEDULED_TRANSFER_TO).get_text()
        transfer_details['to'] = to_text.replace('Deposit into ', '')
        transfer_details['from'] = from_text.replace('From ', '')
        return transfer_details
