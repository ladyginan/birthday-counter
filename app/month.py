import month_names

day_amount = {
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


def get_month_string(month_name):
    for month in month_names.Month:
        if month.name == month_name:
            return int(month.value)


def validate_day_value(day_value, month):
    try:
        day_int = int(day_value)
    except ValueError:
        return False

    if day_int <= 0:
        return False

    for month_name, value in day_amount.items():
        if month == month_name and day_int >= value:
            return False
