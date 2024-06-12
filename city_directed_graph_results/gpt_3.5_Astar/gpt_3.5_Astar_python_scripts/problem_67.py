
import heapq


def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries of connected cities
    adjacency_matrix = {
        'A': {'E': 1, 'G': 1},
        'K': {'F': 1, 'H': 1},
        'G': {'B': 1, 'M': 1, 'R': 1},
        'U': {'L': 1, 'M': 1},
        'Q': {'K': 1, 'L': 1, 'M': 1},
        'D': {'A': 1, 'E': 1, 'J': 1, 'K': 1, 'L': 1},
        'N': {'C': 1, 'E': 1, 'K': 1},
        'X': {'A': 1, 'G': 1, 'M': 1},
        'S': {'A': 1, 'B': 1, 'E': 1, 'K': 1, 'M': 1},
        'V': {'C': 1, 'G': 1, 'H': 1},
        'Y': {'A': 1, 'E': 1, 'K': 1},
        'R': {'B': 1, 'G': 1, 'H': 1, 'K': 1},
        'Z': {'A': 1, 'B': 1, 'D': 1, 'G': 1, 'H': 1, 'I': 1}
    }
    
    # Define the start city and the target cities
    start_city = 'S'
    target_cities = ['N', 'R']
    
    # Initialize a priority queue to store the paths to explore, with the initial path as the first element
    queue = [(0, [start_city])]
    
    # While there are paths to explore
    while queue:
        # Pop the path with the lowest cost from the queue
        _, path = heapq.heappop(queue)
        
        # Get the current city from the end of the path
        current_city = path[-1]
        
        # Check if we have visited both target cities twice and return the path if we have
        if path.count('N') == 2 and path.count('R') == 2:
            return path
        
        # Explore all possible next cities from the current city
        for next_city in adjacency_matrix[current_city]:
            # Check if the next city has not been visited before
            if next_city not in path:
                # Calculate the cost of the path by counting the number of cities visited
                cost = len(path)
                # Create a new path by extending the current path with the next city
                new_path = path + [next_city]
                # Add the new path to the queue with the cost as the priority
                heapq.heappush(queue, (cost, new_path))
    
    return None


print(a_star())
