"""AntoniusRemindersBot class."""

import json
import os
import time
from datetime import datetime
from typing import Literal, Optional, Union

from .Messages import Gif, TextMessage


def _get_messages_path(filename: str) -> str:
    """Determines the path to the json file containing the data of the messages.

    Args:
        filename (str): The base name of the JSON file without extension.

    Returns:
        str: The absolute path to the JSON file.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
    return os.path.join(parent_dir, "messages", f"{filename}.json")


class AntoniusRemindersBot:
    """A bot for managing and sending reminder messages."""

    def __init__(self) -> None:
        """Initializes AntoniusRemindersBot with text and GIF messages."""
        self.text_messages = self._read_json_info(message_type="text_messages")
        self.gifs = self._read_json_info(message_type="gifs")
        self.all_messages = self.text_messages + self.gifs

    @staticmethod
    def _read_json_info(
        message_type: Literal["text_messages", "gifs"]
    ) -> list[Union[TextMessage, Gif]]:
        """Reads message information from a JSON file and returns it as objects.

        Args:
            message_type (Literal["text_messages", "gifs"]): The type of messages to read.
                Must be either "text_messages" or "gifs".

        Returns:
            list[Union[TextMessage, Gif]]: A list of message objects corresponding to the specified type.
        """
        with open(_get_messages_path(message_type), "r") as file:
            message_data = json.load(file)

        messages = []
        for kind, msg_info in message_data.items():
            if message_type == "text_messages":
                messages.append(
                    TextMessage(
                        start_date=datetime(
                            msg_info["start_date_year"],
                            msg_info["start_date_month"],
                            msg_info["start_date_day"],
                        ),
                        msg_every_x_days=msg_info["msg_every_x_days"],
                        kind=kind,
                        msg=msg_info["msg"],
                        chat_name=msg_info["chat_name"],
                    )
                )
            elif message_type == "gifs":
                messages.append(
                    Gif(
                        start_date=datetime(
                            msg_info["start_date_year"],
                            msg_info["start_date_month"],
                            msg_info["start_date_day"],
                        ),
                        msg_every_x_days=msg_info["msg_every_x_days"],
                        kind=kind,
                        url=msg_info["url"],
                        chat_name=msg_info["chat_name"],
                    )
                )
        return messages

    def send_messages_of_the_day(
        self, date: Optional[datetime] = datetime.now()
    ) -> None:
        """Sends messages scheduled for a given date.

        Args:
            date (Optional[datetime]): The target date for sending messages. Defaults to the current date.
        """
        for msg in self.all_messages:
            if msg.check_if_should_be_sent(date):
                msg.send()
                time.sleep(5)  # Avoid too many requests error
            else:
                print(f"No need to send msg for reminder on {msg.kind}")
