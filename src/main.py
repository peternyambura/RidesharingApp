import random
import networkx as nx
from rideshare import RideshareSimulator

def main():
    num_nodes = 100
    connectivity = 3
    num_vans = 30

    G = generate_random_graph(num_nodes, connectivity)

    pickup_requests = generate_pickup_requests(num_nodes, 600)

    simulator = RideshareSimulator(G, num_vans)
    simulator.simulate_ridesharing(pickup_requests)

def generate_random_graph(num_nodes, connectivity):
    G = nx.random_regular_graph(connectivity, num_nodes)
    for edge in G.edges():
        G[edge[0]][edge[1]]['weight'] = random.randint(1, 10)
    return G

def generate_pickup_requests(num_nodes, num_requests):
    pickup_requests = []
    for customer_id in range(1, num_requests + 1):
        pickup_node = random.randint(0, num_nodes - 1)
        dropoff_node = random.randint(0, num_nodes - 1)
        pickup_requests.append((customer_id, pickup_node, dropoff_node))
    return pickup_requests

if __name__ == "__main__":
    main()
