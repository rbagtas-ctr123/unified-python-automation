"""This file houses low-level utility functions, such as date math and string
manipulation"""
import re
import random
from datetime import datetime, timedelta
from decimal import Decimal

import warnings
with warnings.catch_warnings():
    # QA-196 todo: Pandas has an import warning.  Temporarily suppressing this warning until a new release fixes it
    warnings.filterwarnings("ignore", category=ImportWarning)
    # QA-287 todo: CircleCI causes an import warning.  We are temporarily suppressing until a solution is found
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    from pandas.tseries.offsets import CustomBusinessDay
    from pandas.tseries.holiday import USFederalHolidayCalendar


def future_day(days_in_future):
    """Returns the date of the day days_in_future days from the current time.
    If days_in_future == 0, returns the current date"""
    today = datetime.today()
    desired_day = today + timedelta(days_in_future)
    return desired_day


def future_business_day(days_in_future):
    """Returns the date of the business day days_in_future business days from
    the current time, thus skipping weekends and US federal holidays. If
    days_in_future == 0, returns the current date. Note that this means the
    return value may not actually be a business day if days_in_future is 0"""
    business_day = CustomBusinessDay(calendar=USFederalHolidayCalendar())
    today = datetime.today()
    desired_day = today + days_in_future*business_day
    return desired_day


def format_date_long(date):
    """Returns date as an all-caps string in MMMM D, YYYY format"""
    return '{0} {1}, {2}'.format(date.strftime('%B'), date.day, 
                                 date.year).upper()


def number_to_dollar_string(number):
    """ Format number with commas and dollar sign to make a string with matches traditional format for money values """
    dollar_string = "{:0.2f}".format(number)
    if dollar_string.find('-') == -1:
        dollar_string = '$' + dollar_string
    else:
        dollar_string = '-$' + dollar_string[1:]
    while re.search(r'(\d)(\d{3}(?:,|\.))', dollar_string):
        dollar_string = re.sub(r'(\d)(\d{3}(?:,|\.))', r'\1,\2',
                               dollar_string)
    return dollar_string


def generate_random_dollar_amount(max_value, min_value=1):
    """Returns a random decimal rounded to two decimal places between min_value and max_value"""
    amount = (random.random() * (max_value-min_value)) + min_value
    return Decimal(amount).quantize(Decimal("1.00"))


def decimal_from_string(string_to_examine):
    """ Returns the first Decimal value found within a string. """
    return Decimal(re.sub(r'[^\d.]', '', string_to_examine))


def remove_whitespace_from_string(string_to_examine):
    """ Returns a string with all whitespace removed. """
    return re.sub(r' ', '', string_to_examine)
