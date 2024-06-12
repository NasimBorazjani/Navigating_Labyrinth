
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'B': {'K': 1, 'P': 1, 'Q': 1, 'R': 1, 'V': 1},
        'K': {'D': 1, 'P': 1},
        'S': {'K': 1, 'P': 1},
        'X': {'D': 1, 'J': 1, 'T': 1},
        'T': {'D': 1, 'J': 1, 'P': 1},
        'P': {'E': 1},
        'Q': {'K': 1, 'J': 1, 'P': 1},
        'M': {'K': 1, 'J': 1, 'R': 1},
        'R': {'B': 1, 'D': 1, 'G': 1, 'P': 1},
        'G': {'J': 1, 'T': 1},
        'J': {'P': 1, 'T': 1},
        'V': {'R': 1, 'E': 1},
        'E': {'R': 1, 'D': 1, 'G': 1}
    }
    
    # Define the start city and the goal cities
    start_city = 'S'
    goal_cities = ['B', 'V']
    
    # Initialize a dictionary to store the cost of reaching each visited city
    visited_costs = {}
    visited_costs[start_city] = 0
    
    # Initialize a priority queue of cities not yet visited, with the start city as the first element
    queue = [(0, 0, [start_city], start_city)]
    
    # While there are un-visited cities
    while queue:
        _, g, path, current_city = heapq.heappop(queue)
        
        # If we have visited both goal cities twice, return the path
        if path.count('B') == 2 and path.count('V') == 2:
            return path
        
        # Generate all possible actions from the current city, which includes moving to any connected city
        for neighbor, cost in adjacency_matrix[current_city].items():
            # Check if the new city is unvisited or we found a new path with a lower cost to reach this city
            if neighbor not in visited_costs or g + cost < visited_costs[neighbor]:
                visited_costs[neighbor] = g + cost
                heapq.heappush(queue, (g + cost, g + cost, path + [neighbor], neighbor))
    
    return None

print(a_star())
