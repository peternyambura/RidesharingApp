

class RideshareSimulator:
    def __init__(self, G, num_vans):
        self.G = G
        self.num_vans = num_vans
        self.vans = [Van(van_id) for van_id in range(1, num_vans + 1)]
        self.network_flow = nx.DiGraph()


    def update_network_flow(self):
        for van in self.vans:
            for customer_request in van.service_queue:
                pickup_node = customer_request[1]
                dropoff_node = customer_request[2]
                edge_capacity = 1  
                self.network_flow.add_edge(pickup_node, dropoff_node, capacity=edge_capacity)

    def calculate_network_flow(self):
        flow_value, flow_dict = flow.max_flow_min_cost(self.network_flow, source_node, sink_node)
        return flow_value, flow_dict

    def simulate_ridesharing(self, pickup_requests):
        for clock_tick in range(1, 11):
            print(f"At clock tick {clock_tick}:")
            
            self.update_network_flow()
            
            flow_value, flow_dict = self.calculate_network_flow()
            
            for van in self.vans:
                if not van.service_queue:
                    if pickup_requests:
                        customer_request = self.assign_customer_based_on_flow(flow_dict, flow_value, pickup_requests)
                        if customer_request:
                            van.assign_customer(customer_request)
                            print(f"Van {van.van_id}: Pickup request at node {customer_request[1]} for customer {customer_request[0]}, drop off at node {customer_request[2]}")
                else:
                    next_node = van.service_queue[0][1]
                    print(f"Van {van.van_id} is heading to node {next_node}")
                    van.routing_queue.append(next_node)
                    van.service_queue.pop(0)

class Van:
    def __init(self, van_id, capacity=5):
        self.van_id = van_id
        self.capacity = capacity
        self.service_queue = []
        self.routing_queue = []

    def assign_customer(self, customer_request):
        if len(self.service_queue) < self.capacity:
            self.service_queue.append(customer_request)
        else:
            print(f"Van {self.van_id}: No capacity for customer {customer_request[0]}")

    def calculate_distance(self, node1, node2):
        return abs(node1 - node2)

    def get_next_node(self):
        if self.service_queue:
            next_customer = self.service_queue[0]
            next_node = next_customer[1] if not self.is_occupied else next_customer[2]
            return next_node
        else:
            return None

    def update_location(self, next_node):
        distance = self.calculate_distance(self.current_node, next_node)
        self.current_node = next_node
        self.routing_queue.pop(0)
        self.is_occupied = not self.is_occupied

    def simulate_tick(self):
        next_node = self.get_next_node()
        if next_node is not None:
            print(f"Van {self.van_id} is heading to node {next_node}")
            self.update_location(next_node)
            