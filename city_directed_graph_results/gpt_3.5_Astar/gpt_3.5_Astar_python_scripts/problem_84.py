
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries of connected cities
    adjacency_matrix = {
        'F': {'L', 'P', 'R', 'Q', 'B', 'T'},
        'O': {'L', 'Y', 'Q', 'B', 'V', 'A'},
        'L': {'F', 'O', 'P', 'R', 'Q', 'B', 'V', 'A'},
        'P': {'F', 'O', 'Y', 'Q', 'B', 'T'},
        'Y': {'O', 'Q', 'B', 'V', 'A'},
        'R': {'F', 'Y', 'Q', 'B', 'V'},
        'Q': {'O', 'R', 'B', 'T', 'V', 'A', 'K', 'H'},
        'B': {'F', 'O', 'P', 'R', 'Q', 'T', 'V', 'A', 'K', 'S'},
        'T': {'F', 'Q', 'V', 'K'},
        'V': {'O', 'B', 'T', 'A', 'K', 'S', 'H'},
        'A': {'O', 'L', 'B', 'V', 'K', 'H'},
        'K': {'O', 'B', 'A', 'H'},
        'S': {'B', 'V', 'A', 'H'},
        'H': {'Q', 'V', 'A', 'K', 'S'}
    }
    
    # Define the initial state, goal state, and other variables
    initial_state = 'T'
    goal_state = {'H', 'K'}
    visited = set()
    path = []
    
    # Initialize a priority queue with the initial state
    queue = [(0, initial_state, path)]
    
    while queue:
        # Pop the city with the lowest cost so far from the queue
        cost, current_city, path = heapq.heappop(queue)
        
        # If we reach one of the goal states, add it to the visited set
        if current_city in goal_state:
            visited.add(current_city)
        
        # If we have visited both goal states twice, return the path
        if visited == goal_state:
            return path
        
        # Add the current city to the visited set
        visited.add(current_city)
        
        # Explore the neighbors of the current city
        for neighbor in adjacency_matrix[current_city]:
            # If the neighbor has not been visited, calculate the cost and add it to the queue
            if neighbor not in visited:
                new_cost = cost + 1
                new_path = path + [neighbor]
                heapq.heappush(queue, (new_cost, neighbor, new_path))
    
    return None

print(a_star())
