import requests
import os

URL = "http://ww1.vlsi-backend-adventure.com/"

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def is_live():
    try:
        r = requests.get(URL, timeout=10)
        return r.status_code == 200 and "VLSI" in r.text
    except:
        return False

def send_telegram():
    message = "🚀 VLSI Backend Adventure is LIVE!\n" + URL
    send_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(send_url, data={
        "chat_id": CHAT_ID,
        "text": message
    })

if is_live():
    send_telegram()


