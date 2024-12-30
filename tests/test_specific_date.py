"""Check messages specific dates."""

import time
from datetime import datetime
import requests
from tkinter import Tk, Button, Label
from tkcalendar import Calendar
from src.antonius_reminders.AntoniusRemindersBot import AntoniusRemindersBot
from src.antonius_reminders.constants import BOT_TOKEN, CHAT_ID

def send_single_msg(text: str) -> None:
    """Send a single message in telegram."""
    requests.post(
        url=f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": text},
    )

def send_messages_for_dates(selected_dates):
    """Send messages for the selected dates."""
    reminders_bot = AntoniusRemindersBot()
    for date_str in selected_dates:
        test_date = datetime.strptime(date_str, '%Y-%m-%d')
        send_single_msg(text=f"{test_date.strftime('%d %B %Y')}:")
        reminders_bot.send_messages_of_the_day(date=test_date)
        time.sleep(5)  # To avoid too many requests error

def open_calendar():
    """Open a calendar for selecting multiple dates."""
    selected_dates = []

    def on_date_select():
        """Add the selected date to the list."""
        selected_date = calendar.get_date()
        if selected_date not in selected_dates:
            selected_dates.append(selected_date)
            selected_label.config(text=f"Selected Dates: {', '.join(selected_dates)}")

    def on_done():
        """Close the calendar and proceed with sending messages."""
        root.destroy()
        send_messages_for_dates(selected_dates)

    root = Tk()
    root.title("Select Dates")

    Label(root, text="Select dates for sending messages:").pack(pady=10)
    calendar = Calendar(root, selectmode='day', date_pattern='yyyy-MM-dd')
    calendar.pack(pady=10)

    selected_label = Label(root, text="Selected Dates: None")
    selected_label.pack(pady=10)

    Button(root, text="Add Date", command=on_date_select).pack(pady=5)
    Button(root, text="Done", command=on_done).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    open_calendar()
