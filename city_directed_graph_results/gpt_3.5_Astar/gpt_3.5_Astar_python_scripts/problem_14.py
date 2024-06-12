
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries of connected cities
    adjacency_matrix = {
        'M': {'Z': 1, 'U': 1, 'B': 1, 'H': 1},
        'U': {'F': 1, 'P': 1, 'B': 1, 'M': 1},
        'B': {'U': 1, 'V': 1, 'Z': 1, 'N': 1},
        'F': {'E': 1, 'H': 1, 'U': 1},
        'V': {'F': 1, 'P': 1, 'Z': 1},
        'Z': {'M': 1, 'B': 1, 'V': 1, 'N': 1},
        'P': {'U': 1, 'V': 1, 'Z': 1},
        'N': {'B': 1, 'Z': 1, 'H': 1},
        'E': {'F': 1},
        'H': {'M': 1, 'B': 1, 'Z': 1}
    }
    
    # Define the initial state, which is the starting city 'N'
    initial_state = 'N'
    
    # Define the goal state, which is to visit cities 'H' and 'M' twice each
    goal_state = ['H', 'M', 'H', 'M']
    
    # Initialize a priority queue to store the states to be visited, with the initial state as the first element
    queue = [(0, [initial_state])]
    
    # While there are states to visit
    while queue:
        _, path = heapq.heappop(queue)
        current_city = path[-1]
        
        # Check if the current path satisfies the goal state
        if path == goal_state:
            return path
        
        # Generate all possible actions from the current state, which are the cities connected to the current city
        for neighbor in adjacency_matrix[current_city]:
            # Check if the neighbor city has not been visited before in the current path
            if neighbor not in path:
                new_path = path + [neighbor]
                # Calculate the cost of the new path, which is the length of the path
                new_cost = len(new_path)
                # Add the new path to the priority queue
                heapq.heappush(queue, (new_cost, new_path))
    
    return None

print(a_star())
