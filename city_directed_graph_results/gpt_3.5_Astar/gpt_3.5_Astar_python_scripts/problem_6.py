
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries of connected cities
    adjacency_matrix = {
        'F': {'J': 1, 'K': 1, 'D': 0, 'N': 0, 'R': 0, 'M': 0, 'B': 1},
        'I': {'F': 1, 'K': 0, 'D': 0, 'N': 0, 'R': 0, 'M': 0, 'B': 1},
        'O': {'F': 0, 'J': 1, 'K': 0, 'D': 0, 'N': 0, 'R': 0, 'M': 1, 'B': 1},
        'J': {'F': 1, 'I': 0, 'O': 1, 'K': 0, 'D': 0, 'N': 0, 'R': 0, 'M': 0, 'B': 0},
        'K': {'J': 0, 'O': 1, 'D': 0, 'N': 0, 'R': 0, 'M': 1, 'B': 0},
        'D': {'I': 1, 'O': 1, 'K': 0, 'N': 0, 'R': 0, 'M': 0, 'B': 0},
        'N': {'I': 1, 'K': 0, 'D': 0, 'R': 0, 'M': 0, 'B': 0},
        'R': {'O': 1, 'M': 0, 'B': 1},
        'M': {'F': 1, 'I': 1, 'O': 0, 'J': 1, 'R': 0, 'B': 1},
        'B': {'F': 1, 'I': 0, 'O': 0, 'J': 1, 'K': 0, 'D': 0, 'N': 0, 'R': 1, 'M': 1}
    }
    
    # Define the initial state, which is the starting city 'N'
    initial_state = 'N'
    
    # Define the goal state, which is to visit cities 'D' and 'F' twice each
    goal_state = ['D', 'D', 'F', 'F']
    
    # Initialize a priority queue to store the states to be visited, with the initial state as the first element
    queue = [(0, [initial_state])]
    
    # While there are states to visit
    while queue:
        _, path = heapq.heappop(queue)
        current_city = path[-1]
        
        # If the current path satisfies the goal state, return the path
        if path.count('D') == 2 and path.count('F') == 2:
            return path
        
        # Generate all possible actions from the current state, which are the cities connected to the current city
        for neighbor, cost in adjacency_matrix[current_city].items():
            if neighbor not in path:
                new_path = path + [neighbor]
                # Calculate the cost of the new path, which is the sum of the costs of the edges traversed
                new_cost = sum(adjacency_matrix[new_path[i]][new_path[i+1]] for i in range(len(new_path) - 1))
                heapq.heappush(queue, (new_cost, new_path))
    
    return None

print(a_star())
