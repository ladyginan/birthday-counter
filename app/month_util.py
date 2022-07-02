from datetime import date
from app import year_util
from app.month import get_month_number

max_amount_of_days_in_month = {
    'January': 31,
    'February': 29,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 30,
    'September': 31,
    'October': 30,
    'November': 31,
    'December': 30
}


class Error(Exception):
    """Base class for exceptions"""

    def __init__(self, msg):
        self.msg = msg
        super().__init__(self.msg)

    pass


class IncorrectDayValueException(Error):
    """Throws when user put an incorrect day value(e.g. 0, 111111, -6)"""


def validate_day_value(day_value, month, year) -> date:
    """
    Ensures that the day value is in the range of valid values.
    In case of 29 February, it'll check if a year is a leap year.
    If the year isn't a leap, the b_date will be changed to 1 March
    """
    day_int = int(day_value)

    if day_int <= 0:
        raise IncorrectDayValueException(msg="Wrong input, day can't be zero or below")

    month_number = get_month_number(month)
    days_in_month = max_amount_of_days_in_month[month]

    if day_int > days_in_month:
        raise IncorrectDayValueException(msg="Wrong input, the day value is greater than days in the month")

    if month == 'February' and day_int == 29:
        is_leap_year = year_util.check_leap_year(year)
        if not is_leap_year:
            return date(year, get_month_number('March'), 1)

    return date(year, month_number, day_int)
