import requests
import pprint
from bson.json_util import dumps
url = ' http://127.0.0.1:5000/setting/tenant/123456'
header = {
    'Content-Type': 'application/json'
}
data = {
    "tenant": "123456"
}

# response = requests.post(url, json=data)
# print(response.json())
response = requests.get(url)
print(response.json())