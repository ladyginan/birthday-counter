from datetime import date
from month_util import validate_day_value
from month_util import IncorrectDayValueException


def run_app():
    # parse user input
    b_day = input("Set your birthday day(format example - 'March 24') ")
    b_day_format = b_day.split(" ")
    input_month = b_day_format[0]
    input_day = b_day_format[1]
    today = date.today()
    my_birthday = validate_day_value(input_day, input_month, today.year)

    # calculate
    time_to_birthday = calculate_days_before_b_day(today, my_birthday)
    if my_birthday == today:
        print("Yor birthday is today! Congratulation!")
    else:
        print(f"Your birthday will be in: {time_to_birthday.days} days")


def calculate_days_before_b_day(today, my_birthday):
    if my_birthday < today:
        my_birthday = date(today.year + 1, my_birthday.month, my_birthday.day)
    time_to_birthday = abs(my_birthday - today)
    return time_to_birthday


if __name__ == '__main__':

    while True:
        try:
            run_app()
        except IndexError:
            print("Incorrect input. Check the format example")
        except KeyError:
            print("Incorrect month name")
        except ValueError:
            print("Incorrect day number")
        except IncorrectDayValueException as e:
            print(e.msg)
