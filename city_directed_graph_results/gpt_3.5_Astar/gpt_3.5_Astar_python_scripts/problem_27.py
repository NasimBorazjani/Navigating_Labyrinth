
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'J': {'X': 1},
        'H': {'K': 1, 'B': 1, 'U': 1, 'I': 1},
        'K': {'I': 1},
        'W': {'H': 1, 'X': 1},
        'X': {'H': 1, 'I': 1},
        'I': {'K': 1, 'B': 1, 'U': 1, 'G': 1},
        'B': {'W': 1, 'Z': 1, 'G': 1},
        'U': {'W': 1, 'X': 1, 'I': 1},
        'D': {'W': 1, 'B': 1},
        'Z': {'J': 1, 'W': 1, 'X': 1, 'G': 1},
        'G': {'J': 1, 'X': 1}
    }
    
    # Define the initial state as being in city 'D'
    initial_state = 'D'
    # Define the goal state as visiting cities 'H' and 'Z' twice each
    goal_state = ['H', 'H', 'Z', 'Z']
    
    # Initialize a priority queue to store the states to be visited, with the initial state as the first element
    queue = [(0, [initial_state])]
    
    # While there are states to visit
    while queue:
        _, path = heapq.heappop(queue)
        current_city = path[-1]
        
        # If the current path satisfies the goal state, return the path
        if path.count('H') == 2 and path.count('Z') == 2:
            return path
        
        # Explore all possible next cities to visit from the current city
        for neighbor in adjacency_matrix[current_city]:
            # Ensure we only visit each city once (except for 'H' and 'Z')
            if neighbor not in path or neighbor in ['H', 'Z']:
                new_path = path + [neighbor]
                # Calculate the cost of the path (number of cities visited)
                cost = len(new_path)
                # Add the new path to the priority queue
                heapq.heappush(queue, (cost, new_path))
    
    return None

print(a_star())
