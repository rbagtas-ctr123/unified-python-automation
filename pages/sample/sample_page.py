""" Interface Page Class for the automation dev testing

    File must import all implementation subclasses to ensure they are registered during test collection
    Those imports must be after the interface class to avoid circular references during import
"""

from pages.base_pages import BasePage
from abc import abstractmethod


class SamplePage(BasePage, is_interface=True):
    """ Methods for testing the development of page classes """

    @abstractmethod
    def whoami(self):
        """  Identify itself """


from pages.sample.sample_page_android import SamplePageAndroid
from pages.sample.sample_page_ios import SamplePageiOS
from pages.sample.sample_page_web import SamplePageWeb
