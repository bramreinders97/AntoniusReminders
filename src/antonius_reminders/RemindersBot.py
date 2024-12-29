import os
import json
from typing import Optional

import requests

from datetime import datetime
from .Message import Message

def _get_messages_path() -> str:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
    return os.path.join(parent_dir, "messages.json")

class RemindersBot:
    def __init__(self):
        self.BOT_TOKEN = os.getenv("BOT_TOKEN")
        self.CHAT_ID = os.getenv("CHAT_ID")
        self.messages = self._read_messages_info()

    @staticmethod
    def _read_messages_info() -> list[Message]:
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
        # Sending the message
        response = requests.post(
            url=f"https://api.telegram.org/bot{self.BOT_TOKEN}/sendMessage",
            data={
                "chat_id": self.CHAT_ID,
                "text": text
            }
        )

        # Checking the response
        if response.status_code == 200:
            print(f"Message sent successfully for {kind}!")
        else:
            print("Failed to send message:", response.text)

    def send_messages_of_the_day(self, date: Optional[datetime] = datetime.now()) -> None:
        for msg in self.messages:
            if msg.check_if_msg_should_be_sent(date):
                self.send_single_message(text=msg.text, kind=msg.kind)
            else:
                print(f"No need to send msg for reminder on {msg.kind}")
