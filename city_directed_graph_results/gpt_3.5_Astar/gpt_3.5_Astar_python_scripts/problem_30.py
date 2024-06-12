
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary
    adjacency_matrix = {
        'S': {'V': 1, 'U': 1, 'W': 0, 'G': 0, 'E': 1, 'H': 1, 'P': 0, 'T': 0, 'Q': 0, 'Z': 0},
        'V': {'S': 0, 'U': 0, 'W': 0, 'G': 0, 'E': 0, 'H': 0, 'P': 1, 'T': 0, 'Q': 0, 'Z': 0},
        'U': {'S': 0, 'V': 1, 'W': 0, 'G': 0, 'E': 0, 'H': 0, 'P': 1, 'T': 0, 'Q': 1, 'Z': 0},
        'W': {'S': 1, 'V': 1, 'U': 0, 'G': 0, 'E': 0, 'H': 0, 'P': 0, 'T': 0, 'Q': 0, 'Z': 1},
        'G': {'S': 0, 'V': 1, 'U': 1, 'W': 0, 'E': 0, 'H': 0, 'P': 0, 'T': 0, 'Q': 0, 'Z': 0},
        'E': {'S': 1, 'V': 0, 'U': 0, 'W': 0, 'G': 0, 'H': 0, 'P': 0, 'T': 1, 'Q': 0, 'Z': 0},
        'H': {'S': 0, 'V': 1, 'U': 0, 'W': 1, 'G': 0, 'E': 0, 'P': 0, 'T': 0, 'Q': 0, 'Z': 1},
        'P': {'S': 0, 'V': 0, 'U': 0, 'W': 0, 'G': 0, 'E': 1, 'H': 1, 'T': 0, 'Q': 0, 'Z': 0},
        'T': {'S': 0, 'V': 0, 'U': 0, 'W': 0, 'G': 1, 'E': 0, 'H': 0, 'P': 1, 'Q': 0, 'Z': 0},
        'Q': {'S': 0, 'V': 0, 'U': 0, 'W': 0, 'G': 0, 'E': 0, 'H': 1, 'P': 1, 'T': 0, 'Z': 0},
        'Z': {'S': 0, 'V': 1, 'U': 0, 'W': 1, 'G': 0, 'E': 0, 'H': 0, 'P': 0, 'T': 1, 'Q': 0}
    }
    
    # Define the initial state, goal state, and other variables
    initial_state = 'G'
    goal_state = ['H', 'P']
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
        for next_city, connected in adjacency_matrix[current_city].items():
            if connected == 1:
                # Update the number of visits to the destination cities
                if next_city in goal_state:
                    num_visits[next_city] += 1
                
                # Generate the new state
                new_cost = g + 1
                if next_city not in visited_costs or new_cost < visited_costs[next_city]:
                    visited_costs[next_city] = new_cost
                    heapq.heappush(queue, (new_cost, new_cost, actions + [next_city], next_city))
    
    return None

print(a_star())
