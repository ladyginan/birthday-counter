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
    day_int = int(day_value)

    if day_int <= 0:
        raise IncorrectDayValueException(msg="Wrong input, day can't be zero or below")

    for month_name, value in max_amount_of_days_in_month.items():
        if month == month_name:
            if day_int <= value:
                break
            else:
                raise IncorrectDayValueException(msg="Wrong input, day value is more than days in the month")
        break

    if month == get_month_number('February') and day_int == 29:
        is_leap_year = year_util.check_leap_year(year)
        if not is_leap_year:
            return date(year, get_month_number('March'), 1)

    return date(year, month, day_int)
