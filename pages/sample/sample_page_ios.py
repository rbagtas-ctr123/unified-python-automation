""" Implement functions of the iOS SamplePage """

from pages.sample.sample_page import SamplePage
from pages.base_pages import iOSPageType


class SamplePageiOS(SamplePage, iOSPageType):
    def whoami(self):
        return "I am SamplePage on iOS!"
