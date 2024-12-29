from datetime import datetime


class Message:
    """
    Represents a reminder message with details about its schedule and type.

    Attributes:
        text (str): The content of the message.
        start_date (datetime): The date from which the reminder starts.
        msg_every_x_days (int): The interval in days for the reminder.
        kind (str): The type or category of the reminder.
    """

    def __init__(self, text: str, start_date: datetime, msg_every_x_days: int, kind: str) -> None:
        """
        Initializes a Message object.

        Args:
            text (str): The message content.
            start_date (datetime): The starting date of the message schedule.
            msg_every_x_days (int): The interval between messages in days.
            kind (str): The type of the message.
        """
        self.text = text
        self.start_date = start_date
        self.msg_every_x_days = msg_every_x_days
        self.kind = kind

    def check_if_msg_should_be_sent(self, date: datetime) -> bool:
        """
        Determines if the message should be sent on the specified date.

        Args:
            date (datetime): The current date to check.

        Returns:
            bool: True if the message should be sent, False otherwise.
        """
        delta_days = (date - self.start_date).days
        return delta_days >= 0 and delta_days % self.msg_every_x_days == 0
