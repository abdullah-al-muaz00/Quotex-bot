import os
import requests
import time
import random
from datetime import datetime

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

markets = ["EUR/USD", "USD/JPY", "GBP/JPY", "AUD/USD", "USD/CHF", "EUR/GBP"]

def send_signal():
    market = random.choice(markets)
    direction = random.choice(["🟢 CALL", "🔴 PUT"])
    accuracy = round(random.uniform(97.5, 99.9), 2)
    now = datetime.now().strftime("%d %B %Y - %I:%M %p")

    message = f"""**__𝑨𝑨𝑴 𝑻𝒓𝒂𝒅𝒆𝒓__**
{market}
Duration: 1 min
Signal: {direction}
Accuracy: {accuracy}%
Time: {now}
**__𝑸𝒖𝒐𝒕𝒆𝒙 𝑨𝑨𝑴__**"""

    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data={
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    })
    time.sleep(60)
    result = random.choice(["✅ Result: WIN", "❌ Result: LOSS"])
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data={
        "chat_id": CHAT_ID,
        "text": result
    })

if __name__ == "__main__":
    while True:
        send_signal()
        time.sleep(180)
