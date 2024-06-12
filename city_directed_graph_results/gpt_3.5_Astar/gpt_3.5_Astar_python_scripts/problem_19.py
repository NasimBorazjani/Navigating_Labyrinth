
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'J': {'I': 1, 'R': 1, 'M': 1, 'D': 1, 'E': 1},
        'X': {'R': 1, 'T': 1},
        'U': {'J': 1, 'X': 1, 'T': 1, 'B': 1},
        'I': {'U': 1},
        'R': {'I': 1, 'B': 1},
        'T': {'J': 1, 'I': 1, 'B': 1},
        'Y': {'I': 1, 'T': 1, 'D': 1},
        'B': {'X': 1, 'M': 1},
        'M': {'R': 1},
        'D': {'X': 1, 'M': 1},
        'E': {'J': 1, 'D': 1}
    }
    
    # Define the start city, the two destination cities, and the number of times we need to visit each destination
    start_city = 'E'
    destination_cities = ['T', 'Y']
    num_visits = 2
    
    # Initialize a priority queue to store the paths to explore, starting with the start city
    queue = [(0, [start_city])]
    
    # While there are paths to explore
    while queue:
        # Pop the path with the lowest cost from the priority queue
        _, path = heapq.heappop(queue)
        
        # Get the current city from the end of the path
        current_city = path[-1]
        
        # Check if we have visited both destination cities the required number of times
        if path.count(destination_cities[0]) == num_visits and path.count(destination_cities[1]) == num_visits:
            return path
        
        # Explore all possible connections from the current city
        for neighbor in adjacency_matrix[current_city]:
            # Check if the neighbor city has not been visited yet
            if neighbor not in path:
                # Calculate the cost of the path by adding 1 for each step
                new_cost = len(path)
                # Create a new path by extending the current path with the neighbor city
                new_path = path + [neighbor]
                # Add the new path to the priority queue with the cost as the priority
                heapq.heappush(queue, (new_cost, new_path))
    
    return None

print(a_star())
