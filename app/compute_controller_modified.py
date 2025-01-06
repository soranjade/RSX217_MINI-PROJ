import requests
import json
from heapq import heapify, heappop, heappush

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
    
    return response_json['links']

class Graph:
    
    def __init__(self, graph={}):
        self.graph = graph  # A dictionary for the adjacency list
        self.key = "id"

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:  # Check if the node is already added
            self.graph[node1] = {}  # If not, create the node
        self.graph[node1][node2] = weight
        
    def links_to_edge(self, links):
        # translate ONOS LINKS into EDGE for the graph
        for link in links:
            # add a node in/on the graphe
            self.add_edge(link['src']['device'], link['dst']['device'], 1)
    
    def shortest_distances(self, source: str):
       # Initialize the values of all nodes with infinity
        distances = {node: float("inf") for node in self.graph}
        distances[source] = 0  # Set the source value to 0
       
        pq = [(0, source)]
        heapify(pq)
       
        visited = set()
        while pq:  # While the priority queue isn't empty
            current_distance, current_node = heappop(pq)

            if current_node in visited:
                continue 
            visited.add(current_node)

            for neighbor, weight in self.graph[current_node].items():
            # Calculate the distance from current_node to the neighbor
                tentative_distance = current_distance + weight
                if tentative_distance < distances[neighbor]:
                    distances[neighbor] = tentative_distance
                    heappush(pq, (tentative_distance, neighbor))
    
        predecessors = {node: None for node in self.graph}

        for node, distance in distances.items():
            for neighbor, weight in self.graph[node].items():
                if distances[neighbor] == distance + weight:
                    predecessors[neighbor] = node

        return distances, predecessors

              
devices = get_devices()
links = get_links()
    
G = Graph()

G.links_to_edge(links)

distances_e1, pred_e1 = G.shortest_distances("of:00000000000000e1")
distances_e2 = G.shortest_distances("of:00000000000000e2")
distances_e3 = G.shortest_distances("of:00000000000000e3")
distances_e4 = G.shortest_distances("of:00000000000000e4")
distances_c1 = G.shortest_distances("of:00000000000000c1")
distances_c2 = G.shortest_distances("of:00000000000000c2")
distances_c3 = G.shortest_distances("of:00000000000000c3")
distances_c4 = G.shortest_distances("of:00000000000000c4")

print(pred_e1, "\n")
