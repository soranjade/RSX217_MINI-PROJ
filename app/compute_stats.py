import requests
import json
from pathlib import Path


def get_stats():
    # get stats on ONOS
    url = "http://localhost:8181/onos/v1/statistics/delta/ports"

    payload = {}
    headers = {
    'Authorization': 'Basic a2FyYWY6a2FyYWY='
    }

    response = requests.request("GET", url, headers=headers, data=payload, timeout=10)

    stats = json.loads(response.content)
    
    return stats["statistics"]

def better_stats(stats):
    # Convert STATS into BETTER_STATS for better programs
    # Sample result in json_result/better_stats.json
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
            
    return better_stats

stats = better_stats(get_stats())
Path('stats.json').write_text(json.dumps(stats, indent=4, sort_keys=True))
        
    
