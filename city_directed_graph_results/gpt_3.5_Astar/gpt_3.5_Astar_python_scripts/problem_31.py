
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'S': {'E': 1},
        'A': {'J': 1, 'B': 1, 'L': 1},
        'J': {'A': 1, 'F': 1},
        'U': {'S': 1, 'N': 1, 'P': 1},
        'E': {'A': 1},
        'B': {'E': 1, 'N': 1},
        'N': {'A': 1, 'B': 1, 'P': 1, 'L': 1, 'F': 1},
        'P': {'J': 1, 'L': 1},
        'L': {'U': 1, 'X': 1},
        'X': {'U': 1, 'P': 1},
        'F': {'A': 1, 'N': 1}
    }
    
    # Define the initial state, goal state, and other variables
    initial_state = 'J'
    goal_state = ['U', 'E']
    num_visits = {city: 0 for city in goal_state}
    
    visited_costs = {}
    visited_costs[initial_state] = 0
    
    queue = []
    heapq.heappush(queue, (0, 0, [], initial_state))
    
    while queue:
        _, g, actions, current_city = heapq.heappop(queue)
        
        # Check if we have visited both destination cities twice
        if num_visits['U'] == 2 and num_visits['E'] == 2:
            return actions
        
        # Generate all possible actions from the current city
        for neighbor in adjacency_matrix[current_city]:
            # Check if we can visit the neighbor city
            if num_visits.get(neighbor, 0) < 2:
                # Update the number of visits to the destination cities
                if neighbor in goal_state:
                    num_visits[neighbor] += 1
                
                # Generate the new state
                new_cost = g + 1
                if neighbor not in visited_costs or new_cost < visited_costs[neighbor]:
                    visited_costs[neighbor] = new_cost
                    heapq.heappush(queue, (new_cost, new_cost, actions + [neighbor], neighbor))
    
    return None

print(a_star())
