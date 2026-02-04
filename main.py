import yfinance as yf
import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1468337671041581168/vII1Ke1qLMf_Cus3D7j51puPUShPTNU574Zs7E5VxmGEIQ4qT5Eyx9KVfHDNCZpcFvvU"

def send_message(message):
    data = {"content": message}
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print("Sent:", message)
    else:
        print("Failed:", response.text)

def get_price(symbol):
    df = yf.download(symbol, period="1d", interval="5m", progress=False)
    if df.empty:
        print(f"No data for {symbol}")
        return None
    # Lấy giá cuối cùng đúng scalar
    return df["Close"].iat[-1]  # iat[-1] trả về scalar float

if __name__ == "__main__":
    btc_price = get_price("BTC-USD")
    if btc_price is not None:
        send_message(f"BTC-USD Price: {btc_price:.2f}")

    spy_price = get_price("SPY")
    if spy_price is not None:
        send_message(f"SPY Price: {spy_price:.2f}")
