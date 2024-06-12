
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries of connected cities
    adjacency_matrix = {
        'W': {'Y': 1, 'K': 1, 'Q': 1},
        'D': {'A': 1},
        'R': {'W': 1, 'C': 1},
        'A': {'D': 1, 'Y': 1, 'F': 1, 'S': 1, 'N': 1},
        'Y': {'Q': 1},
        'F': {'W': 1, 'C': 1},
        'C': {'A': 1, 'Y': 1, 'F': 1, 'S': 1, 'N': 1, 'Q': 1},
        'S': {'W': 1, 'D': 1, 'A': 1, 'Y': 1, 'K': 1},
        'N': {'D': 1, 'A': 1, 'Y': 1},
        'E': {'K': 1},
        'K': {'D': 1, 'A': 1, 'F': 1, 'N': 1},
        'Q': {'D': 1, 'A': 1, 'F': 1, 'C': 1, 'S': 1}
    }
    
    # Define the start city, the two destination cities, and the number of times to visit each destination
    start_city = 'E'
    destination_cities = ['R', 'D']
    num_visits = 2
    
    # Initialize a dictionary to store the cost of reaching each visited city
    visited_costs = {}
    visited_costs[start_city] = 0
    
    # Initialize a priority queue of cities not yet visited, with the start city as the first element
    queue = [(0, 0, [start_city], start_city)]
    
    # While there are unvisited cities
    while queue:
        _, g, path, current_city = heapq.heappop(queue)
        
        # Check if we have visited both destination cities the required number of times
        if all(path.count(city) == num_visits for city in destination_cities):
            return path
        
        # Generate all possible actions from the current city, which includes moving to any connected city
        for neighbor in adjacency_matrix[current_city]:
            # Check if the new city is unvisited or we found a new path with a lower cost to reach this city
            new_cost = g + 1
            if neighbor not in visited_costs or new_cost < visited_costs[neighbor]:
                visited_costs[neighbor] = new_cost
                heapq.heappush(queue, (new_cost, new_cost, path + [neighbor], neighbor))
    
    return None

print(a_star())
