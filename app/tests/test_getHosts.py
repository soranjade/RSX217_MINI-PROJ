import requests

url = "http://localhost:8181/onos/v1/hosts"

payload = {}
headers = {
  'Authorization': 'Basic a2FyYWY6a2FyYWY='
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
