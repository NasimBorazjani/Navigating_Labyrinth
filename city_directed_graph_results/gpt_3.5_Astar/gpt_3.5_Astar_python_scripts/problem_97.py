
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are lists of connected cities
    adjacency_matrix = {
        'R': ['J', 'A'],
        'Y': ['R', 'W', 'J', 'A', 'O', 'U', 'P', 'V'],
        'W': ['U'],
        'H': ['Y', 'O', 'U', 'L'],
        'J': ['Y', 'W', 'H', 'A', 'O', 'L'],
        'A': ['Y', 'J', 'N', 'E'],
        'O': ['R', 'Y', 'J', 'N', 'V'],
        'N': ['Y', 'H', 'U', 'P'],
        'U': ['W', 'H'],
        'E': ['Y', 'W', 'O', 'V'],
        'Q': ['R', 'O', 'U'],
        'L': ['Y', 'A', 'O'],
        'P': ['Y', 'H', 'J', 'A'],
        'V': ['H', 'J', 'P', 'X'],
        'X': ['H', 'A', 'P']
    }
    
    # Define the start city
    start_city = 'Q'
    # Define the destination cities that need to be visited twice
    destinations = ['N', 'Y']
    
    visited_costs = {}
    visited_costs[start_city] = 0
    
    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], start_city))
    
    while queue:
        _, g, actions, current_city = heappop(queue)
        
        # Check if we have visited both destination cities twice
        if all(destinations.count(city) == 2 for city in actions):
            return actions
        
        # Generate all possible actions from the current city
        for neighbor in adjacency_matrix[current_city]:
            # Check if the neighbor city has not been visited before
            if actions.count(neighbor) < 1:
                new_cost = g + 1
                if neighbor not in visited_costs or new_cost < visited_costs[neighbor]:
                    visited_costs[neighbor] = new_cost
                    heappush(queue, (new_cost, new_cost, actions + [neighbor], neighbor))
    
    return None

print(a_star())
