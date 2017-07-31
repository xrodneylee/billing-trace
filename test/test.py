import requests
import pprint

url = ' http://127.0.0.1:5000/setting/tenant'
header = {
    'Content-Type': 'application/json'
}
data = {
    "tenant": "7777",
    "client_id": "123",
    "client_secret": "555abcccc"
}

response = requests.put(url, json=data)
print(response.json())
response = requests.get(url)
print(response.json())