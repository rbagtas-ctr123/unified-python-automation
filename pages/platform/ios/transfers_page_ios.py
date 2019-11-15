""" Implement functions of the iOS TransfersPage """

from pages.platform.ios import transfers_locators_ios as locators
from pages.platform.transfers_page import TransfersPage
from pages.base_pages import iOSPageType


class TransfersPageiOS(TransfersPage, iOSPageType):
    """ Implement functions of the iOS TransfersPage """

    def wait_until_transfers_displayed(self):
        """ Check  whether the current page is the transfers page
            Dismiss any 'First-Visit' tutorial hints
        """
        raise NotImplementedError

    def show_scheduled_transfers(self):
        """ Show scheduled transfers """
        raise NotImplementedError

    def open_next_scheduled_transfer(self):
        """ Preview the next scheduled transfer """
        raise NotImplementedError

    def transfer_preview_details(self):
        """ return the results of a previewed transfer """
        raise NotImplementedError

    def close_previewed_transfer(self):
        """ close the previewed transfer """
        raise NotImplementedError

    def cancel_previewed_transfer(self):
        """ cancel the previewed transfer """
        raise NotImplementedError

    def cancel_all_scheduled_transfers(self):
        """ Cancel all scheduled transfers """
        raise NotImplementedError

    def prepare_transfer(self, transfer_amount, from_account, to_account):
        """ Prepare a funds transfer with the specified details and advance to the scheduling step """
        raise NotImplementedError

    def schedule_transfer(self, days_in_future=0):
        """ Schedule a prepared transfer
            days_in_future is the minimum days in the future to attempt to schedule transfer
        """
        raise NotImplementedError

    def submit_transfer_request(self):
        """ Submit a prepared and scheduled transfer request """
        raise NotImplementedError

    def transfer_request_result(self):
        """ return the results of a just submitted transfer request """
        raise NotImplementedError

    def dismiss_transfer_result(self):
        """ Dismiss the results displayed after a transfer is scheduled or performed """
        raise NotImplementedError

    def next_scheduled_transfer_summary(self):
        """ Return summarized details of next scheduled transfer, or None if no transfer is scheduled """
        raise NotImplementedError
