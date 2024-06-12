
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are lists of connected cities
    adjacency_matrix = {
        'C': ['Z', 'R'],
        'Z': ['H', 'P', 'R'],
        'F': ['Y', 'R'],
        'U': ['C', 'F', 'H', 'P', 'A', 'R'],
        'W': ['C', 'Z', 'H', 'I', 'B'],
        'T': ['Y', 'P', 'A', 'I'],
        'H': ['F', 'Y', 'P', 'O', 'A', 'I', 'G'],
        'Y': ['P', 'R'],
        'P': ['O', 'A', 'R'],
        'O': ['H', 'I', 'B'],
        'A': ['Z', 'H', 'I', 'G'],
        'R': ['C', 'Z', 'U', 'A', 'I', 'G'],
        'I': ['C', 'Z', 'U', 'A', 'G'],
        'G': ['C', 'Z', 'U', 'A'],
        'B': ['Y', 'G']
    }
    
    # Define the initial state as being in city 'F'
    initial_state = 'F'
    # Define the goal state as visiting cities 'G' and 'R' twice each
    goal_state = ['G', 'G', 'R', 'R']
    
    # Initialize a priority queue to store the states to be visited, with the initial state as the first element
    queue = [(0, [initial_state])]
    
    # While there are states to visit
    while queue:
        _, path = heapq.heappop(queue)
        current_city = path[-1]
        
        # If the current path satisfies the goal state, return the path
        if path.count('G') == 2 and path.count('R') == 2:
            return path
        
        # Generate all possible actions from the current state, which are the connected cities that have not been visited yet
        for neighbor in adjacency_matrix[current_city]:
            if neighbor not in path:
                new_path = path + [neighbor]
                # Calculate the cost of the path as the length of the path
                cost = len(new_path)
                # Add the new path to the priority queue
                heapq.heappush(queue, (cost, new_path))
    
    return None

print(a_star())
