
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries of connected cities
    adjacency_matrix = {
        'O': {'Z': 1, 'L': 1, 'R': 1},
        'M': {'V': 1},
        'Y': {'O': 1, 'M': 1, 'V': 1},
        'J': {'Z': 1, 'F': 1, 'X': 1},
        'Z': {},
        'V': {},
        'K': {'M': 1, 'Y': 1, 'J': 1},
        'F': {'O': 1},
        'X': {'J': 1, 'Z': 1, 'L': 1},
        'L': {'O': 1, 'K': 1},
        'R': {'J': 1, 'K': 1}
    }
    
    # Define the initial state, goal state, and other variables
    initial_state = 'M'
    goal_state = ['X', 'Y']
    num_visits = 2
    visited_states = set()
    
    # Initialize a priority queue to store the states to be visited, with the initial state as the first element
    queue = [(0, initial_state, [initial_state], 0)]
    
    # While there are states to visit
    while queue:
        _, current_state, path, visits = heapq.heappop(queue)
        
        # If we have visited the goal states the required number of times, return the path
        if current_state in goal_state and path.count(current_state) == num_visits:
            return path
        
        # Add the current state to the set of visited states
        visited_states.add(current_state)
        
        # Explore all possible actions from the current state
        for neighbor, cost in adjacency_matrix[current_state].items():
            # Check if the neighbor has not been visited before
            if neighbor not in visited_states:
                # Calculate the new cost and add it to the priority queue
                new_cost = len(path) + cost
                heapq.heappush(queue, (new_cost, neighbor, path + [neighbor], visits + 1))
    
    return None

print(a_star())
