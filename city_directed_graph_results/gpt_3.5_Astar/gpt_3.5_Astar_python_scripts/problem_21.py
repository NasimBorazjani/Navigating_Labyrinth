
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary
    adjacency_matrix = {
        'I': {'M': 1, 'Y': 1, 'H': 1, 'R': 1, 'W': 1},
        'K': {'M': 1},
        'D': {'C': 1, 'R': 1},
        'M': {'I': 1},
        'Y': {'K': 1, 'D': 1},
        'H': {'K': 1, 'D': 1, 'C': 1, 'V': 1, 'Q': 1},
        'C': {'K': 1, 'R': 1, 'V': 1},
        'R': {'V': 1, 'Q': 1},
        'V': {'W': 1},
        'W': {'I': 1, 'C': 1},
        'Q': {'Y': 1, 'H': 1, 'C': 1, 'R': 1}
    }
    
    # Define the initial state, which is the starting city 'Y'
    initial_state = 'Y'
    
    # Define the goal state, which is to visit cities 'I' and 'Q' twice
    goal_state = ['I', 'I', 'Q', 'Q']
    
    # Initialize a priority queue to store the states to be visited, with the initial state as the first element
    queue = [(0, [initial_state])]
    
    # While there are states to visit
    while queue:
        _, path = heapq.heappop(queue)
        
        # If the path contains the goal state twice, return the path
        if path.count('I') == 2 and path.count('Q') == 2:
            return path
        
        # Get the current city from the path
        current_city = path[-1]
        
        # Get the neighbors of the current city from the adjacency matrix
        neighbors = adjacency_matrix[current_city]
        
        # Iterate over the neighbors
        for neighbor in neighbors:
            # Check if the neighbor has not been visited before
            if neighbor not in path:
                # Create a new path by adding the neighbor to the current path
                new_path = path + [neighbor]
                # Calculate the cost of the new path (length of the path)
                cost = len(new_path)
                # Add the new path to the priority queue
                heapq.heappush(queue, (cost, new_path))
    
    return None

print(a_star())
