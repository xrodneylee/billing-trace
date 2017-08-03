import requests
import pprint
import json

url = ' http://127.0.0.1:5000/setting/group'
header = {
    'Content-Type': 'application/json'
}
# data = {
#     "tenant": "aaa",
#     "client_id": "sss",
#     "client_secret": "fff"
# }

data = {
    "groupName": "guanpu",
    "subscriptions": [
        {"subscription" : "subscription1"},
        {"subscription" : "subscription2"}
    ]
}

response = requests.post(url, json=json.dumps(data))
print(response.json())
# response = requests.get(url)
# print(response.json())
# response = requests.delete(url)
# print(response.json())