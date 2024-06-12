
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries of connected cities
    adjacency_matrix = {
        'M': {'Y': 1, 'E': 1, 'A': 1, 'J': 1, 'S': 1},
        'Y': {'E': 1, 'N': 1, 'W': 1},
        'Q': {'T': 1, 'E': 1, 'F': 1},
        'T': {'Y': 1, 'Q': 1, 'A': 1, 'J': 1, 'S': 1},
        'E': {'Q': 1, 'N': 1, 'Z': 1},
        'A': {'M': 1, 'Q': 1, 'J': 1, 'V': 1},
        'J': {'M': 1, 'Y': 1, 'T': 1, 'A': 1},
        'S': {'M': 1, 'T': 1, 'V': 1},
        'V': {'Y': 1, 'Q': 1, 'T': 1, 'F': 1, 'N': 1},
        'F': {'Z': 1, 'I': 1},
        'W': {'T': 1},
        'N': {'M': 1, 'Q': 1, 'T': 1, 'I': 1},
        'Z': {'Q': 1, 'V': 1, 'I': 1},
        'C': {'V': 1, 'F': 1, 'Z': 1},
        'I': {'Q': 1, 'E': 1, 'F': 1}
    }
    
    # Define the start city, destination cities, and the number of times to visit each destination city
    start_city = 'S'
    destination_cities = ['T', 'C']
    num_visits = {city: 2 for city in destination_cities}
    
    visited_costs = {}
    visited_costs[start_city] = 0
    
    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], start_city, num_visits.copy()))
    
    while queue:
        _, g, actions, current_city, remaining_visits = heappop(queue)
        
        # If we have visited all destination cities the required number of times, return the actions taken
        if all(remaining_visits[city] == 0 for city in destination_cities):
            return actions
        
        # Generate all possible actions from the current city
        for neighbor, cost in adjacency_matrix[current_city].items():
            if remaining_visits.get(neighbor, 0) > 0:
                new_remaining_visits = remaining_visits.copy()
                new_remaining_visits[neighbor] -= 1
                new_cost = g + cost
                
                if neighbor not in visited_costs or new_cost < visited_costs[neighbor]:
                    visited_costs[neighbor] = new_cost
                    heappush(queue, (new_cost, new_cost, actions + [neighbor], neighbor, new_remaining_visits))
    
    return None

print(a_star())
