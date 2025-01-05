import requests
import json
url = "http://localhost:8181/onos/v1/statistics/delta/ports"

payload = {}
headers = {
  'Authorization': 'Basic a2FyYWY6a2FyYWY='
}

response = requests.request("GET", url, headers=headers, data=payload, timeout=10)

#stats = json.loads(response.content)
print(json.loads(response.content))

