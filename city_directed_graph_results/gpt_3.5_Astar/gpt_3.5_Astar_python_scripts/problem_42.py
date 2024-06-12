
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary with city names as keys and a list of connected cities as values
    adjacency_matrix = {
        'J': ['Y', 'P'],
        'U': ['T', 'Y', 'P'],
        'T': ['U', 'S', 'H'],
        'S': ['J', 'Y', 'P'],
        'N': ['J', 'A'],
        'F': ['A'],
        'Y': ['C', 'H'],
        'C': ['T', 'A'],
        'H': ['U', 'A'],
        'A': ['J', 'M', 'P'],
        'M': ['T'],
        'P': ['S', 'C', 'H']
    }
    
    # Define the initial state, goal state, and other variables
    initial_state = 'F'
    goal_state = ['H', 'N', 'H', 'N']
    visited = set()
    path = []
    
    # Initialize a priority queue to store the cities to visit, with the initial state as the first element
    queue = [(0, initial_state, [])]
    
    # While there are cities to visit in the queue
    while queue:
        _, current_city, current_path = heapq.heappop(queue)
        
        # If we have visited both destination cities twice, return the path
        if current_path.count('H') == 2 and current_path.count('N') == 2:
            return current_path
        
        # Add the current city to the visited set
        visited.add(current_city)
        
        # Iterate through the connected cities of the current city
        for city in adjacency_matrix[current_city]:
            # Check if the city has not been visited before
            if city not in visited:
                # Calculate the cost of the path so far
                cost = len(current_path) + 1
                # Add the city to the path and add it to the priority queue
                new_path = current_path + [city]
                heapq.heappush(queue, (cost, city, new_path))
    
    return None

print(a_star())
