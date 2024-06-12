
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'I': {'E': 1},
        'H': {'A': 1, 'B': 1, 'C': 1, 'G': 1},
        'R': {'E': 1, 'F': 1, 'G': 1, 'J': 1, 'L': 1, 'Q': 1, 'S': 1, 'V': 1},
        'E': {'I': 1, 'H': 1},
        'G': {'B': 1, 'F': 1},
        'S': {'C': 1, 'H': 1, 'Q': 1, 'R': 1, 'V': 1},
        'W': {'R': 1},
        'Q': {'A': 1, 'C': 1, 'H': 1, 'S': 1},
        'C': {'A': 1, 'H': 1, 'Q': 1},
        'A': {'C': 1, 'H': 1},
        'B': {'G': 1, 'H': 1, 'Q': 1},
        'F': {'G': 1, 'R': 1},
        'J': {'R': 1},
        'V': {'Q': 1, 'R': 1, 'S': 1},
        'L': {'R': 1}
    }
    
    # Define the initial state, goal state, and other variables
    initial_state = 'F'
    goal_state = ['R', 'S']
    num_visits = {city: 0 for city in goal_state}
    
    visited_costs = {}
    visited_costs[initial_state] = 0
    
    queue = [(0, 0, [], initial_state, num_visits.copy())]
    
    while queue:
        _, g, actions, current_city, current_visits = heapq.heappop(queue)
        
        # If we have visited both destination cities twice, return the path
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
