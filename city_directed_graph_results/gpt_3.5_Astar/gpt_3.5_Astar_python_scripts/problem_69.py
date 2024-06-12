
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries of connected cities
    adjacency_matrix = {
        'N': {'Y': 1, 'H': 1, 'G': 1, 'K': 1, 'J': 1, 'B': 1},
        'Y': {'N': 1, 'U': 1, 'R': 1},
        'P': {'G': 1, 'U': 1, 'R': 1},
        'L': {'N': 1, 'Y': 1, 'G': 1, 'K': 1, 'J': 1, 'B': 1},
        'Q': {'R': 1},
        'H': {'C': 1, 'G': 1, 'U': 1, 'J': 1},
        'C': {'N': 1, 'Y': 1, 'P': 1, 'L': 1, 'K': 1, 'B': 1, 'T': 1},
        'G': {'Y': 1, 'P': 1, 'L': 1, 'K': 1, 'J': 1, 'B': 1},
        'U': {'K': 1, 'J': 1, 'B': 1},
        'K': {'N': 1, 'Y': 1, 'G': 1, 'J': 1, 'B': 1},
        'J': {'N': 1, 'Y': 1, 'G': 1, 'K': 1, 'B': 1},
        'B': {'N': 1, 'U': 1, 'R': 1},
        'R': {'Y': 1, 'P': 1, 'L': 1, 'Q': 1, 'B': 1},
        'T': {'Y': 1, 'P': 1, 'L': 1, 'C': 1}
    }
    
    # Define the initial state, goal state, and other variables
    initial_state = 'P'
    goal_state = ['N', 'R']
    num_visits = {city: 0 for city in goal_state}
    
    visited_costs = {}
    visited_costs[initial_state] = 0
    
    queue = [(0, 0, [], initial_state, num_visits.copy())]
    
    while queue:
        _, g, actions, current_city, current_visits = heapq.heappop(queue)
        
        # If we have visited both goal cities twice, return the actions taken
        if all(value == 2 for value in current_visits.values()):
            return actions
        
        # Generate all possible actions from the current city
        for neighbor, cost in adjacency_matrix[current_city].items():
            new_visits = current_visits.copy()
            if neighbor in goal_state:
                new_visits[neighbor] += 1
            new_cost = g + cost
            
            if new_cost < visited_costs.get(neighbor, float('inf')):
                visited_costs[neighbor] = new_cost
                heapq.heappush(queue, (new_cost, new_cost, actions + [neighbor], neighbor, new_visits))
    
    return None

print(a_star())
