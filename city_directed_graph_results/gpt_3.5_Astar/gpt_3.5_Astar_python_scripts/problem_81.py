
import heapq


def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'T': {'L': 1, 'S': 1, 'H': 1},
        'J': {'L': 1},
        'X': {'J': 1, 'U': 1, 'H': 1},
        'U': {'C': 1, 'Z': 1},
        'L': {'U': 1, 'D': 1},
        'S': {'H': 1, 'O': 1},
        'C': {'T': 1, 'X': 1, 'O': 1},
        'H': {'T': 1, 'S': 1, 'Z': 1, 'D': 1},
        'Z': {'J': 1, 'S': 1, 'O': 1},
        'O': {'D': 1, 'Q': 1},
        'D': {'J': 1, 'X': 1, 'G': 1},
        'Q': {'J': 1, 'X': 1},
        'G': {'T': 1, 'L': 1, 'H': 1},
        'W': {'J': 1, 'S': 1, 'O': 1}
    }
    
    # Define the initial state, which is the starting city 'U'
    initial_state = 'U'
    
    # Define the goal state, which is to visit cities 'H' and 'L' twice each
    goal_state = ['H', 'H', 'L', 'L']
    
    # Initialize a priority queue to store the states to be visited, with the initial state as the first element
    queue = [(0, initial_state, [])]
    
    # While there are states to visit
    while queue:
        _, current_city, path = heapq.heappop(queue)
        
        # If we have visited both 'H' and 'L' twice each, return the path
        if path.count('H') == 2 and path.count('L') == 2:
            return path + [current_city]
        
        # Generate all possible actions from the current city
        for neighbor, weight in adjacency_matrix[current_city].items():
            # Check if visiting the neighbor city is valid (not already visited)
            if neighbor not in path:
                # Calculate the cost of the new state
                new_cost = weight
                
                # Add the new state to the priority queue
                heapq.heappush(queue, (new_cost, neighbor, path + [current_city]))
    
    return None


print(a_star())
