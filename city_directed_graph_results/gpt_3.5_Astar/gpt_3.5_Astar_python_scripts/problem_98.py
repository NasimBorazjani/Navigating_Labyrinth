
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are lists of connected cities
    adjacency_matrix = {
        'B': ['F', 'Q', 'V', 'D', 'A', 'J'],
        'X': ['V', 'J', 'K', 'H'],
        'F': ['B', 'J', 'N'],
        'Q': ['J', 'V'],
        'V': ['B', 'X', 'Q', 'G', 'H', 'K', 'T'],
        'D': ['B', 'X', 'V', 'N'],
        'A': ['F', 'J', 'S'],
        'J': ['X', 'Q', 'A', 'N', 'H'],
        'N': ['F', 'J', 'M', 'G', 'S'],
        'M': ['F', 'N'],
        'G': ['V', 'J', 'K', 'H', 'S'],
        'H': ['X', 'V', 'J', 'G', 'K'],
        'K': ['V', 'G', 'H', 'T', 'S'],
        'T': ['V', 'K', 'S'],
        'S': ['A', 'N', 'G', 'H', 'K', 'T']
    }
    
    # Define the start city
    start_city = 'D'
    # Define the destination cities we need to visit twice
    destinations = ['J', 'X']
    
    visited_costs = {}
    visited_costs[start_city] = 0
    
    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [start_city], start_city))
    
    while queue:
        _, g, path, current_city = heappop(queue)
        
        # Check if we have visited both destination cities twice
        if path.count('J') == 2 and path.count('X') == 2:
            return path
        
        # Generate all possible actions from the current city, which includes moving to any connected city
        for neighbor in adjacency_matrix[current_city]:
            # Check if the neighbor city has not been visited yet
            if path.count(neighbor) == 0:
                new_path = path + [neighbor]
                new_cost = g + 1
                
                if neighbor not in visited_costs or new_cost < visited_costs[neighbor]:
                    visited_costs[neighbor] = new_cost
                    heappush(queue, (new_cost, new_cost, new_path, neighbor))
    
    return None

print(a_star())
