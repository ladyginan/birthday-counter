from datetime import date

import month

bday = input("Set your birthday day(format example - 'March 24') ")

bday_format = bday.split(" ")
input_month = bday_format[0]
input_day = bday_format[1]

today = date.today()
print(today)

# Validation
bday_month = month.get_month_string(input_month)
if bday_month is None:
    print("Incorrect month name")

bday_day_valid = month.validate_day_value(input_day, input_month)

if bday_day_valid is False:
    print("Incorrect day number")

bday_day = int(input_day)

my_birthday = date(today.year, bday_month, bday_day)

if my_birthday < today:
    my_birthday = date(today.year+1, bday_month, bday_day)


time_to_birthday = abs(my_birthday - today)
print("Your birthday will be in: " + str(time_to_birthday.days))
