
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'L': {'P': 1, 'N': 1, 'F': 1, 'O': 1, 'K': 1, 'H': 1, 'W': 1, 'U': 1},
        'S': {'R': 1, 'O': 1, 'W': 1},
        'P': {'N': 1, 'R': 1},
        'R': {'P': 1, 'F': 1, 'H': 1},
        'N': {'S': 1, 'O': 1, 'T': 1},
        'F': {'R': 1, 'O': 1, 'U': 1},
        'O': {'K': 1, 'H': 1},
        'K': {'S': 1, 'F': 1, 'T': 1},
        'B': {'P': 1, 'N': 1, 'W': 1},
        'H': {'S': 1, 'F': 1, 'T': 1, 'E': 1},
        'T': {'L': 1, 'H': 1, 'W': 1, 'E': 1},
        'W': {'L': 1, 'B': 1, 'T': 1, 'U': 1},
        'U': {'L': 1, 'B': 1, 'F': 1, 'E': 1},
        'E': {'S': 1, 'R': 1, 'H': 1}
    }
    
    # Define the start city and the two destination cities we need to visit twice
    start_city = 'B'
    destinations = ['W', 'F']
    
    # Initialize a dictionary to store the cost of reaching each visited city
    visited_costs = {}
    visited_costs[start_city] = 0
    
    # Initialize a priority queue of cities not yet visited, with the start city as the first element
    queue = [(0, 0, [start_city], start_city)]
    
    while queue:
        _, g, path, current_city = heapq.heappop(queue)
        
        # If we have visited both destination cities twice, return the path
        if path.count(destinations[0]) == 2 and path.count(destinations[1]) == 2:
            return path
        
        # Generate all possible actions from the current city, which includes moving to any connected city
        for neighbor in adjacency_matrix[current_city]:
            new_path = path + [neighbor]
            new_cost = g + 1
            
            # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of unvisited cities
            if neighbor not in visited_costs or new_cost < visited_costs[neighbor]:
                visited_costs[neighbor] = new_cost
                heapq.heappush(queue, (new_cost, new_cost, new_path, neighbor))
    
    return None

print(a_star())
