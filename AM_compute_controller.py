import requests
import json


def get_devices():
    
    url = "http://localhost:8181/onos/v1/devices"

    payload = {}
    headers = {
    'Authorization': 'Basic a2FyYWY6a2FyYWY='
    }

    response = requests.request("GET", url, headers=headers, data=payload, timeout=10)
    response_json = json.loads(response.content)

    # print(response_json['devices'])

    #for device in response_json['devices']:
    #    print(device['id'])
        
    return response_json['devices']

def get_links():
    url = "http://localhost:8181/onos/v1/links"

    payload = {}
    headers = {
    'Authorization': 'Basic a2FyYWY6a2FyYWY='
    }

    response = requests.request("GET", url, headers=headers, data=payload, timeout=10)
    response_json = json.loads(response.content)

    # print(response_json['devices'])

    #for link in response_json['links']:
    #    print(link)
    return response_json['links']

class Node:
    def __init__(self, id):
        self.id = id
        self.neighbors = []
    
    def add_neighbor(self):
        pass
    
            

    
class Graph:
    def __init__(self, graph: dict = {}):
        self.graph = graph  # A dictionary for the adjacency list

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:  # Check if the node is already added
            self.graph[node1] = {}  # If not, create the node
        self.graph[node1][node2] = weight  # Else, add a connection to its neighbor
        
    def links_to_neighbors(self, links):
        for link in links:
            self.add_edge(link['src']['device'], link['dst']['device'], 1)

devices = get_devices()
links = get_links()

#for link in links:
#    print(link)
    
G = Graph()

G.links_to_neighbors(links)

for node in G.graph.items():
    print(node)

'''print(json.dumps(devices))
print(json.dumps(links))'''