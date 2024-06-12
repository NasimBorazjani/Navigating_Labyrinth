
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'J': {'H': 1, 'L': 1, 'F': 1, 'A': 1, 'P': 1, 'D': 1, 'R': 1, 'T': 1, 'Z': 1, 'N': 1},
        'H': {'J': 1},
        'X': {'H': 1, 'D': 1},
        'L': {'X': 1, 'F': 1, 'A': 1, 'M': 1, 'R': 1, 'Z': 1},
        'F': {'D': 1, 'R': 1},
        'A': {'J': 1, 'L': 1, 'D': 1},
        'P': {'M': 1, 'Z': 1, 'N': 1},
        'M': {'L': 1, 'D': 1, 'R': 1, 'T': 1, 'Z': 1},
        'D': {'M': 1, 'R': 1, 'T': 1},
        'R': {'H': 1, 'M': 1, 'P': 1, 'Z': 1},
        'T': {'J': 1, 'H': 1, 'L': 1, 'M': 1, 'Z': 1},
        'Z': {'H': 1, 'M': 1, 'P': 1, 'N': 1},
        'N': {'L': 1, 'F': 1, 'P': 1, 'Z': 1},
        'K': {'J': 1, 'H': 1, 'X': 1}
    }
    
    # Define the start city
    start_city = 'X'
    # Define the destination cities that need to be visited twice
    destinations = ['K', 'N']
    
    visited_costs = {}
    visited_costs[(start_city, 0, 0)] = 0
    
    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], start_city, 0))
    
    while queue:
        _, g, actions, current_city, num_destinations_visited = heappop(queue)
        
        # Check if we have visited both destination cities twice
        if num_destinations_visited == 2:
            return actions
        
        # Generate all possible actions from the current city
        for neighbor, cost in adjacency_matrix[current_city].items():
            # Check if visiting the neighbor city is valid
            if neighbor not in actions and (neighbor not in destinations or actions.count(neighbor) < 2):
                new_num_destinations_visited = num_destinations_visited + 1 if neighbor in destinations else num_destinations_visited
                new_cost = g + cost
                new_actions = actions + [neighbor]
                
                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of unvisited states
                if (neighbor, new_num_destinations_visited) not in visited_costs or new_cost < visited_costs[(neighbor, new_num_destinations_visited)]:
                    visited_costs[(neighbor, new_num_destinations_visited)] = new_cost
                    heappush(queue, (new_cost, new_num_destinations_visited, new_actions, neighbor, new_num_destinations_visited))
    
    return None

print(a_star())
