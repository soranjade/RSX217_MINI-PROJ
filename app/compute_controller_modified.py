import requests
import json
from pathlib import Path
from heapq import heapify, heappop, heappush

def path_between_hosts(h1,h2,dij_graph,nodelink_table):
    first_node = nodelink_table[h1]
    pass
    

def post_flow(appId,payload):
    # post the flow without intelligence with an appId
    url = "http://localhost:8181/onos/v1/flows?appId="+appId
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic a2FyYWY6a2FyYWY='
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    #print(response.text)
    
def rule_to_flow(device_id, port_in, port_out, mac_src, mac_dst):
    # take the rule and convert it into a statefull flow with a txt template file
    template = Path('template/flow.json').read_text()
    template = template.replace("__DEVICE_ID__", device_id)
    template = template.replace("__PORT_IN__", port_in)
    template = template.replace("__PORT_OUT__", port_out)
    template = template.replace("__MAC_DST__", mac_dst)
    template = template.replace("__MAC_SRC__", mac_src)

    return template
    
def get_devices():
    # get all devices on ONOS, return JSON
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
    # get all links on ONOS, return JSON
    url = "http://localhost:8181/onos/v1/links"

    payload = {}
    headers = {
    'Authorization': 'Basic a2FyYWY6a2FyYWY='
    }

    response = requests.request("GET", url, headers=headers, data=payload, timeout=10)
    response_json = json.loads(response.content)
    
    return response_json['links']

def get_hosts():
    # get all hosts(pc) on ONOS, return JSON
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
    def __init__(self, table = {}, hosts = {}):
        self.table = table
        
    def add_NL(self, NL1, NL2, port, type):
        if NL1 not in self.table:  # Check if the node is already added
            self.table[NL1] = {}  # If not, create the node
            self.table[NL1]["type"] = type
        if type == "switch":
            self.table[NL1][NL2] = port
        if type == "host":
            self.table[NL1]["switch"] = NL2
            self.table[NL1]["switch_port"] = port
    
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
    print(link)'''

# {id,mac,locations[{elementId, port}]}
hosts = get_hosts()

'''
for host in hosts:
    print(host['mac'])
    print(host['locations'][0]['elementId'])
    print(host['locations'][0]['port'])'''
    

nodelink = NodeLink()
nodelink.links_to_NL(links)
#print(nodelink)
nodelink.hosts_to_NL(hosts)
# result json state of nodelink in json_result/nodelink.json
#print(json.dumps(nodelink.table))

# Create the dij graph
G = Graph()
# Convert ONOS links into edge for the graphe
G.links_to_edge(links)
#print(json.dumps(G.graph))
'''
#Samples tests to define the shortest path in numerical way
distances_e1, pred_e1 = G.shortest_distances("of:00000000000000e1")
distances_e2 = G.shortest_distances("of:00000000000000e2")
distances_e3 = G.shortest_distances("of:00000000000000e3")
distances_e4 = G.shortest_distances("of:00000000000000e4")
distances_c1 = G.shortest_distances("of:00000000000000c1")
distances_c2 = G.shortest_distances("of:00000000000000c2")
distances_c3 = G.shortest_distances("of:00000000000000c3")
distances_c4 = G.shortest_distances("of:00000000000000c4")'''

#print(distances_e1)
# Example of the shortest path between two nodes E1 -> E3
#print("path e1 -> e3 : " + str(G.shortest_path("of:00000000000000e1","of:00000000000000e2")))

#print(hosts)
# HOST TO HOST

h1 = "00:00:00:00:00:01"
h2 = "00:00:00:00:00:05"


switch_h1 = nodelink.table[h1]["switch"]
switch_port_h1 = nodelink.table[h1]["switch_port"]

switch_h2 = nodelink.table[h2]["switch"]
switch_port_h2 = nodelink.table[h2]["switch_port"]

better_stats = json.loads(Path("stats.json").read_text())
h1_cost_out = better_stats[switch_h1][switch_port_h1]["Mbits_in"]
h2_cost_out = better_stats[switch_h2][switch_port_h2]["Mbits_in"]

print("h1 cost : " + str(h1_cost_out))
print("h2 cost : " + str(h2_cost_out))

# GET THE HOST SWITCH CONNECTION
first_node = nodelink.table[h1]["switch"]
last_node = nodelink.table[h2]["switch"]
first_node_port = nodelink.table[h1]["switch_port"]
last_node_port = nodelink.table[h2]["switch_port"]

nodepath = G.shortest_path(first_node,last_node)
nodepath = json.loads(json.dumps(nodepath))
print(nodepath)

for node in nodepath:
    index = nodepath.index(node)
    node_id = node
    mac_src = h1
    mac_dst = h2
    
    if index == 0:
        # first node treatment
        port_in = first_node_port
        port_out = nodelink.table[node][nodepath[index+1]]
        
    elif index == len(nodepath) -1:
        # last node treatment
        port_in = nodelink.table[node][nodepath[index-1]]
        port_out = last_node_port
        
    else:
        # node between first and last
        port_in = nodelink.table[node][nodepath[index-1]]
        port_out = nodelink.table[node][nodepath[index+1]]
        
    print(node_id + ", " + port_in + ", " + port_out +", " + mac_src + ", " + mac_dst)
    post_flow("dijto", json.dumps(json.loads(rule_to_flow(node_id, port_in, port_out, mac_src, mac_dst))))
    
#print("path e1 -> e3 : " + str(nodepath))
'''

flows = [ 
         ["of:00000000000000e1", "1", "3", "00:00:00:00:00:01", "00:00:00:00:00:03"],
         ["of:00000000000000c1", "3", "4", "00:00:00:00:00:01", "00:00:00:00:00:03"],
         ["of:00000000000000e2", "3", "1", "00:00:00:00:00:01", "00:00:00:00:00:03"],
    ]


for flow in flows :
    #print(flow)
    device_id, port_in, port_out, mac_src, mac_dst = flow
    post_flow("dijto", json.dumps(json.loads(rule_to_flow(device_id, port_in, port_out, mac_src, mac_dst))))'''


