import requests

url = ' http://127.0.0.1:5000/setting/tenant'
header = {
    'Content-Type': 'application/json'
}
data = {
    "tenant": "123456"
}

response = requests.post(url, json=data)
print(response.text)