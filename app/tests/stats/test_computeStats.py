import requests
import json

def get_stats():
    url = "http://localhost:8181/onos/v1/statistics/delta/ports"

    payload = {}
    headers = {
    'Authorization': 'Basic a2FyYWY6a2FyYWY='
    }

    response = requests.request("GET", url, headers=headers, data=payload, timeout=10)

    stats = json.loads(response.content)
    
    return stats["statistics"]



stats = get_stats()

better_stats = {}

for stat in stats:
    device = stat["device"]
    if device not in better_stats:
        better_stats[device] = {}
    
    for port in stat["ports"]:
        port_number = str(port["port"])
        bits_in = port["bytesReceived"] * 8
        bits_out = port["bytesSent"] * 8
        
        if port["bytesReceived"] > 0:
            bits_in = round(port["bytesReceived"] * 8 / port["durationSec"] / 1000000)
        if port["bytesSent"] > 0:
            bits_out = round(port["bytesSent"] * 8 / port["durationSec"] / 1000000)
        
        better_stats[device][port_number] = {}
        better_stats[device][port_number]["Mbits_in"] = bits_in
        better_stats[device][port_number]["Mbits_out"] = bits_out
    
print(json.dumps(better_stats))