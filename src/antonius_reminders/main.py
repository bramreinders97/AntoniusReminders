from .RemindersBot import RemindersBot

# Initialize the RemindersBot instance
reminders_bot = RemindersBot()

# Send messages of the day if applicable
reminders_bot.send_messages_of_the_day()
