
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the city names and the values are lists of connected cities
    adjacency_matrix = {
        'K': ['I', 'X'],
        'I': ['Y', 'J', 'U'],
        'E': ['D', 'J'],
        'B': ['J'],
        'Y': ['K', 'D'],
        'J': ['E', 'Y', 'U', 'F'],
        'U': ['L', 'J'],
        'D': ['L', 'A'],
        'L': ['I', 'X', 'J'],
        'A': ['E', 'D'],
        'X': ['Y', 'I', 'C'],
        'C': ['L', 'F'],
        'F': ['L'],
        'V': ['E', 'Y', 'J']
    }
    
    # Define the initial state and goal state
    initial_state = 'V'
    goal_state = ['E', 'U']
    
    # Initialize a priority queue to store the states to be visited, with the initial state as the first element
    queue = [(0, [initial_state], initial_state)]
    
    # While there are states to visit
    while queue:
        _, path, current_city = heapq.heappop(queue)
        
        # If we have visited both destination cities twice, return the path
        if path.count('E') == 2 and path.count('U') == 2:
            return path
        
        # Explore the neighbors of the current city
        for neighbor in adjacency_matrix[current_city]:
            # Check if the neighbor has not been visited before
            if neighbor not in path:
                # Calculate the cost of the path so far
                cost = len(path)
                # Calculate the heuristic (distance to the goal) as the number of remaining destination cities to visit
                heuristic = 4 - path.count('E') - path.count('U')
                # Add the neighbor to the path and push the new state to the priority queue
                heapq.heappush(queue, (cost + heuristic, path + [neighbor], neighbor))
    
    return None

print(a_star())
