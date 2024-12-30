"""Functionality running in production."""

from .AntoniusRemindersBot import AntoniusRemindersBot

# Initialize the RemindersBot instance
reminders_bot = AntoniusRemindersBot()

# Send messages of the day if applicable
reminders_bot.send_messages_of_the_day()
