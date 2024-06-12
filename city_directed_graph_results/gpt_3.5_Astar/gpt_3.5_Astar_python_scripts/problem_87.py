
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are lists of connected cities
    adjacency_matrix = {
        'A': ['Z', 'O', 'L', 'X', 'E', 'T', 'W', 'D', 'S', 'Q'],
        'P': ['R', 'I', 'S', 'G', 'Q'],
        'Z': ['O', 'L', 'I', 'W'],
        'O': ['R', 'I', 'S', 'D'],
        'R': ['A', 'P', 'I', 'L', 'X', 'T', 'W', 'D', 'S', 'G', 'Q'],
        'I': ['X', 'E', 'T', 'W', 'D', 'S', 'G', 'Q'],
        'L': ['A', 'P', 'O', 'R', 'X', 'T', 'W', 'D', 'S', 'Q'],
        'X': ['E', 'T', 'W', 'D', 'S', 'G', 'Q'],
        'E': ['O', 'L', 'X', 'T', 'W', 'D', 'S', 'Q'],
        'T': ['W', 'D', 'S', 'G', 'Q'],
        'W': ['Z', 'O', 'L', 'X', 'E', 'T', 'D', 'S', 'G', 'Q'],
        'D': ['A', 'P', 'O', 'R', 'I', 'L', 'X', 'E', 'T', 'W', 'S', 'G', 'Q'],
        'S': ['A', 'P', 'Z', 'O', 'R', 'I', 'L', 'X', 'E', 'T', 'W', 'D', 'G', 'Q'],
        'G': ['P', 'Z', 'O', 'R', 'I', 'L', 'X', 'E', 'T', 'W', 'D', 'S', 'Q'],
        'Q': ['A', 'Z', 'O', 'R', 'I', 'L', 'X', 'E', 'T', 'W', 'D', 'S', 'G']
    }
    
    # Define the start city
    start_city = 'E'
    # Define the goal cities
    goal_cities = ['A', 'P']
    
    visited = set()
    queue = []
    # Start at city E with 0 cost and an empty path
    heapq.heappush(queue, (0, start_city, []))
    
    while queue:
        cost, current_city, path = heapq.heappop(queue)
        
        # If we reach a goal city, add it to the path
        if current_city in goal_cities:
            path.append(current_city)
            # If we have visited both goal cities twice, return the path
            if path.count('A') == 2 and path.count('P') == 2:
                return path
        
        # Add the current city to the visited set
        visited.add(current_city)
        
        # Explore the neighbors of the current city
        for neighbor in adjacency_matrix[current_city]:
            # If the neighbor has not been visited, add it to the queue with the updated cost and path
            if neighbor not in visited:
                heapq.heappush(queue, (cost + 1, neighbor, path + [current_city]))
    
    return None

print(a_star())
