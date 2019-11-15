
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from utilities.utils import future_business_day
from pages.elements.base_elements import BaseElement

DEFAULT_TIMEOUT = 10


class CalendarDatePicker(object):
    """ Enables methods to interact with aspirations custom calendar date picker only works with Web platform"""

    def __init__(self, driver):
        self.driver = driver
        self.date = dict()
        self.calendar_date_picker = (By.XPATH, '//div[@id="react-aria-modal-dialog"]')
        self.month_heading = (By.XPATH, '//button[@data-test-id="DatePickerMonth"]')
        self.previous_month_button = (By.XPATH, '//button[@aria-label="Previous Month"]')
        self.next_month_button = (By.XPATH, '//button[@aria-label="Next Month"]')
        self.use_this_date_button = (By.XPATH, '//button[contains(text(), "Use This Date")]')
        self.disabled_use_date_button = (By.XPATH, '//button[contains(text(), "Use This Date") '
                                                   'and @aria-disabled="true"]')
        self.enabled_day_buttons = (By.XPATH, '//button[@data-test-id="DatePickerDay-enabled"]')
        self.disabled_day_buttons = (By.XPATH, '//button[@data-test-id="DatePickerDay-disabled"]')
        self.enabled_selected_day_button = (By.XPATH, '//button[@data-test-id="DatePickerDay-enabled-selected"]')
        self.disabled_selected_day_button = (By.XPATH, '//button[@data-test-id="DatePickerDay-enabled-selected"]')
        self.selected_day = (By.XPATH, '//button[contains(@data-test-id, "DatePickerDay") '
                                       'and contains(@data-test-id, "selected")]')
        self.day_number = (By.XPATH, './/span[text()]')

    def get_calendar_date_picker(self, seconds_to_wait=DEFAULT_TIMEOUT):
        try:
            WebDriverWait(self.driver, seconds_to_wait).\
                until(ec.visibility_of_element_located(self.calendar_date_picker))
        except TimeoutException:
            raise ElementNotVisibleException(f"Element '{self.calendar_date_picker}' exists, but are not visible")
        date_picker = self.driver.find_element(*self.calendar_date_picker)
        return date_picker

    def get_available_dates(self, seconds_to_wait=DEFAULT_TIMEOUT):
        """
        Returns list of enabled day elements
        :param seconds_to_wait: set to default timeout
        :return: element object
        """
        try:
            WebDriverWait(self.driver, seconds_to_wait).\
                until(ec.visibility_of_all_elements_located(self.enabled_day_buttons))
        except TimeoutException:
            raise ElementNotVisibleException(f"Element '{self.enabled_day_buttons}' exists, but are not visible")
        dict_of_days = {}
        available_days = self.driver.find_elements(*self.enabled_day_buttons)
        for date in available_days:
            day = date.find_element(*self.day_number)
            dict_of_days[day.text] = date
        return dict_of_days

    def get_unavailable_dates(self, seconds_to_wait=DEFAULT_TIMEOUT):
        """
        Returns list of disabled day elements
        :param seconds_to_wait: set to default timeout
        :return: element object
        """
        try:
            WebDriverWait(self.driver, seconds_to_wait).\
                until(ec.visibility_of_all_elements_located(self.disabled_day_buttons))
        except TimeoutException:
            raise ElementNotVisibleException(f"Element '{self.disabled_day_buttons}' exists, but are not visible")
        dict_of_days = {}
        unavailable_days = self.driver.find_elements(*self.disabled_day_buttons)
        for date in unavailable_days:
            day = date.find_element(*self.day_number)
            dict_of_days[day.text] = date
        return dict_of_days

    def get_selected_day(self, seconds_to_wait=DEFAULT_TIMEOUT):
        """
        Return selected day element
        :param seconds_to_wait: set to default timeout
        :return: element object
        """
        selected_day = dict()
        try:
            WebDriverWait(self.driver, seconds_to_wait).until(ec.element_to_be_clickable(self.selected_day))
        except TimeoutException:
            raise ElementNotVisibleException(f"Element '{self.selected_day}' exists, but is not click-able")
        day = self.driver.find_element(*self.selected_day)
        day_number = day.find_element(*self.day_number).text
        selected_day[day_number] = day
        return selected_day

    def get_month_year(self, seconds_to_wait=DEFAULT_TIMEOUT):
        """
        Returns current month
        :param seconds_to_wait: set to default timeout
        :return: text of month year heading element
        """
        try:
            WebDriverWait(self.driver, seconds_to_wait).until(ec.visibility_of_element_located(self.month_heading))
        except TimeoutException:
            raise ElementNotVisibleException(f"Element '{self.month_heading}' exists, but is not visible")
        month_year = self.driver.find_element(*self.month_heading)
        return month_year.text

    def select_day(self, day):
        """
        Selects an available day within a month
        :param day: a string representation of the day number that is wanting to be clicked
        :return: Clicks a day button on the calendar no object is returned
        """
        available_days = self.get_available_dates()
        unavailable_days = self.get_unavailable_dates()
        if day in unavailable_days:
            for key in sorted(available_days):
                if int(day) < int(key):
                    day_to_select = available_days[key]
                    day_to_select.click()
        elif day in available_days:
            day_to_select = available_days[day]
            day_to_select.click()
        else:
            raise ValueError(f'The value "{day}" is not a valid day to click')

    def select_month_year(self, month_year, seconds_to_wait=DEFAULT_TIMEOUT):
        """
        Selects a month
        :param month_year: String of month and year
        :param seconds_to_wait: DEFAULT_TIMEOUT
        :return: Navigates the months on the calendar no object is returned
        """
        preferred_month_year = month_year
        month_year_heading = self.get_month_year()
        try:
            WebDriverWait(self.driver, seconds_to_wait).until(ec.visibility_of_element_located(self.next_month_button))
            while month_year_heading != preferred_month_year:
                next_month_button = self.driver.find_element(*self.next_month_button)
                if not next_month_button.get_attribute('disabled'):
                    next_month_button.click()
                break
        except TimeoutException:
            raise ElementNotVisibleException(f"Element '{self.month_heading}' exists, but is not visible")

    def transform_days_to_date(self, days_in_future):
        """
        Take the days in future var and transforms it into a usable day month year
        :param days_in_future:
        :return: date dict
        """
        transfer_date = future_business_day(days_in_future)
        self.date['month_year'] = transfer_date.strftime('%B') + ' ' + str(transfer_date.year)
        self.date['day'] = str(transfer_date.day)
        return self.date

    def select_date_by_days_in_future(self, days_in_future):
        """
        Navigates through Calendar selecting the month, day, year from the days_in_future
        :param days_in_future: int
        :return:
        """
        self.transform_days_to_date(days_in_future)
        day = self.date['day']
        month_year = self.date['month_year']
        self.select_month_year(month_year)
        self.select_day(day)
        self.driver.find_element(*self.use_this_date_button).click()
        BaseElement(self.driver, self.month_heading).wait_until_not_displayed()
