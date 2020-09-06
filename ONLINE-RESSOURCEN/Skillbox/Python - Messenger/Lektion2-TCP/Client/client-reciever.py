import time
from datetime import datetime

import requests

last_time = 0

while True:
    response = requests.get("http://localhost:5000/messages",
                            params={'after': last_time})  # => http://localhost:5000/messages?after=xxxx
    messages = response.json()["messages"]
    for message in messages:
        beatity_time = datetime.fromtimestamp(message["time"])
        beatity_time = beatity_time.strftime('%d/%m/%Y %H:%M:%S')
        print(message["username"], beatity_time)
        print(message["text"])

        last_time = message['time']

    time.sleep(1)
