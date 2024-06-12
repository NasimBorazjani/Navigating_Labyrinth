
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries of connected cities
    adjacency_matrix = {
        'C': {'A': 1},
        'L': {'C': 1, 'O': 1, 'H': 1},
        'D': {'C': 1, 'H': 1, 'K': 1, 'N': 1, 'J': 1},
        'O': {'L': 1, 'A': 1},
        'A': {'L': 1, 'Z': 1},
        'Z': {'H': 1, 'N': 1},
        'M': {'H': 1, 'J': 1},
        'H': {'L': 1, 'D': 1, 'K': 1, 'R': 1, 'M': 1},
        'K': {'C': 1, 'L': 1, 'A': 1, 'R': 1},
        'R': {'A': 1, 'Z': 1, 'M': 1, 'Q': 1},
        'Q': {'L': 1, 'D': 1, 'R': 1},
        'N': {'L': 1, 'D': 1, 'Z': 1},
        'J': {'D': 1, 'M': 1}
    }
    
    # Define the start city, the two destination cities, and the number of times we need to visit each destination
    start_city = 'C'
    destination_cities = ['D', 'J']
    num_visits = 2
    
    # Initialize a priority queue to store the paths to explore, with the initial path as the first element
    queue = [(0, [start_city])]
    
    # While there are paths to explore
    while queue:
        # Pop the path with the lowest cost from the queue
        _, path = heapq.heappop(queue)
        
        # Get the current city from the end of the path
        current_city = path[-1]
        
        # Check if we have visited both destination cities the required number of times
        if path.count(destination_cities[0]) == num_visits and path.count(destination_cities[1]) == num_visits:
            return path
        
        # Explore all possible next cities to visit from the current city
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
