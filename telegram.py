import requests
import os

# Replace with your Bot Token
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Replace with your Chat ID
CHAT_ID = os.getenv('CHAT_ID')

if BOT_TOKEN is None:
    print('BOT_TOKEN not set')

# Message to send
MESSAGE = "Hello, this is a message from my Python script!"

# Telegram API URL
URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# Sending the message
response = requests.post(URL, data={
    "chat_id": CHAT_ID,
    "text": MESSAGE
})

# Checking the response
if response.status_code == 200:
    print("Message sent successfully!")
else:
    print("Failed to send message:", response.text)
