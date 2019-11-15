""" Interface Page Class for the Dashboard page of the Aspiration application

    File must import all implementation subclasses to ensure they are registered during test collection
    Those imports must be after the interface class to avoid circular references during import
"""

from abc import abstractmethod
from pages.base_pages import BasePage

from enum import IntEnum


class Products(IntEnum):
    """ Enum representation of the product.code/id found in the product table"""
    REDWOOD = 1
    FLAGSHIP = 2
    SPEND = 4
    SAVE = 5


class ProductApplicationStatus(IntEnum):
    """ Enum representation of the user_product_application.status found in the user_product_application table """
    DOES_NOT_EXIST = 0  # UNDEFINED
    IN_PROGRESS = 1  # NEW
    UNCONFIRMED = 2
    SUBMITTED = 3
    COMPLETED = 4  # APPROVED
    REJECTED = 5
    CANCELLED = 6
    PENDING = 7
    PENDING_ERROR = 8
    PENDING_RECONCILIATION = 9
    STARTED_MIGRATION = 10
    MIGRATING = 11


class DashboardPage(BasePage, is_interface=True):
    """ Interface Page Class for the Dashboard page of the Aspiration application """

    @abstractmethod
    def wait_until_dashboard_displayed(self):
        """ Check  whether the current page is the dashboard.
            Return true if dashboard elements appear
            Return false if they do not """

    @abstractmethod
    def get_product_balance(self, product):
        """ Return the displayed balance of a user's chosen product """

    @abstractmethod
    def get_product_status(self, product):
        """ Return the status of the supplied product """

    @abstractmethod
    def continue_product_application(self, product):
        """ Wait for Dashboard to display then continue a Product Application """

    @abstractmethod
    def wait_until_debit_card_tracker_displayed(self):
        """ Wait until the Debit Card Tracker is displayed """


from pages.platform.android.dashboard_page_android import DashboardPageAndroid
from pages.platform.ios.dashboard_page_ios import DashboardPageiOS
from pages.platform.web.dashboard_page_web import DashboardPageWeb
