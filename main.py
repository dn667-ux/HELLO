import yfinance as yf
import pandas as pd
import requests
import time

WEBHOOK_URL = "https://discord.com/api/webhooks/1468337671041581168/vII1Ke1qLMf_Cus3D7j51puPUShPTNU574Zs7E5VxmGEIQ4qT5Eyx9KVfHDNCZpcFvvU"

SYMBOL = "BTC-USD"
INTERVAL = "5m"
LOOKBACK = "1d"

def send_message(message):
    """Gửi tin nhắn tới Discord"""
    data = {"content": message}
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print("Message sent:", message)
    else:
        print("Failed to send message:", response.text)

def send_initial_note():
    """Gửi note ban đầu 1 lần"""
    note = "HELLO, testing. Auto scan, auto send, repeat 5m, BTC/USD EMA9 crossed above EMA20! Price"
    send_message(note)

def check_ema():
    """Kiểm tra EMA9 cắt EMA20"""
    df = yf.download(SYMBOL, period=LOOKBACK, interval=INTERVAL, progress=False)
    if df.empty:
        print("No data received")
        return

    df["EMA9"] = df["Close"].ewm(span=9).mean()
    df["EMA20"] = df["Close"].ewm(span=20).mean()

    prev = df.iloc[-2]
    last = df.iloc[-1]

    if prev["EMA9"] <= prev["EMA20"] and last["EMA9"] > last["EMA20"]:
        price = last["Close"]
        message = f"🚨 BTC/USD EMA9 crossed above EMA20! Price: {price:.2f}"
        send_message(message)
    else:
        print("No crossover detected")

if __name__ == "__main__":
    # Gửi note đầu tiên
    send_initial_note()
    # Kiểm tra EMA
    check_ema()
