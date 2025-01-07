import requests

intentID = "0x1e"

url = "http://localhost:8181/onos/v1/intents/org.onosproject.ovsdb/" + intentID

payload = {}
headers = {
  'Authorization': 'Basic a2FyYWY6a2FyYWY='
}

response = requests.request("DELETE", url, headers=headers, data=payload, timeout=10)

print(response.status_code)
