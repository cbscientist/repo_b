"""
Source repo that I'd like to merge
"""
from datetime import datetime


def sleep_in(gone_fishing: bool) -> bool:
    """
    Function that returns true if it is the weekend or if it a vacation day
    """
    current_date = datetime.today()
    day_of_week = current_date.weekday()

    if day_of_week in [5, 6] or gone_fishing is True:
        return True
    else:
        return False


if __name__=="__main__":
    print(sleep_in(gone_fishing=False))