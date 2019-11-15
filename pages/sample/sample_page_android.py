""" Implement functions of the Android SamplePage """

from pages.sample.sample_page import SamplePage
from pages.base_pages import AndroidPageType


class SamplePageAndroid(SamplePage, AndroidPageType):
    def whoami(self):
        return "I am SamplePage on Android!"
