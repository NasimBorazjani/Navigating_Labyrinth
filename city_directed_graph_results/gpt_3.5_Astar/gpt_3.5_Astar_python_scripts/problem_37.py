
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'R': {'F': 1, 'K': 1, 'T': 1, 'W': 1},
        'Q': {'X': 1, 'W': 1},
        'Y': {'R': 1, 'Q': 1, 'M': 1},
        'U': {'Y': 1, 'M': 1},
        'F': {'R': 1, 'M': 1, 'H': 1},
        'K': {'R': 1, 'F': 1, 'M': 1, 'W': 1},
        'M': {'Y': 1, 'U': 1, 'F': 1, 'K': 1},
        'T': {'Q': 1, 'F': 1, 'X': 1},
        'X': {'Q': 1, 'T': 1, 'W': 1},
        'W': {'R': 1, 'K': 1, 'X': 1, 'H': 1},
        'H': {'F': 1, 'W': 1},
        'L': {'W': 1}
    }
    
    # Define the start city
    start_city = 'L'
    # Define the goal cities
    goal_cities = ['M', 'Q']
    
    # Initialize a dictionary to store the cost of reaching each visited city
    visited_costs = {}
    visited_costs[start_city] = 0
    
    # Initialize a priority queue of cities not yet visited, with the start city as the first element
    queue = [(0, 0, [start_city], start_city)]
    
    # While there are un-visited cities
    while queue:
        _, g, path, current_city = heapq.heappop(queue)
        
        # If we have visited both goal cities twice, return the path
        if path.count('M') == 2 and path.count('Q') == 2:
            return path
        
        # Generate all possible actions from the current city, which includes moving to any connected city
        for neighbor in adjacency_matrix[current_city]:
            # Check if the new city is unvisited
            if neighbor not in path:
                # Generate the new path
                new_path = path + [neighbor]
                # The cost so far is the number of cities visited
                new_cost = g + 1
                
                # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of un-visited cities
                if neighbor not in visited_costs or new_cost < visited_costs[neighbor]:
                    visited_costs[neighbor] = new_cost
                    heapq.heappush(queue, (new_cost, new_cost, new_path, neighbor))
    
    return None

print(a_star())
