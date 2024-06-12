
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries of connected cities
    adjacency_matrix = {
        'L': {'M': 1},
        'A': {'L': 1, 'E': 1, 'P': 1},
        'J': {'Q': 1, 'H': 1, 'K': 1},
        'U': {'E': 1, 'K': 1, 'M': 1},
        'E': {'Q': 1},
        'P': {'Q': 1, 'K': 1},
        'Q': {'J': 1, 'H': 1, 'K': 1},
        'Y': {'L': 1, 'A': 1, 'H': 1},
        'H': {'Y': 1, 'A': 1, 'P': 1, 'K': 1},
        'R': {'M': 1},
        'K': {'U': 1, 'P': 1, 'Q': 1},
        'M': {'F': 1},
        'F': {'A': 1, 'P': 1}
    }
    
    # Define the initial state, goal state, and other variables
    initial_state = 'L'
    goal_state = ['J', 'K']
    num_visits = {city: 0 for city in goal_state}
    
    visited_costs = {}
    visited_costs[initial_state] = 0
    
    queue = [(0, 0, [], initial_state)]
    
    while queue:
        _, g, actions, current_city = heapq.heappop(queue)
        
        # Check if we have visited both destination cities twice
        if all(num_visits[city] == 2 for city in goal_state):
            return actions
        
        # Generate all possible actions from the current city
        for next_city in adjacency_matrix[current_city]:
            # Check if we have not visited the next city before
            if num_visits[next_city] < 2:
                # Update the number of visits to the next city
                num_visits[next_city] += 1
                # Generate the new state
                new_state = next_city
                # The cost so far is the number of actions taken
                new_cost = g + 1
                
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # Calculate the heuristic as the number of remaining visits to the destination cities
                    h = sum(2 - num_visits[city] for city in goal_state)
                    heapq.heappush(queue, (new_cost + h, new_cost, actions + [next_city], new_state))
    
    return None

print(a_star())
