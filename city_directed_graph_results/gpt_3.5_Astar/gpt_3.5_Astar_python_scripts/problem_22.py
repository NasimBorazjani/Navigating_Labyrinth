
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries of connected cities
    adjacency_matrix = {
        'X': {'N': 1, 'U': 1, 'V': 1, 'Z': 1, 'S': 1},
        'M': {'N': 1, 'U': 1, 'T': 1, 'V': 1},
        'U': {'N': 1, 'T': 1, 'V': 1},
        'N': {'X': 1, 'M': 1, 'U': 1, 'S': 1, 'F': 1},
        'T': {'X': 1, 'M': 1, 'U': 1, 'E': 1},
        'V': {'M': 1, 'U': 1, 'N': 1, 'Z': 1, 'S': 1, 'F': 1},
        'Z': {'M': 1, 'V': 1},
        'S': {'Z': 1, 'F': 1},
        'F': {'E': 1, 'J': 1},
        'E': {'X': 1, 'V': 1, 'S': 1, 'F': 1, 'J': 1},
        'J': {'M': 1, 'U': 1, 'V': 1}
    }
    
    # Define the start city, the two destination cities, and the number of times to visit each destination
    start_city = 'X'
    destination_cities = ['E', 'T']
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
        for neighbor, cost in adjacency_matrix[current_city].items():
            new_path = path + [neighbor]
            new_cost = g + cost
            
            # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of unvisited cities
            if neighbor not in visited_costs or new_cost < visited_costs[neighbor]:
                visited_costs[neighbor] = new_cost
                heapq.heappush(queue, (new_cost, new_cost, new_path, neighbor))
    
    return None

print(a_star())
