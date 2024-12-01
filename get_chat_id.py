import os

import requests

BOT_TOKEN = os.getenv('BOT_TOKEN')
URL = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"

response = requests.get(URL)
if response.status_code == 200:
    print(response.json())
else:
    print("Failed to fetch updates:", response.text)
