from datetime import date

import month_util
from app.month import get_month_number


def run_app():
    # parse user input
    b_day = input("Set your birthday day(format example - 'March 24') ")
    b_day_format = b_day.split(" ")
    input_month = b_day_format[0]
    input_day = b_day_format[1]
    b_day_month = get_month_number(input_month)
    b_day_day = month_util.validate_day_value(input_day, input_month)

    # calculate
    time_to_birthday = calculate_days_before_b_day(b_day_month, b_day_day)
    print("Your birthday will be in: " + str(time_to_birthday.days))


def calculate_days_before_b_day(b_day_month, b_day_day):
    today = date.today()
    my_birthday = date(today.year, b_day_month, b_day_day)

    if my_birthday < today:
        my_birthday = date(today.year + 1, b_day_month, b_day_day)
    time_to_birthday = abs(my_birthday - today)
    return time_to_birthday


if __name__ == '__main__':

    while True:
        try:
            run_app()
        except IndexError:
            print("Incorrect input")
        except KeyError:
            print("Incorrect month name")
        except ValueError:
            print("Incorrect day number")
        except month_util.IncorrectDayValueException as e:
            print(e.msg)
