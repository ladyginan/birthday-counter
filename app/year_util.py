def check_leap_year(year) -> bool:
    """Return True if year is a leap year otherwise False"""
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


