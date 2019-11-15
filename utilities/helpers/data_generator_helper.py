import random
import string
import time


def generate_random_phone_number() -> str:
    """Returns a randomly generated Phone Number"""
    return str(random.randint(1000000000, 9999999999))


def generate_random_ssn(will_pass_alloy_sandbox_verification: bool) -> str:
    """
    Returns a randomly generated SSN
    :param will_pass_alloy_sandbox_verification:
        - True results in a SSN with a pattern of ###-##-0001
        - False results in a SSN with a pattern of ###-##-0002
    """
    first_three = str(random.randint(100, 899))
    while first_three is '666':
        first_three = str(random.randint(100, 899))
    second_two = str(random.randint(10, 99))
    first_five = first_three + second_two
    # TODO will need to expand to cover off on other Alloy statuses QA-256
    if will_pass_alloy_sandbox_verification is True:
        ssn = first_five + '0001'
    else:
        ssn = first_five + '0002'
    return ssn


def generate_random_string(min_length: int, max_length: int) -> str:
    """ Generate a string based on the min and max range given """
    chars = string.ascii_letters
    size = random.randint(min_length, max_length)
    return ''.join(random.choice(chars) for _ in range(size))


def generate_timestamped_email(email_suffix: str) -> str:
    """Creates an email using current UTC time and adds it to the front of the supplied email domain"""
    current_milli_time = int(round(time.time() * 1000))
    test_time = str(current_milli_time)
    email = (test_time + '+' + email_suffix)
    return email
