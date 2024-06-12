
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries of connected cities
    adjacency_matrix = {
        'P': {'K': 1, 'M': 1, 'O': 1},
        'U': {'E': 1, 'J': 1, 'R': 1},
        'Q': {'Z': 1},
        'G': {'E': 1, 'J': 1, 'R': 1},
        'E': {'G': 1, 'J': 1, 'O': 1},
        'K': {'J': 1, 'M': 1},
        'M': {'E': 1, 'J': 1, 'O': 1},
        'J': {'U': 1, 'G': 1, 'K': 1, 'M': 1},
        'N': {'E': 1, 'R': 1, 'T': 1},
        'T': {'P': 1, 'M': 1, 'O': 1},
        'Y': {'E': 1, 'R': 1},
        'R': {'K': 1, 'M': 1, 'Y': 1},
        'Z': {'P': 1},
        'X': {'E': 1, 'J': 1, 'O': 1},
        'O': {'N': 1, 'T': 1, 'X': 1}
    }
    
    # Define the initial state and goal state
    initial_state = 'G'
    goal_state = ['P', 'E', 'E']
    
    # Initialize a priority queue to store the states to be visited
    queue = []
    heapq.heappush(queue, (0, [initial_state], initial_state))
    
    # While there are states to visit
    while queue:
        _, path, current_city = heapq.heappop(queue)
        
        # If the current city is one of the goal cities, remove it from the list of goal cities
        if current_city in goal_state:
            goal_state.remove(current_city)
        
        # If all goal cities have been visited, return the path
        if not goal_state:
            return path
        
        # Get the neighbors of the current city
        neighbors = adjacency_matrix[current_city]
        
        # Iterate over the neighbors
        for neighbor in neighbors:
            # If the neighbor has not been visited yet
            if neighbor not in path:
                # Calculate the cost of the path
                new_path = path + [neighbor]
                new_cost = len(new_path)
                # Add the new path to the queue
                heapq.heappush(queue, (new_cost, new_path, neighbor))
    
    return None

print(a_star())
