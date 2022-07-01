


def check_leap_year(year):
    if year % 4 != 0:
        return 365
    elif year % 100 != 0:
        return 366
    elif year % 400 != 0:
        return 356
    else:
        return 366


