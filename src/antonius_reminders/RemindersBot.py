import os
import json
from typing import Optional
import requests
from datetime import datetime
from .Message import Message


def _get_messages_path() -> str:
    """
    Determines the path to the messages.json file.

    Returns:
        str: The absolute path to the messages.json file.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
    return os.path.join(parent_dir, "messages.json")


class RemindersBot:
    """
    A bot to manage and send scheduled reminder messages.

    Attributes:
        BOT_TOKEN (str): The Telegram bot token from environment variables.
        CHAT_ID (str): The chat ID to send messages to from environment variables.
        messages (List[Message]): A list of messages to be managed by the bot.
    """

    def __init__(self):
        """
        Initializes the RemindersBot by loading environment variables and messages.
        """
        self.BOT_TOKEN = os.getenv("BOT_TOKEN")
        self.CHAT_ID = os.getenv("CHAT_ID")
        self.messages = self._read_messages_info()

    @staticmethod
    def _read_messages_info() -> list[Message]:
        """
        Reads message details from the messages.json file.

        Returns:
            List[Message]: A list of Message objects created from the file data.
        """
        with open(_get_messages_path(), 'r') as file:
            message_data = json.load(file)

        messages = []
        for kind, msg_info in message_data.items():
            messages.append(Message(
                text=msg_info["msg"],
                start_date=datetime(
                    msg_info["start_date_year"],
                    msg_info["start_date_month"],
                    msg_info["start_date_day"],
                ),
                msg_every_x_days=msg_info["msg_every_x_days"],
                kind=kind,
            ))

        return messages

    def send_single_message(self, text: str, kind: str) -> None:
        """
        Sends a single message using the Telegram API.

        Args:
            text (str): The message content.
            kind (str): The type of the message.
        """
        response = requests.post(
            url=f"https://api.telegram.org/bot{self.BOT_TOKEN}/sendMessage",
            data={
                "chat_id": self.CHAT_ID,
                "text": text
            }
        )

        if response.status_code == 200:
            print(f"Message sent successfully for {kind}!")
        else:
            print("Failed to send message:", response.text)

    def send_messages_of_the_day(self, date: Optional[datetime] = datetime.now()) -> None:
        """
        Sends messages scheduled for the current day.

        Args:
            date (Optional[datetime]): The date to check for sending messages.
                                       Defaults to the current date.
        """
        for msg in self.messages:
            if msg.check_if_msg_should_be_sent(date):
                self.send_single_message(text=msg.text, kind=msg.kind)
            else:
                print(f"No need to send msg for reminder on {msg.kind}")
