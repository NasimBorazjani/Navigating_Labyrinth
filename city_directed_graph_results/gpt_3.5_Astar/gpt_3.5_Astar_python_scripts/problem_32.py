
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'D': {'T': 1, 'E': 1, 'J': 1},
        'T': {'L': 1, 'E': 1, 'Q': 1},
        'L': {'E': 1},
        'E': {'C': 1, 'J': 1, 'Q': 1, 'O': 1},
        'C': {'J': 1},
        'J': {'X': 1},
        'Q': {'T': 1, 'O': 1, 'F': 1},
        'O': {'D': 1, 'K': 1},
        'K': {'T': 1, 'L': 1, 'F': 1},
        'X': {'D': 1},
        'F': {'D': 1, 'T': 1, 'L': 1}
    }
    
    # Define the start city and the target cities we need to visit twice
    start_city = 'J'
    target_cities = ['D', 'E']
    
    # Initialize a dictionary to store the cost of reaching each visited city
    visited_costs = {}
    visited_costs[start_city] = 0
    
    # Initialize a priority queue of cities not yet visited, with the start city as the first element
    queue = [(0, 0, [start_city], start_city)]
    
    # While there are unvisited cities
    while queue:
        _, g, path, current_city = heapq.heappop(queue)
        
        # Check if we have visited both target cities twice
        if path.count('D') == 2 and path.count('E') == 2:
            return path
        
        # Generate all possible actions from the current city, which includes moving to any connected city
        for neighbor, cost in adjacency_matrix[current_city].items():
            # Check if the new city is unvisited or we found a new path with a lower cost to reach this city
            if neighbor not in path or g + cost < visited_costs[neighbor]:
                visited_costs[neighbor] = g + cost
                heapq.heappush(queue, (g + cost, g + cost, path + [neighbor], neighbor))
    
    return None

print(a_star())
