
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary
    adjacency_matrix = {
        'S': {'O': 1, 'B': 1},
        'E': {'F': 1, 'B': 1, 'I': 1, 'Z': 1},
        'D': {'F': 1},
        'Y': {'E': 1, 'D': 1, 'B': 1, 'J': 1},
        'F': {'B': 1, 'Y': 1, 'U': 1, 'I': 1},
        'B': {'S': 1, 'E': 1, 'Y': 1, 'F': 1, 'U': 1},
        'O': {'S': 1, 'H': 1, 'Q': 1},
        'H': {'Y': 1, 'Q': 1, 'Z': 1},
        'U': {'E': 1, 'B': 1, 'I': 1, 'Q': 1},
        'I': {'F': 1, 'U': 1, 'Z': 1},
        'C': {'J': 1},
        'Q': {'O': 1, 'H': 1, 'U': 1, 'Z': 1},
        'Z': {'E': 1, 'H': 1, 'I': 1, 'Q': 1, 'J': 1},
        'J': {'Y': 1, 'Z': 1},
    }
    
    # Define the initial state and goal state
    initial_state = 'O'
    goal_state = ['B', 'H']
    
    # Initialize a priority queue to store the states to be visited
    queue = []
    heapq.heappush(queue, (0, [initial_state], initial_state))
    
    # While there are states to visit
    while queue:
        _, path, current_state = heapq.heappop(queue)
        
        # If we have visited both destination cities twice, return the path
        if path.count('B') == 2 and path.count('H') == 2:
            return path
        
        # Explore the neighbors of the current state
        for neighbor, weight in adjacency_matrix[current_state].items():
            # Check if the neighbor has not been visited before
            if neighbor not in path:
                new_path = path + [neighbor]
                new_cost = len(new_path)
                heapq.heappush(queue, (new_cost, new_path, neighbor))
    
    return None

print(a_star())
