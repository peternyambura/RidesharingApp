import random
import networkx as nx

def generate_random_graph(num_nodes, connectivity):
    G = nx.random_regular_graph(connectivity, num_nodes)
    for edge in G.edges():
        G[edge[0]][edge[1]]['weight'] = random.randint(1, 10)
    return G

def calculate_distance(G, node1, node2):
    return nx.shortest_path_length(G, source=node1, target=node2, weight='weight')

def find_optimal_path(G, start_node, end_node):
    return nx.shortest_path(G, source=start_node, target=end_node, weight='weight')

def is_connected(G):
    return nx.is_connected(G)

def generate_random_pickup_location(G):
    return random.choice(list(G.nodes()))

def generate_random_dropoff_location(G, pickup_node):
    dropoff_node = pickup_node
    while dropoff_node == pickup_node:
        dropoff_node = random.choice(list(G.nodes()))
    return dropoff_node

