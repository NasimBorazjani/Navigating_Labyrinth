
import heapq


def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'F': {'Z': 1, 'M': 1, 'Q': 1, 'V': 1, 'J': 1, 'D': 1, 'B': 1},
        'Z': {'I': 1, 'L': 1, 'B': 1},
        'M': {'Z': 1, 'C': 1, 'J': 1, 'N': 1, 'E': 1, 'O': 1},
        'Q': {'C': 1, 'J': 1},
        'I': {'V': 1, 'J': 1},
        'V': {'C': 1},
        'L': {'M': 1, 'Q': 1},
        'C': {'F': 1, 'Z': 1, 'J': 1, 'N': 1, 'O': 1},
        'J': {'Z': 1, 'L': 1, 'D': 1, 'N': 1, 'E': 1, 'B': 1},
        'D': {'F': 1, 'M': 1, 'B': 1},
        'N': {'I': 1, 'V': 1, 'O': 1},
        'E': {'I': 1, 'V': 1},
        'B': {'F': 1, 'Z': 1, 'M': 1, 'C': 1, 'N': 1, 'E': 1},
        'O': {'M': 1, 'C': 1, 'J': 1}
    }
    
    # Define the start city
    start_city = 'Q'
    # Define the destination cities
    destination_cities = ['M', 'L']
    
    # Initialize a priority queue to store the paths to be explored, with the start city as the first element
    queue = [(0, [start_city])]
    
    while queue:
        _, path = heapq.heappop(queue)
        current_city = path[-1]
        
        # Check if we have visited both destination cities twice
        if path.count('M') == 2 and path.count('L') == 2:
            return path
        
        # Explore all possible connections from the current city
        for neighbor, weight in adjacency_matrix[current_city].items():
            # Check if the neighbor city has not been visited before
            if neighbor not in path:
                # Calculate the new cost of the path
                new_cost = len(path)
                # Calculate the heuristic cost (in this case, the remaining number of destination cities to visit)
                heuristic_cost = 4 - path.count('M') - path.count('L')
                # Add the new path to the priority queue
                heapq.heappush(queue, (new_cost + heuristic_cost, path + [neighbor]))
    
    return None


print(a_star())
