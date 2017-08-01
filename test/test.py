import requests
import pprint

url = ' http://127.0.0.1:5000/setting/subscription'
header = {
    'Content-Type': 'application/json'
}
data = {
    "tenant": "",
    "client_id": "",
    "client_secret": ""
}

response = requests.post(url, json=data)
print(response.json())
# response = requests.get(url)
# print(response.json())
# response = requests.delete(url)
# print(response.json())