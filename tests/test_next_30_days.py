"""Send the messages that we expect in the next 30 days for testing purposes."""

import time

from datetime import datetime, timedelta

from src.antonius_reminders.RemindersBot import RemindersBot


today = datetime.now()
reminders_bot = RemindersBot()

# For the next 30 days, send the messages we expect to send
for day_offset in range(31):
    test_date = today + timedelta(days=day_offset)
    reminders_bot.send_single_message(
        text=f"{test_date.strftime("%d %B %Y")}:", kind="testing"
    )
    reminders_bot.send_messages_of_the_day(date=test_date)
    time.sleep(5) # To avoid too many requests error
