
import heapq


def a_star():
    # Define the adjacency matrix as a dictionary of dictionaries, where the keys are the city names and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'R': {'T': 1, 'C': 1, 'Y': 1, 'E': 1, 'A': 1},
        'T': {'C': 1, 'F': 1, 'W': 1},
        'C': {'Y': 1},
        'F': {'R': 1, 'T': 1, 'X': 1, 'E': 1, 'W': 1},
        'S': {'R': 1, 'E': 1},
        'X': {'R': 1, 'C': 1, 'Y': 1},
        'Y': {'R': 1, 'T': 1, 'E': 1},
        'E': {'C': 1, 'S': 1, 'A': 1, 'W': 1},
        'A': {'R': 1, 'S': 1, 'X': 1, 'Y': 1},
        'W': {'R': 1, 'X': 1, 'A': 1}
    }
    
    # Define the start city, the two destination cities, and the number of times we need to visit each destination
    start_city = 'C'
    destination_cities = ['F', 'W']
    num_visits = 2
    
    # Initialize a priority queue to store the paths to explore, with the initial path as the first element
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
                # Calculate the cost of the path by counting the number of cities visited
                cost = len(path)
                # Create a new path by extending the current path with the neighbor city
                new_path = path + [neighbor]
                # Add the new path to the priority queue with the cost as the priority
                heapq.heappush(queue, (cost, new_path))
    
    return None


print(a_star())
