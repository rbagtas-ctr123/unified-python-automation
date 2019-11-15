"""This module contains definitions of classes for all kinds of web elements which we might want to interact with.
   This module also includes the base class for web page objects"""

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException, WebDriverException,\
    InvalidElementStateException, ElementNotSelectableException, InvalidArgumentException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
import time

DEFAULT_TIMEOUT = 10


class BaseElement(object):
    """Contains general functions applicable to all page elements. Every element shall inherit from this one
       All functions must return 1 of:  The Requested information, 'True' upon completion, or a relevant Exception"""

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    # Blocking actions: These will throw Exceptions when the action fails
    def scroll_into_viewport(self, seconds_to_wait=DEFAULT_TIMEOUT):
        """ Scroll the center of the element into view, if it's not already within view """
        element = self.driver.find_element(*self.locator)
        element_in_view = ec_in_viewport(self.locator)
        if not element_in_view(self.driver):
            self.driver.execute_script("arguments[0].scrollIntoView({block: \"center\"});", element)
            try:
                WebDriverWait(self.driver, seconds_to_wait, poll_frequency=0.1).until(element_in_view)
            except TimeoutException:
                raise ElementNotVisibleException(f"Element '{self.locator}' exists, but cannot be scrolled into view")

    def click(self, seconds_to_wait=DEFAULT_TIMEOUT):
        """Clicks the element.  Returns an exception upon failure"""
        try:
            WebDriverWait(self.driver, seconds_to_wait).until(ec.element_to_be_clickable(self.locator))
            # Even if the element is visible, it may still be moving.  Wait until it's stable.
            WebDriverWait(self.driver, seconds_to_wait).until(ec_element_to_be_still(self.locator))
        except TimeoutException:
            pass
        # Even if the desired element was never clickable, try anyways so we get a precise exception
        self.driver.find_element(*self.locator).click()
        return True

    def select_dropdown_value(self, value, seconds_to_wait=DEFAULT_TIMEOUT):
        """ Select an option from a drop down element"""
        try:
            WebDriverWait(self.driver, seconds_to_wait).until(ec.element_to_be_clickable(self.locator))
            WebDriverWait(self.driver, seconds_to_wait).until(ec_element_to_be_still(self.locator))
            drop_down = Select(self.driver.find_element(*self.locator))
            options = drop_down.options
            for option in options:
                # Attempt to get the option by text
                if value in option.text:
                    drop_down.select_by_visible_text(option.text)
                    break
                # Else attempt to get it by value
                elif value in option.get_attribute('value'):
                    drop_down.select_by_value(option.get_attribute("value"))
                    break
        except TimeoutException:
            raise ValueError(f'The value {value} does not exist in the drop down')

    def wait_until_gone(self, seconds_to_wait=DEFAULT_TIMEOUT):
        """ Waits for an element to be disappear from the DOM. """
        # qa-315 todo: Use the included "none_of" EC when it's included in selenium
        # WebDriverWait(self.driver, seconds_to_wait).until(ec.none_of(ec.presence_of_element_located(self.locator)))
        WebDriverWait(self.driver, seconds_to_wait).until_not(ec.presence_of_element_located(self.locator))
        return True

    def wait_until_displayed(self, seconds_to_wait=DEFAULT_TIMEOUT):
        """ Wait for an element to appear, and raise the correct exception if it doesn't """
        try:
            WebDriverWait(self.driver, seconds_to_wait).until(
                ec.visibility_of_element_located(self.locator))
        except TimeoutException:
            if self.driver.find_element(*self.locator):
                raise ElementNotVisibleException(f"Element '{self.locator}' exists but is not visible")
        return True

    def wait_until_not_displayed(self, seconds_to_wait=DEFAULT_TIMEOUT):
        """ Wait for an element to disappear, and return a timeout exception if it doesn't """
        WebDriverWait(self.driver, seconds_to_wait).until(ec.invisibility_of_element_located(self.locator))
        return True

    def wait_until_selected(self, seconds_to_wait=DEFAULT_TIMEOUT):
        """ Wait for an element to be selected, and raise the correct exception if it isn't """
        try:
            WebDriverWait(self.driver, seconds_to_wait).until(
                ec.element_located_selection_state_to_be(self.locator, True))
        except TimeoutException:
            if self.driver.find_element(*self.locator):
                raise InvalidElementStateException(f"Element '{self.locator}' exists but is not selected")
        return True

    def get_text(self, seconds_to_wait=DEFAULT_TIMEOUT):
        """ Return the text in the element """
        element = WebDriverWait(self.driver, seconds_to_wait).until(
            ec.visibility_of_element_located(self.locator))
        return element.text

    def get_attribute(self, attribute, seconds_to_wait=DEFAULT_TIMEOUT):
        """ Return the value of attribute if element has such an attribute
            Return None if element does not have that attribute does not
            Return an exception if the element could not be located"""
        try:
            WebDriverWait(self.driver, seconds_to_wait).until(ec.visibility_of_element_located(self.locator))
        except TimeoutException:
            if self.driver.find_element(*self.locator):
                raise ElementNotVisibleException(f"Element '{self.locator}' exists but is not visible")
        self.driver.find_element(*self.locator).get_attribute(attribute)

    # Non-blocking requests for information: these will never throw exceptions
    def displayed(self, seconds_to_wait=0):
        """ Return true if an element is displayed.  Optional timeout."""
        try:
            WebDriverWait(self.driver, seconds_to_wait).until(
                ec.visibility_of_element_located(self.locator))
            return True
        except TimeoutException:
            return False

    def not_displayed(self, seconds_to_wait=0):
        """ Return true if an element is not displayed. Optional timeout. """
        try:
            WebDriverWait(self.driver, seconds_to_wait).until_not(
                ec.visibility_of_element_located(self.locator))
            return True
        except TimeoutException:
            return False


class TextElement(BaseElement):
    """ Child class for text elements """
    def set_text(self, value, seconds_to_wait=DEFAULT_TIMEOUT):
        """ Clear & type text into the element. """
        self.click(seconds_to_wait)
        element = self.driver.find_element(*self.locator)
        element.clear()
        element.send_keys(value)
        return True

    def send_keypress(self, key, number_to_send=1):
        """ Send 1 or more keypresses to the element """
        # If key argument contains more than one character, throw exception
        if len(key) != 1:
            raise InvalidArgumentException("'key' argument must be a single character; '{key}' is invalid.")
        self.click()
        element = self.driver.find_element(*self.locator)
        [element.send_keys(key) for _ in range(number_to_send)]
        return True


class DropdownElement(BaseElement):
    """Child class for dropdown menu elements"""
    def select_value(self, search_term, seconds_to_wait=DEFAULT_TIMEOUT):
        """ Select a value in a dropdown by typing the search term and pressing Enter.
            Returns an exceptions if element could not be located"""
        element = WebDriverWait(self.driver, seconds_to_wait).until(
            ec.visibility_of_element_located(self.locator))
        element.clear()
        element.send_keys(search_term)
        element.send_keys(Keys.RETURN)
        return True


class IframeElement(BaseElement):
    """ Child class for iframe elements """
    def switch_to_iframe(self, start_at_default_content, seconds_to_wait=DEFAULT_TIMEOUT):
        """
        Waits for the iframe to be available then performs self.driver.switch_to.frame(self.locator)
        If start_at_default_content is True will switch to default content first then switch to the iframe element
        """
        if start_at_default_content is True:
            self.driver.switch_to.default_content()
            WebDriverWait(self.driver, seconds_to_wait).until(ec.frame_to_be_available_and_switch_to_it(self.locator))
        else:
            WebDriverWait(self.driver, seconds_to_wait).until(ec.frame_to_be_available_and_switch_to_it(self.locator))
        return True


class WindowElement:
    """ Child class for Window elements """
    def __init__(self, driver):
        self.driver = driver

    def wait_until_window_switched(self, identifier_element, window_index=1, seconds_to_wait=DEFAULT_TIMEOUT):
        """ Wait until the switch to a new window is confirmed by finding the identifying element
        Raises an exception if the identifying element is not found  """
        WebDriverWait(self.driver, seconds_to_wait, ignored_exceptions=WebDriverException).until(
            ec_window_switched(identifier_element, window_index))

    def wait_until_one_window_exists(self, seconds_to_wait=DEFAULT_TIMEOUT):
        """Waits until only one window exists and switches focus to that window"""
        WebDriverWait(self.driver, seconds_to_wait).until(ec.number_of_windows_to_be(1))
        self.driver.switch_to.window(self.driver.window_handles[0])


class AndroidBaseElement(BaseElement):
    """ Child class for Android Base elements
        Android elements require different logic to accurately return click exceptions
    """
    def click(self, seconds_to_wait=DEFAULT_TIMEOUT):
        """ Clicks the element.  Returns an exception upon failure """
        try:
            WebDriverWait(self.driver, seconds_to_wait).until(ec.element_to_be_clickable(self.locator))
            self.driver.find_element(*self.locator).click()
        except TimeoutException:
            # Element is not clickable; attempt to return a precise exception
            e = self.driver.find_element(*self.locator)
            if not e.is_displayed():
                raise ElementNotVisibleException
            raise ElementNotSelectableException("Element was not clickable")
        return True


class AndroidTextElement(AndroidBaseElement, TextElement):
    """ Child class for Android Text elements
        Combines both AndroidBaseElement + TextElement functions without adding any new ones
    """
    pass


class ec_window_switched(object):
    """  expected condition that a window switch was successful.  Confirms by locating an expected element """
    def __init__(self, locator, window_index):
        self.locator = locator
        self.window_index = window_index

    def __call__(self, driver):
        driver.switch_to.window(driver.window_handles[self.window_index])
        return ec._find_element(driver, self.locator)


class ec_element_to_be_still(object):
    """  expected condition that an element is not in motion.  Confirms by comparing element position after a delay """
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        e = driver.find_element(*self.locator)
        initial_position = e.location
        time.sleep(0.1)
        return initial_position == e.location


def ec_in_viewport(locator):
    """ expected condition that the center of the element will be within the viewport """
    def in_viewport_condition(driver):
        element = driver.find_element(*locator)
        element_center_x = element.rect['x'] + ((element.rect['width'])/2)
        element_center_y = element.rect['y'] + ((element.rect['height'])/2)
        return all((
                element_center_x <= driver.execute_script('return document.documentElement.clientWidth'),
                element_center_y <= driver.execute_script('return document.documentElement.clientHeight') +
                driver.execute_script('return window.pageYOffset;')
                ))
    return in_viewport_condition
