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
    "subscriptions": ["coffee", "tea", "water"]
}
# data = '{"groupName": "guanpu", "subscriptions": ["coffee", "tea", "water"]}'
# print(json.loads(data))
# response = requests.post(url, headers=header, json=data)
response = requests.get(url)
print(response.json())
# response = requests.get(url)
# print(response.json())
# response = requests.delete(url)
# print(response.json())