""" Implement functions of the Web SamplePage """

from pages.sample.sample_page import SamplePage
from pages.base_pages import WebPageType


class SamplePageWeb(SamplePage, WebPageType):
    def whoami(self):
        return "I am SamplePage on Web!"
