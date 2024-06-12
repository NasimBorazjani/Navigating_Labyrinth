
import heapq


def a_star():
    # Define the adjacency matrix as a dictionary with city names as keys and a list of connected cities as values
    adjacency_matrix = {
        'S': ['I'],
        'U': ['X'],
        'X': ['R', 'K'],
        'D': ['U', 'Z'],
        'I': ['R', 'Q'],
        'Z': ['S', 'K'],
        'R': ['S', 'U'],
        'M': ['X'],
        'K': ['X', 'Q'],
        'Q': ['U', 'I']
    }
    
    # Define the initial state, goal state, and other variables
    initial_state = 'D'
    goal_state = ['K', 'Q']
    visited = set()
    path = []
    
    # Initialize a priority queue to store the cities to visit, with the initial state as the first element
    queue = [(0, initial_state, path)]
    
    # While there are cities to visit
    while queue:
        _, current_city, path = heapq.heappop(queue)
        
        # If we reach one of the goal cities, add it to the visited set
        if current_city in goal_state:
            visited.add(current_city)
        
        # If we have visited both goal cities twice, return the path
        if len(visited) == 2 and visited == set(goal_state):
            return path
        
        # Add the current city to the path
        path.append(current_city)
        
        # Add the connected cities to the queue
        for city in adjacency_matrix[current_city]:
            if city not in path:
                # Calculate the priority based on the number of visited goal cities
                priority = len(set(path) & set(goal_state))
                heapq.heappush(queue, (priority, city, path[:]))
    
    return None


print(a_star())
