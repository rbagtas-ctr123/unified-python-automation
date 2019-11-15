""" Interface Page Class for the TransfersPage page of the Aspiration application

    File must import all implementation subclasses to ensure they are registered during test collection
    Those imports must be after the interface class to avoid circular references during import
"""

from abc import abstractmethod
from pages.base_pages import BasePage
from enum import IntEnum


class TransferStatus(IntEnum):
    """ Possible Transfer Record statuses.  The value corresponds to the database value they are saved as """
    SCHEDULED = 1
    PROCESSING = 2
    COMPLETED = 3
    CANCELLED = 4
    REJECTED = 5
    INITIAL_FUNDING = 6
    RETURNED = 7


class TransfersPage(BasePage, is_interface=True):
    """ Interface Page Class for the TransfersPage page of the Aspiration application """

    SPEND_ACCOUNT = 'Aspiration Spend'
    SAVE_ACCOUNT = 'Aspiration Save'

    @abstractmethod
    def wait_until_transfers_displayed(self):
        """ Check  whether the current page is the transfers page
            Dismiss any 'First-Visit' tutorial hints
        """

    @abstractmethod
    def show_scheduled_transfers(self):
        """ Show scheduled transfers """

    @abstractmethod
    def open_next_scheduled_transfer(self):
        """ Preview the next scheduled transfer """

    @abstractmethod
    def transfer_preview_details(self):
        """ return the results of a previewed transfer """

    @abstractmethod
    def close_previewed_transfer(self):
        """ close the previewed transfer """

    @abstractmethod
    def cancel_previewed_transfer(self):
        """ cancel the previewed transfer """

    @abstractmethod
    def cancel_all_scheduled_transfers(self):
        """ Cancel all scheduled transfers """

    @abstractmethod
    def prepare_transfer(self, transfer_amount, from_account, to_account):
        """ Prepare a funds transfer with the specified details and advance to the scheduling step """

    @abstractmethod
    def schedule_transfer(self, days_in_future=0):
        """ Schedule a prepared transfer
            days_in_future is the minimum days in the future to attempt to schedule transfer
        """

    @abstractmethod
    def submit_transfer_request(self):
        """ Submit a prepared and scheduled transfer request """

    @abstractmethod
    def transfer_request_result(self):
        """ return the results of a just submitted transfer request """

    @abstractmethod
    def dismiss_transfer_result(self):
        """ Dismiss the results displayed after a transfer is scheduled or performed """

    @abstractmethod
    def next_scheduled_transfer_summary(self):
        """ Return summarized details of next scheduled transfer, or None if no transfer is scheduled """

    @abstractmethod
    def get_opening_deposit_amount(self):
        """Return the amount of the opening deposit transfer"""


from pages.platform.android.transfers_page_android import TransfersPageAndroid
from pages.platform.ios.transfers_page_ios import TransfersPageiOS
from pages.platform.web.transfers_page_web import TransfersPageWeb
