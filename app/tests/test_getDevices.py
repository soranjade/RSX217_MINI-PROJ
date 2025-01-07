import requests
import json

url = "http://localhost:8181/onos/v1/devices"

payload = {}
headers = {
  'Authorization': 'Basic a2FyYWY6a2FyYWY='
}

response = requests.request("GET", url, headers=headers, data=payload, timeout=10)
response_json = json.loads(response.content)

print(response_json['devices'])

for device in response_json['devices']:
  print(device['id'])

