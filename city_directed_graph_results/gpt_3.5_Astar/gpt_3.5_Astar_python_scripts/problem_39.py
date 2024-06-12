
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'O': {'Z': 1, 'M': 1},
        'Z': {'N': 1, 'Y': 1},
        'J': {'O': 1, 'M': 1, 'Q': 1},
        'K': {'O': 1, 'W': 1},
        'E': {'O': 1, 'J': 1, 'T': 1, 'Y': 1},
        'M': {'Z': 1},
        'T': {'Z': 1, 'J': 1, 'E': 1, 'Y': 1},
        'W': {'J': 1, 'E': 1, 'Q': 1},
        'N': {'O': 1, 'E': 1, 'Y': 1},
        'Q': {'E': 1, 'W': 1},
        'U': {'E': 1, 'Y': 1},
        'Y': {'Z': 1, 'J': 1, 'K': 1, 'Q': 1}
    }
    
    # Define the goal state where we visit cities N and T twice
    goal_state = ['N', 'T', 'N', 'T']
    
    # Initialize the starting city and the priority queue with the initial state
    start_city = 'O'
    queue = [(0, [start_city])]
    
    # While there are cities to explore
    while queue:
        _, path = heapq.heappop(queue)
        current_city = path[-1]
        
        # If the current path satisfies the goal state, return the path
        if path == goal_state:
            return path
        
        # Explore all possible next cities to visit
        for neighbor in adjacency_matrix[current_city]:
            new_path = path + [neighbor]
            # Add the new path to the priority queue with the cost being the length of the path
            heapq.heappush(queue, (len(new_path), new_path))
    
    return None

print(a_star())
