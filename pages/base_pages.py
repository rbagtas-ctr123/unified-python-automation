""" Abstract Base Pages for all page classes """

from abc import ABC
from enum import Enum
from appium.webdriver.webdriver import WebDriver as AppiumDriver
from appium.webdriver.common.touch_action import TouchAction


class PageTypes(Enum):
    """ Supported page types """
    WEB = 'WebPageType'
    IOS = 'iOSPageType'
    ANDROID = 'AndroidPageType'


class BasePage(ABC):
    """ Contains functions used by all page objects & maintains a registry for interfaces & page types

        Interface Page Classes subclass from BasePage and are created with the 'is_interface' argument:

            class SamplePage(BasePage, is_interface=True):

        Child Concrete Page Classes must inherit from both an Interface class and one of the PageTypes

            class SamplePageWeb(SamplePage, WebPageType):

    """

    # The registry of interface pages
    interfacePages = {}

    # Store the driver for element access
    def __init__(self, driver):
        self.driver = driver

    # Interface page classes will instantiate different child page objects
    def __new__(cls, driver):
        # If not an interface page, return an instance of the requested class
        if cls not in set(cls.interfacePages.keys()):
            return object.__new__(cls)
        # Otherwise: decide which registered class to instantiate
        if isinstance(driver, AppiumDriver):
            if driver.capabilities['platformName'] == 'Android':
                new_page_type = PageTypes.ANDROID
            elif driver.capabilities['platformName'] == 'iOS':
                new_page_type = PageTypes.IOS
            else:
                raise ValueError(f"The appium platform of {driver.capabilities['platformName']} is not supported!")
        # Otherwise: it's a web page
        else:
            new_page_type = PageTypes.WEB
        # Instantiate the correct page type object if it's been registered
        if new_page_type in cls.interfacePages[cls].keys():
            return object.__new__(cls.interfacePages[cls][new_page_type])
        else:
            raise NotImplementedError(f"No implementation of '{cls.__name__}' Page class with type '{new_page_type}' "
                                      f"has been registered.  Make sure the implementation has been created and also "
                                      f"imported at the end of the interface page class's file.")

    # Register any new interface pages
    def __init_subclass__(cls, is_interface=False, **kwargs):
        if is_interface:
            cls.interfacePages[cls] = dict()


class WebPageType(BasePage):
    """ Contain functions for only Web based page objects & registers child classes as Web type """
    # Register all child classes as Web-based
    def __init_subclass__(cls, **kwargs):
        if cls.__bases__[0] in cls.interfacePages.keys():
            cls.interfacePages[cls.__bases__[0]][PageTypes.WEB] = cls
        else:
            raise ValueError(f"'{cls.__bases__[0].__name__}' has not been registered as an Page Interface. "
                             f"Make sure the '{cls.__bases__[0].__name__}' is defined with 'is_interface=True'")

    def save_page_source_html(self, filename):
        """ Save the HTML page source to a file """
        with open(filename, "w+") as page_source:
            page_source.write(self.driver.page_source)


class AndroidPageType(BasePage):
    """ Contain functions for only Android based page objects & registers child classes as Android type """
    # Register all child classes as Android-based
    def __init_subclass__(cls, **kwargs):
        cls.interfacePages[cls.__bases__[0]][PageTypes.ANDROID] = cls

    def touch_scroll_up(self):
        """ Scroll up using touch actions """
        win_size = self.driver.get_window_size()
        x_middle = int(win_size['width']*0.5)
        y_bottom = int(win_size['height']*0.8)
        y_top = int(win_size['height']*0.2)
        touch_chain = TouchAction(self.driver)
        touch_chain.press(x=x_middle, y=y_bottom)
        touch_chain.move_to(x=x_middle, y=y_top)
        touch_chain.release()
        touch_chain.perform()


class iOSPageType(BasePage):
    """ Contain functions for only iOS based page objects & registers child classes as iOS type  """
    # Register all child classes as iOS-based
    def __init_subclass__(cls, **kwargs):
        cls.interfacePages[cls.__bases__[0]][PageTypes.IOS] = cls
