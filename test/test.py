import requests

url = ' http://127.0.0.1:5000/setting/tenant'
header = {
    'Content-Type': 'application/json'
}
data = {
    "id": 123,
    "tenant": "qq"
}

response = requests.post(url, json=data)
print(response.text)