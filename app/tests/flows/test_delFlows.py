import requests

url = "http://localhost:8181/onos/v1/flows/application/dijto"

payload = {}
headers = {
  'Authorization': 'Basic a2FyYWY6a2FyYWY='
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.status_code)
