def check_leap_year(year) -> bool:
    """Return True if year is a leap year otherwise False"""
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False
