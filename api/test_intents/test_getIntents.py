import requests

url = "http://localhost:8181/onos/v1/intents"

payload = {}
headers = {
  'Authorization': 'Basic a2FyYWY6a2FyYWY='
}

response = requests.request("GET", url, headers=headers, data=payload, timeout=10)

print(response.text)
