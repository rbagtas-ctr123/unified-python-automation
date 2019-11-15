""" Common + Pattern tests for experimenting during automation development

    Kept in the repository to save the time of recreating common diagnostic tests
"""

import pytest
from selenium.webdriver.remote.webdriver import WebDriver as SeleniumDriver
from appium.webdriver.webdriver import WebDriver as AppiumDriver
from pages.platform import LoginPage, TransfersPage, NavigationPage, DashboardPage
from pages.sample import SamplePage


@pytest.mark.dev
@pytest.mark.skip
@pytest.mark.platform("android", "chrome", "firefox")
class TestDev:
    """ Tests for experiments to confirm that the automation architecture is performing as expected. """

    def test_config_report(self, env_config, driver):
        """ Print information about what environment and drivers the test has been given """

        print(f"environment: {env_config['env']}")
        print(f"mobile info: {env_config['mobile']}")
        print(f"Selenium Driver?: {isinstance(driver, SeleniumDriver)}")
        print(f"Appium Driver?: {isinstance(driver, AppiumDriver)}")

        sample = SamplePage(driver)
        print(f"\nWhat page am I? {sample.whoami()}")
        t = TransfersPage(driver)
        print(f"transfers page:  {t.__class__}")

    @pytest.mark.platform("chrome")
    def test_chrome_only(self, env_config, driver):
        """ Marked to be run only when 'chrome' platform is specified """
        print(f"\nrunning 'chrome only'")

    @pytest.mark.platform("firefox")
    def test_firefox_only(self, env_config, driver):
        """ Marked to be run only when 'firefox' platform is specified """
        print(f"\nrunning 'firefox only'")

    @pytest.mark.platform("firefox", "android")
    def test_firefox_android(self, env_config, driver):
        """ Marked to be run only when either 'firefox' or 'android' platform is specified """
        print(f"\nrunning 'firefox-or-android'")

    @pytest.mark.platform("chrome", "firefox")
    def test_web_platforms(self, env_config, driver):
        """ Marked to be run only when a web platform is specified """
        print(f"\nrunning 'any web platform'")

    @pytest.mark.platform("android")
    def test_android_platform(self, env_config, driver):
        """ Marked to be run only when android platform is specified """
        print(f"\nrunning 'any android platform'")
