import requests
import json
from pprint import pprint

token = '1693418503:AAEeLQLK2cX7wa93W13sm3ie6ap-7RKU8GI'


def getUpdates():
    url = f'https://api.telegram.org/bot{token}/getUpdates'
    r = requests.get(url)
    data = r.json()
    update = data['result']
    return update

# 563470641


def sendMsg(id):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
        'chat_id': id,
        'text': 'hello'
    }
    r = requests.get(url, payload)


while True:
    sendMsg(563470641)

