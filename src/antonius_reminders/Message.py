from datetime import datetime


class Message:
    def __init__(self, text: str, start_date: datetime, msg_every_x_days: int, kind: str) -> None:
        self.text = text
        self.start_date = start_date
        self.msg_every_x_days = msg_every_x_days
        self.kind = kind

    def check_if_msg_should_be_sent(self, date: datetime) -> bool:
        # Calculate the difference in days between the current date and the start date
        delta_days = (date - self.start_date).days

        # Check if the difference in days is a multiple of msg_every_x_days
        return delta_days >= 0 and delta_days % self.msg_every_x_days == 0