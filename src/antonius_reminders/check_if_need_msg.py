from datetime import datetime
from typing import Optional

def is_message_date(check_date_start: datetime, msg_every_x_days: int, test_date: Optional[datetime]=None) -> bool:
    """
    Check if the given date (or current date by default) is exactly msg_every_x_days days
    from the start date.

    Args:
        check_date_start (datetime): The start date to calculate recurrence from.
        msg_every_x_days (int): The number of days for recurrence.
        test_date (Optional[datetime]): A specific date to test against. If not provided,
                                        the current date and time will be used.

    Returns:
        bool: True if the test_date (or current date) is exactly msg_every_x_days days
              from check_date_start, otherwise False.
    """
    if test_date is None:
        compare_date = datetime.now()
    else:
        compare_date = test_date

    # Calculate the difference in days between the current date and the start date
    delta_days = (compare_date - check_date_start).days

    # Check if the difference in days is a multiple of msg_every_x_days
    return delta_days >= 0 and delta_days % msg_every_x_days == 0


