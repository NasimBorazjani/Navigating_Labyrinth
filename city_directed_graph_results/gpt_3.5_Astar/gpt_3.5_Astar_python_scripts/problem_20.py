
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'F': {'N': 1},
        'I': {'R': 1},
        'Y': {'N': 1},
        'R': {'F': 1, 'M': 1, 'N': 1},
        'X': {'I': 1, 'Q': 1},
        'Q': {'I': 1, 'M': 1},
        'M': {'R': 1, 'X': 1, 'S': 1, 'N': 1},
        'S': {'F': 1, 'I': 1, 'X': 1},
        'C': {'I': 1, 'Y': 1, 'R': 1},
        'D': {'Y': 1, 'X': 1, 'M': 1},
        'N': {'C': 1, 'D': 1}
    }
    
    # Define the initial state as the starting city 'F' and the number of times we need to visit cities 'I' and 'N'
    initial_state = ('F', 2, 2)
    
    visited_costs = {}
    visited_costs[initial_state] = 0
    
    queue = []
    heapq.heappush(queue, (0, 0, [], initial_state))
    
    while queue:
        _, g, actions, state = heapq.heappop(queue)
        
        # Check if we have visited cities 'I' and 'N' twice each
        if state[1] == 0 and state[2] == 0:
            return actions
        
        current_city = state[0]
        
        # Generate all possible actions from the current state, which includes moving to a neighboring city
        for neighbor, cost in adjacency_matrix[current_city].items():
            # Check if we can visit the neighbor city based on the remaining visits to 'I' and 'N'
            if (neighbor != 'I' or state[1] > 0) and (neighbor != 'N' or state[2] > 0):
                new_state = (neighbor, state[1] - (1 if neighbor == 'I' else 0), state[2] - (1 if neighbor == 'N' else 0))
                new_cost = g + cost
                
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost, new_cost, actions + [neighbor], new_state))
    
    return None

print(a_star())
