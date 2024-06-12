
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries of connected cities
    adjacency_matrix = {
        'S': {'Z': 1, 'P': 1, 'T': 1, 'B': 1},
        'Z': {'N': 1},
        'I': {'Z': 1, 'F': 1, 'L': 1},
        'R': {'S': 1, 'Z': 1, 'P': 1, 'T': 1, 'B': 1, 'G': 1, 'N': 1, 'E': 1},
        'P': {'M': 1},
        'T': {'F': 1},
        'X': {'I': 1, 'R': 1, 'P': 1, 'B': 1, 'F': 1, 'A': 1, 'L': 1, 'M': 1, 'G': 1, 'N': 1, 'E': 1},
        'B': {'F': 1, 'A': 1},
        'F': {'I': 1, 'L': 1},
        'A': {'N': 1},
        'L': {'Z': 1, 'N': 1},
        'M': {'G': 1, 'N': 1, 'E': 1},
        'G': {'I': 1, 'F': 1},
        'N': {'E': 1},
        'E': {}
    }
    
    # Define the initial state, goal state, and other variables
    initial_state = 'P'
    goal_state = ['I', 'N']
    num_visits = {city: 0 for city in goal_state}
    
    visited_costs = {}
    visited_costs[initial_state] = 0
    
    queue = [(0, 0, [], initial_state, num_visits.copy())]
    
    while queue:
        _, g, actions, current_city, current_visits = heapq.heappop(queue)
        
        # If we have visited both I and N twice, return the path
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
