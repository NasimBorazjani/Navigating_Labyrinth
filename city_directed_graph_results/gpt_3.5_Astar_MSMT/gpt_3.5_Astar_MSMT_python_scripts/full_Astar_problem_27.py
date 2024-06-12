
import heapq


def initialize():
    # Define the adjacency matrix representing the connections between cities
    adjacency_matrix = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
                        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
                        [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
                        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0]]
    
    # Define the cities and the start city
    cities = ['J', 'H', 'K', 'W', 'X', 'I', 'B', 'U', 'D', 'Z', 'G']
    start_city = 'D'
    
    # Initialize a dictionary to store the cost of reaching each visited city
    visited_costs = {}
    visited_costs[start_city] = 0
    
    # Initialize a priority queue of cities not yet visited, with the start city as the first element
    queue = [(0, start_city)]
    
    return adjacency_matrix, cities, start_city, visited_costs, queue


def a_star():
    # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem
    adjacency_matrix, cities, start_city, visited_costs, queue = initialize()

    while queue:
        _, current_city = heapq.heappop(queue)

        # Check if we have visited both destination cities twice
        if sum([visited_costs[city] == 2 for city in ['H', 'Z']]) == 2:
            return [city for city in visited_costs.keys()]

        # Find the neighbors of the current city
        neighbors = [cities[i] for i in range(len(cities)) if adjacency_matrix[cities.index(current_city)][i] == 1]

        # Update the costs of the neighbors and add them to the queue
        for neighbor in neighbors:
            new_cost = visited_costs[current_city] + 1
            if neighbor not in visited_costs or new_cost < visited_costs[neighbor]:
                visited_costs[neighbor] = new_cost
                heapq.heappush(queue, (new_cost, neighbor))

    return None


print(a_star())
