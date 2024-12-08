import requests
import os

# Replace with your Bot Token
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Telegram API URL
URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

def send_msg(msg: str, kind: str):
    # Sending the message
    response = requests.post(URL, data={
        "chat_id": os.getenv('CHAT_ID'),
        "text": msg
    })

    # Checking the response
    if response.status_code == 200:
        print(f"Message sent successfully for {kind}!")
    else:
        print("Failed to send message:", response.text)
