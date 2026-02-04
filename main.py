import yfinance as yf
import pandas as pd
import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1468337671041581168/vII1Ke1qLMf_Cus3D7j51puPUShPTNU574Zs7E5VxmGEIQ4qT5Eyx9KVfHDNCZpcFvvU"

def send_message(message):
    data = {"content": message}
    res = requests.post(WEBHOOK_URL, json=data)
    if res.status_code == 204:
        print("Sent:", message)
    else:
        print("Failed:", res.text)

def get_price(symbol):
    df = yf.download(symbol, period="1d", interval="5m", progress=False)
    if df.empty:
        return None
    return df["Close"].iloc[-1]

def send_prices():
    # BTC
    btc_price = get_price("BTC-USD")
    if btc_price:
        send_message(f"BTC-USD Price: {btc_price:.2f}")

    # SPY
    spy_price = get_price("SPY")
    if spy_price:
        send_message(f"SPY Price: {spy_price:.2f}")

def check_btc_ema():
    df = yf.download("BTC-USD", period="1d", interval="5m", progress=False)
    if df.empty:
        return

    df["EMA9"] = df["Close"].ewm(span=9).mean()
    df["EMA20"] = df["Close"].ewm(span=20).mean()

    prev = df.iloc[-2]
    last = df.iloc[-1]

    if prev["EMA9"] <= prev["EMA20"] and last["EMA9"] > last["EMA20"]:
        send_message(f"🚨 BTC/USD EMA9 crossed above EMA20! Price: {last['Close']:.2f}")

if __name__ == "__main__":
    send_message("✔ Sends price BTC‑USD - ✔ Sends price SPY - ✔ Then checks BTC EMA crossover → Alert if crossover - Every 5 minutes GitHub Actions runs automatically")
    send_prices()
    check_btc_ema()
