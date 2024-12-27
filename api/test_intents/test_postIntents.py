import requests
import json

url = "http://localhost:8181/onos/v1/intents"

hostSRC = "D6:25:7C:E3:71:89/-1"
hostDST = "56:CB:3C:C4:EE:01/-1"

payload = json.dumps({
  "type": "HostToHostIntent",
  "appId": "org.onosproject.ovsdb",
  "one": hostSRC,
  "two": hostDST
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic a2FyYWY6a2FyYWY='
}

response = requests.request("POST", url, headers=headers, data=payload, timeout=10)

print(response.status_code)
