import os.path
from datetime import datetime

from .send_msg import send_msg
from .check_if_need_msg import is_message_date
import json

# Get path to messages.json
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
file_path = os.path.join(parent_dir, "messages.json")

# Load the JSON file containing message info
with open(file_path, 'r') as file:
    message_data = json.load(file)

# Check if we need to send a message today
# If so, do it
for kind, msg_info in message_data.items():
    if is_message_date(
        check_date_start=datetime(
            msg_info["start_date_year"],
            msg_info["start_date_month"],
            msg_info["start_date_day"],
        ),
        msg_every_x_days=msg_info["msg_every_x_days"]
    ):
        send_msg(
            msg=msg_info["msg"],
            kind=kind
        )
    else:
        print(f"No need to send msg for reminder on {kind}")
