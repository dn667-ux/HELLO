import requests
import os

WEBHOOK_URL = os.getenv("https://discord.com/api/webhooks/1468337671041581168/vII1Ke1qLMf_Cus3D7j51puPUShPTNU574Zs7E5VxmGEIQ4qT5Eyx9KVfHDNCZpcFvvU")

if not WEBHOOK_URL:
    raise Exception("DISCORD_WEBHOOK not set")

requests.post(
    WEBHOOK_URL,
    json={"content": "HELLO"}
)

print("Message sent")
