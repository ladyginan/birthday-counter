from datetime import date

import month


def run_app():
    b_day = input("Set your birthday day(format example - 'March 24') ")

    b_day_format = b_day.split(" ")
    input_month = b_day_format[0]
    input_day = b_day_format[1]

    today = date.today()
    print(today)

    # Validation
    b_day_month = month.get_month_number(input_month)
    if b_day_month is None:
        print("Incorrect month name")

    b_day_day_valid = month.validate_day_value(input_day, input_month)

    if b_day_day_valid is False:
        print("Incorrect day number")

    b_day_day = int(input_day)

    my_birthday = date(today.year, b_day_month, b_day_day)

    if my_birthday < today:
        my_birthday = date(today.year + 1, b_day_month, b_day_day)

    time_to_birthday = abs(my_birthday - today)
    print("Your birthday will be in: " + str(time_to_birthday.days))


if __name__ == '__main__':

    while True:
        run_app()
