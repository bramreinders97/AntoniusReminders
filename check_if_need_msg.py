from datetime import datetime

def is_message_date(check_date_start: datetime, msg_every_x_weeks: int) -> bool:
    """
    Check if the current_date is exactly recurring_week_delta weeks from check_date_start.

    Args:
        check_date_start (datetime): The start date.
        msg_every_x_weeks (int): The number of weeks to check recurrence.

    Returns:
        bool: True if current_date is exactly msg_every_x_weeks weeks from check_date_start, otherwise False.
    """
    # Calculate the difference in days between the current date and the start date
    delta_days = (datetime.now() - check_date_start).days

    # Check if the difference in days is a multiple of msg_every_x_weeks weeks (7 * msg_every_x_weeks)
    return delta_days >= 0 and delta_days % (7 * msg_every_x_weeks) == 0
