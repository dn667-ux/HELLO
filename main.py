import requests

# Dùng trực tiếp webhook bạn cung cấp
WEBHOOK_URL = "https://discord.com/api/webhooks/1468337671041581168/vII1Ke1qLMf_Cus3D7j51puPUShPTNU574Zs7E5VxmGEIQ4qT5Eyx9KVfHDNCZpcFvvU"

def send_message():
    data = {
        "content": "HELLO, testing"
    }
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print("Message sent successfully!")
    else:
        print("Failed to send message:", response.text)

if __name__ == "__main__":
    send_message()
