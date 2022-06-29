import month_names

max_day_amount = {
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


def get_month_number(month_name):
    return month_names.Month[month_name].value


def validate_day_value(day_value, month):
    try:
        day_int = int(day_value)
    except ValueError:
        return False

    if day_int <= 0:
        return False

    for month_name, value in max_day_amount.items():
        if month == month_name and day_int >= value:
            return False
    return True
