import requests
import json
from heapq import heapify, heappop, heappush

def get_devices():
    # get all devices on ONOS
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
    # get all links on ONOS
    url = "http://localhost:8181/onos/v1/links"

    payload = {}
    headers = {
    'Authorization': 'Basic a2FyYWY6a2FyYWY='
    }

    response = requests.request("GET", url, headers=headers, data=payload, timeout=10)
    response_json = json.loads(response.content)
    
    return response_json['links']

def get_hosts():
    # get all hosts(pc) on ONOS
    url = "http://localhost:8181/onos/v1/hosts"

    payload = {}
    headers = {
    'Authorization': 'Basic a2FyYWY6a2FyYWY='
    }

    response = requests.request("GET", url, headers=headers, data=payload, timeout=10)
    response_json = json.loads(response.content)
    
    return response_json['hosts']

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
    
    def shortest_path(self, source: str, target: str):
        # Generate the predecessors dict
        _, predecessors = self.shortest_distances(source)

        path = []
        current_node = target

        # Backtrack from the target node using predecessors
        while current_node:
            path.append(current_node)
            current_node = predecessors[current_node]

        # Reverse the path and return it
        path.reverse()

        return path

class NodeLink:
    def __init__(self, table = {}):
        self.table = table
        
    def add_NL(self, NL1, NL2, port, type):
        if NL1 not in self.table:  # Check if the node is already added
            self.table[NL1] = {}  # If not, create the node
            self.table[NL1]["type"] = type
        self.table[NL1][NL2] = port
    
    def links_to_NL(self, links):
        # translate ONOS LINKS into EDGE for the graph
        for link in links:
            # add a node in/on the graphe
            self.add_NL(link['src']['device'], link['dst']['device'], link['src']['port'], "switch")
    def hosts_to_NL(self, hosts):
        # translate ONOS LINKS into EDGE for the graph
        for host in hosts:
            # add a node in/on the graphe
            self.add_NL(host['mac'], host['locations'][0]['elementId'], host['locations'][0]['port'], "host")


# { src { port, device }, dst { port, device} }
links = get_links()
'''
for link in links:
    print(link)
'''
# {id,mac,locations[{elementId, port}]}
hosts = get_hosts()

'''
for host in hosts:
    print(host['mac'])
    print(host['locations'][0]['elementId'])
    print(host['locations'][0]['port'])
    '''

nodelink = NodeLink()
nodelink.links_to_NL(links)
nodelink.hosts_to_NL(hosts)
# result json state of nodelink in json_result/nodelink.json
#print(json.dumps(nodelink.table))

# Create the dij graph
G = Graph()
# Convert ONOS links into edge for the graphe
G.links_to_edge(links)
'''
Samples tests to define the shortest path in numerical way
distances_e1, pred_e1 = G.shortest_distances("of:00000000000000e1")
distances_e2 = G.shortest_distances("of:00000000000000e2")
distances_e3 = G.shortest_distances("of:00000000000000e3")
distances_e4 = G.shortest_distances("of:00000000000000e4")
distances_c1 = G.shortest_distances("of:00000000000000c1")
distances_c2 = G.shortest_distances("of:00000000000000c2")
distances_c3 = G.shortest_distances("of:00000000000000c3")
distances_c4 = G.shortest_distances("of:00000000000000c4")'''

# Example of the shortest path between two nodes E1 -> E3
print("path e1 -> e3 : " + str(G.shortest_path("of:00000000000000e1","of:00000000000000e3")))
