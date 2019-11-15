""" Implement functions of the Web TransfersPage """

from pages.elements.base_elements import BaseElement, TextElement
from pages.elements.custom_elements import CalendarDatePicker
import utilities.utils as utils
import pages.platform.web.transfers_locators_web as locators
from pages.platform.transfers_page import TransfersPage, TransferStatus
from pages.base_pages import WebPageType


class TransfersPageWeb(TransfersPage, WebPageType):
    """ Implement functions of the Web TransfersPage """

    def wait_until_transfers_displayed(self):
        """ Check  whether the current page is the transfers page
            Dismiss any 'First-Visit' tutorial hints
        """
        BaseElement(self.driver, locators.TRANSFER_MONEY_BUTTON).wait_until_displayed()

    def show_scheduled_transfers(self):
        """ Show scheduled transfers """
        if BaseElement(self.driver, locators.SCHEDULED_TAB_ACTIVE).not_displayed():
            BaseElement(self.driver, locators.SCHEDULED_TAB).click()
            BaseElement(self.driver, locators.SCHEDULED_TAB_ACTIVE).wait_until_displayed()

    def open_next_scheduled_transfer(self):
        """ Preview the next scheduled transfer """
        top_transfer = BaseElement(self.driver, locators.FIRST_SCHEDULED_TRANSFER_LINK)
        top_transfer.click()
        BaseElement(self.driver, locators.RECEIPT_STATUS_TEXT).wait_until_displayed()

    def transfer_preview_details(self):
        """ return the results of a previewed transfer """
        transfer_preview_details = dict()
        status = BaseElement(self.driver, locators.RECEIPT_STATUS_TEXT).get_text()
        if "completed" in status:
            transfer_preview_details["status"] = TransferStatus.COMPLETED
        elif "scheduled" in status:
            transfer_preview_details["status"] = TransferStatus.SCHEDULED
        amount = BaseElement(self.driver, locators.RECEIPT_AMOUNT_TEXT).get_text()
        transfer_preview_details["amount"] = utils.decimal_from_string(amount)
        transfer_preview_details["from"] = BaseElement(self.driver, locators.RECEIPT_FROM_TEXT).get_text()
        transfer_preview_details["to"] = BaseElement(self.driver, locators.RECEIPT_TO_TEXT).get_text()
        return transfer_preview_details

    def close_previewed_transfer(self):
        """ Close transfer preview """
        close_confirmation_button = BaseElement(self.driver, locators.RECEIPT_CLOSE_BUTTON)
        close_confirmation_button.click()
        BaseElement(self.driver, locators.RECEIPT_STATUS_TEXT).wait_until_not_displayed()

    def cancel_previewed_transfer(self):
        """ Cancel transfer preview """
        BaseElement(self.driver, locators.SCHEDULED_CANCEL_BUTTON).click()
        confirm_cancel_button = BaseElement(self.driver, locators.CONFIRM_CANCEL_BUTTON)
        confirm_cancel_button.click()
        confirm_cancel_button.wait_until_not_displayed()
        BaseElement(self.driver, locators.WORKING_SPINNER).wait_until_not_displayed()

    def cancel_all_scheduled_transfers(self):
        """ Cancel all scheduled transfers """
        self.show_scheduled_transfers()
        top_scheduled_row = BaseElement(self.driver, locators.FIRST_SCHEDULED_TRANSFER_LINK)
        while top_scheduled_row.displayed(3):
            self.open_next_scheduled_transfer()
            self.cancel_previewed_transfer()

    def prepare_transfer(self, transfer_amount, from_account, to_account):
        """ Prepare a funds transfer with the specified details and advance to the scheduling step """
        BaseElement(self.driver, locators.TRANSFER_MONEY_BUTTON).click()
        from_account_dropdown = BaseElement(self.driver, locators.FROM_ACCOUNT_DROP_DOWN)
        to_account_dropdown = BaseElement(self.driver, locators.TO_ACCOUNT_DROP_DOWN)
        from_account_dropdown.wait_until_displayed()
        to_account_dropdown.wait_until_displayed()
        from_account_dropdown.select_dropdown_value(from_account)
        to_account_dropdown.select_dropdown_value(to_account)
        TextElement(self.driver, locators.AMOUNT_INPUT).set_text(str(transfer_amount))

    def schedule_transfer(self, days_in_future=0):
        """ Schedule a prepared transfer
            days_in_future is the minimum days in the future to attempt to schedule transfer
        """
        BaseElement(self.driver, locators.TRANSFER_DATE_INPUT).click()
        transfer_calendar = CalendarDatePicker(self.driver)
        transfer_calendar.select_date_by_days_in_future(days_in_future)

    def submit_transfer_request(self):
        """ Submit a prepared and scheduled transfer request """
        submit_button = BaseElement(self.driver, locators.SCHEDULE_TRANSFER_BUTTON)
        submit_button.click()
        BaseElement(self.driver, locators.RECEIPT_STATUS_TEXT).wait_until_displayed()

    def transfer_request_result(self):
        """ return the results of a just submitted transfer request """
        return self.transfer_preview_details()

    def dismiss_transfer_result(self):
        """ Dismiss the results of a scheduled transfer """
        self.close_previewed_transfer()

    def next_scheduled_transfer_summary(self):
        """ Return summarized details of next scheduled transfer, or None if no transfer is scheduled """
        # QA-329 To-Do : Update logic to handle 'no activity' message
        date_caption = BaseElement(self.driver, locators.FIRST_SCHEDULED_TRANSFER_DATE)
        if date_caption.displayed(5):
            transfer_details = {'date': date_caption.get_text()}
        else:
            return None
        # BANK-1683 todo: a method to identify the to, from, and amount fields
        # transfer_details['amount'] = utils.decimal_from_string(BaseElement(self.driver,
        #                                                        locators.FIRST_SCHEDULED_TRANSFER_AMOUNT).get_text())
        # transfer_details['from'] =
        # transfer_details['to'] =
        return transfer_details

    def get_opening_deposit_amount(self):
        """ Return the amount of the Opening Deposit transfer"""
        transfer_amount = BaseElement(self.driver, locators.FIRST_HISTORY_TRANSFER_AMOUNT)
        if transfer_amount.displayed(5):
            opening_deposit = utils.decimal_from_string(transfer_amount.get_text())
        else:
            return None
        return opening_deposit
