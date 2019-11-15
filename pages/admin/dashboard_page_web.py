""" Implement functions of the Admin20 Dashboard Page """

import pages.admin.dashboard_locators_web as locators
from pages.elements.base_elements import BaseElement
from pages.admin.dashboard_page import AdminDashboardPage
from pages.base_pages import WebPageType


class AdminDashboardPageWeb(AdminDashboardPage, WebPageType):
    """ Implement functions of the Admin20 Dashboard Page """

    def wait_until_dashboard_displayed(self):
        """ Check  whether the dashboard loads
            Return true if dashboard elements appear
            Return false if they do not """
        BaseElement(self.driver, locators.DASHBOARD_HEADER).wait_until_displayed()
        BaseElement(self.driver, locators.DASHBOARD_FRAME).wait_until_displayed()
