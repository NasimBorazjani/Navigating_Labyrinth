
import heapq


def initialize():
    # Define the adjacency matrix representing the connections between cities
    adjacency_matrix = [
        ['F', 'I', 'C', 'G', 'N', 'L', 'X', 'Q', 'U', 'R', 'O', 'B'],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0],
        [0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0]
    ]
    # Define the start city
    start_city = 'G'
    # Define the destination cities that need to be visited twice
    destination_cities = ['O', 'R']
    # Initialize a dictionary to store the cost of reaching each visited city
    visited_costs = {}
    visited_costs[start_city] = 0
    # Initialize a priority queue of cities not yet visited, with the start city as the first element
    queue = [(0, 0, [start_city], start_city)]
    
    return adjacency_matrix, start_city, destination_cities, visited_costs, queue


def a_star():
    # The initialize function initializes and returns the variables needed for the A* algorithm
    adjacency_matrix, start_city, destination_cities, visited_costs, queue = initialize()

    while queue:
        _, g, path, current_city = heapq.heappop(queue)

        # Check if the current city is one of the destination cities that need to be visited twice
        if current_city in destination_cities:
            # Remove the current city from the list of destination cities
            destination_cities.remove(current_city)
            # If there are no more destination cities left, return the path
            if not destination_cities:
                return path

        # Find the index of the current city in the adjacency matrix
        current_city_index = adjacency_matrix[0].index(current_city)

        # Explore the neighbors of the current city
        for i in range(len(adjacency_matrix)):
            # Check if there is a road from the current city to the neighbor city
            if adjacency_matrix[current_city_index][i] == 1:
                neighbor_city = adjacency_matrix[0][i]
                # Calculate the cost to reach the neighbor city
                new_cost = g + 1
                
                # If the neighbor city has not been visited yet or we found a new path with a lower cost to reach the city, add it to the queue
                if neighbor_city not in visited_costs or new_cost < visited_costs[neighbor_city]:
                    visited_costs[neighbor_city] = new_cost
                    heapq.heappush(queue, (new_cost, new_cost, path + [neighbor_city], neighbor_city))
    
    return None


print(a_star())
