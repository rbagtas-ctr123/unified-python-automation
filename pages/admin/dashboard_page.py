""" Interface Page Class for the Dashboard page of the Admin20 application

    File must import all implementation subclasses to ensure they are registered during test collection
    Those imports must be after the interface class to avoid circular references during import
"""

from abc import abstractmethod
from pages.base_pages import BasePage


class AdminDashboardPage(BasePage, is_interface=True):
    """ Interface Page Class for the Dashboard page of the Admin20 application """

    @abstractmethod
    def wait_until_dashboard_displayed(self):
        """ Check  whether the dashboard loads
            Return true if dashboard elements appear
            Return false if they do not """


import pages.admin.dashboard_page_web
