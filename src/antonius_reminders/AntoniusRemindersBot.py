import os
import json
from typing import Optional, Union
from datetime import datetime
from .Messages import TextMessage, Gif


def _get_messages_path(filename: str) -> str:
    """
    Determines the path to the messages.json file.

    Returns:
        str: The absolute path to the messages.json file.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
    return os.path.join(parent_dir, "messages",  f"{filename}.json")


class AntoniusRemindersBot:

    def __init__(self):
        """
        Initializes the RemindersBot by loading environment variables and messages.
        """
        self.text_messages = self._read_json_info(message_type='text_messages')
        self.gifs = self._read_json_info(message_type='gifs')
        self.all_messages = self.text_messages + self.gifs

    @staticmethod
    def _read_json_info(message_type: str) -> list[Union[TextMessage, Gif]]:
        with open(_get_messages_path(message_type), 'r') as file:
            message_data = json.load(file)

        messages = []
        for kind, msg_info in message_data.items():
            if message_type == 'text_messages':
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
                    )
                )
            elif message_type == 'gifs':
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
                    )
                )

        return messages




    def send_messages_of_the_day(self, date: Optional[datetime] = datetime.now()) -> None:
        for msg in self.all_messages:
            if msg.check_if_should_be_sent(date):
                msg.send()
            else:
                print(f"No need to send msg for reminder on {msg.kind}")

