"""Message classes."""

from datetime import datetime

import requests

from src.antonius_reminders.constants import BOT_TOKEN, CHAT_ID


class Message:
    """Base class for messages."""

    def __init__(self, start_date: datetime, msg_every_x_days: int, kind: str) -> None:
        """Initializes a Message object.

        Args:
            start_date (datetime): The start date for the message.
            msg_every_x_days (int): Frequency in days to send the message.
            kind (str): A label describing the type of the message.
        """
        self.start_date = start_date
        self.msg_every_x_days = msg_every_x_days
        self.kind = kind

    def check_if_should_be_sent(self, date: datetime) -> bool:
        """Determines if the message should be sent on the specified date.

        Args:
            date (datetime): The current date to check.

        Returns:
            bool: True if the message should be sent, False otherwise.
        """
        delta_days = (date - self.start_date).days
        return delta_days >= 0 and delta_days % self.msg_every_x_days == 0

    def _send(self, api_method: str, data: dict) -> None:
        """Sends the message using a specified Telegram API method.

        Args:
            api_method (str): The Telegram API method to use for sending.
            data (dict): The payload to send to the API.
        """
        response = requests.post(
            url=f"https://api.telegram.org/bot{BOT_TOKEN}/{api_method}", data=data
        )

        if response.status_code == 200:
            print(f"Message sent successfully for {self.kind}!")
        else:
            print("Failed to send message:", response.text)


class TextMessage(Message):
    """A text-based message."""

    def __init__(
        self, start_date: datetime, msg_every_x_days: int, kind: str, msg: str
    ) -> None:
        """Initializes a TextMessage object.

        Args:
            start_date (datetime): The start date for the message.
            msg_every_x_days (int): Frequency in days to send the message.
            kind (str): A label describing the type of the message.
            msg (str): The text content of the message.
        """
        super().__init__(start_date, msg_every_x_days, kind)
        self.msg = msg

    def send(self) -> None:
        """Sends the text message."""
        data = {"chat_id": CHAT_ID, "text": self.msg}
        super()._send("sendMessage", data)


class Gif(Message):
    """A GIF-based message."""

    def __init__(
        self, start_date: datetime, msg_every_x_days: int, kind: str, url: str
    ) -> None:
        """Initializes a Gif object.

        Args:
            start_date (datetime): The start date for the message.
            msg_every_x_days (int): Frequency in days to send the message.
            kind (str): A label describing the type of the message.
            url (str): The URL of the GIF.
        """
        super().__init__(start_date, msg_every_x_days, kind)
        self.url = url

    def send(self) -> None:
        """Sends the GIF message."""
        data = {"chat_id": CHAT_ID, "animation": self.url}
        super()._send("sendAnimation", data)
