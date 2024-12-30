"""Send the messages that we expect in the next 30 days for testing purposes."""

import time
import requests
from datetime import datetime, timedelta

from src.antonius_reminders.AntoniusRemindersBot import AntoniusRemindersBot
from src.antonius_reminders.constants import BOT_TOKEN, CHAT_ID

def send_single_msg(text):
    requests.post(
        url=f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": text
        }
    )


today = datetime.now()
reminders_bot = AntoniusRemindersBot()

# For the next 30 days, send the messages we expect to send
for day_offset in range(31):
    test_date = today + timedelta(days=day_offset)
    send_single_msg(
        text=f"{test_date.strftime("%d %B %Y")}:"
    )
    reminders_bot.send_messages_of_the_day(date=test_date)
    time.sleep(5) # To avoid too many requests error
