
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary of dictionaries
    adjacency_matrix = {
        'G': {'G': 0, 'P': 0, 'H': 0, 'I': 0, 'J': 0, 'X': 1, 'D': 1, 'V': 0, 'Q': 0, 'L': 0, 'Y': 1},
        'P': {'G': 0, 'P': 0, 'H': 1, 'I': 1, 'J': 1, 'X': 0, 'D': 0, 'V': 0, 'Q': 0, 'L': 0, 'Y': 0},
        'H': {'G': 1, 'P': 1, 'H': 0, 'I': 0, 'J': 0, 'X': 1, 'D': 0, 'V': 0, 'Q': 1, 'L': 0, 'Y': 0},
        'I': {'G': 1, 'P': 0, 'H': 0, 'I': 0, 'J': 0, 'X': 0, 'D': 0, 'V': 0, 'Q': 0, 'L': 0, 'Y': 0},
        'J': {'G': 1, 'P': 0, 'H': 1, 'I': 1, 'J': 0, 'X': 0, 'D': 0, 'V': 0, 'Q': 0, 'L': 1, 'Y': 0},
        'X': {'G': 0, 'P': 0, 'H': 0, 'I': 0, 'J': 0, 'X': 0, 'D': 0, 'V': 1, 'Q': 0, 'L': 0, 'Y': 1},
        'D': {'G': 0, 'P': 1, 'H': 0, 'I': 0, 'J': 0, 'X': 1, 'D': 0, 'V': 0, 'Q': 0, 'L': 0, 'Y': 1},
        'V': {'G': 1, 'P': 0, 'H': 0, 'I': 0, 'J': 0, 'X': 1, 'D': 0, 'V': 0, 'Q': 0, 'L': 0, 'Y': 1},
        'Q': {'G': 1, 'P': 0, 'H': 1, 'I': 0, 'J': 1, 'X': 0, 'D': 1, 'V': 0, 'Q': 0, 'L': 1, 'Y': 0},
        'L': {'G': 0, 'P': 0, 'H': 1, 'I': 0, 'J': 0, 'X': 0, 'D': 0, 'V': 1, 'Q': 0, 'L': 0, 'Y': 0},
        'Y': {'G': 1, 'P': 0, 'H': 0, 'I': 1, 'J': 1, 'X': 1, 'D': 0, 'V': 0, 'Q': 0, 'L': 1, 'Y': 0}
    }
    
    # Define the initial state as being in city 'D'
    initial_state = 'D'
    # Define the goal state as visiting cities 'G' and 'Q' twice each
    goal_state = ['G', 'Q', 'G', 'Q']
    
    # Initialize a dictionary to store the cost of reaching each visited city
    visited_costs = {}
    visited_costs[initial_state] = 0
    
    # Initialize a priority queue of cities not yet visited, with the initial state as the first element
    queue = [(0, 0, [], initial_state)]
    
    while queue:
        _, g, actions, current_city = heapq.heappop(queue)
        
        # If we have visited both 'G' and 'Q' twice each, return the path taken
        if all(goal_state.count(city) == actions.count(city) for city in goal_state):
            return actions
        
        # Generate all possible actions from the current city, which includes moving to any directly connected city
        for next_city in adjacency_matrix[current_city]:
            # Check if the new city is not already visited
            if next_city not in actions:
                # Calculate the cost of moving to the new city
                new_cost = g + 1
                # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of unvisited cities
                if next_city not in visited_costs or new_cost < visited_costs[next_city]:
                    visited_costs[next_city] = new_cost
                    heapq.heappush(queue, (new_cost, new_cost, actions + [next_city], next_city))
    
    return None

print(a_star())
