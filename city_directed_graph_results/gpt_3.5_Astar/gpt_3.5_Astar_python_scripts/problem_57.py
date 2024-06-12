
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries of connected cities
    adjacency_matrix = {
        'V': {'C': 1, 'Y': 1, 'W': 1},
        'C': {'Y': 1, 'J': 1},
        'I': {'V': 1, 'C': 1, 'Y': 1, 'Q': 1},
        'Y': {'Z': 1, 'J': 1, 'F': 1},
        'W': {'C': 1, 'Q': 1, 'X': 1},
        'Q': {'X': 1, 'F': 1},
        'X': {'I': 1, 'Z': 1, 'J': 1},
        'K': {'W': 1, 'X': 1},
        'Z': {'I': 1, 'Y': 1, 'J': 1},
        'T': {'C': 1, 'W': 1, 'K': 1},
        'J': {'Z': 1, 'T': 1, 'U': 1},
        'U': {'I': 1, 'V': 1, 'C': 1},
        'F': {'J': 1}
    }
    
    # Define the initial state, goal state, and other variables
    initial_state = 'T'
    goal_state = ['V', 'I']
    num_visits = 2
    visited = {initial_state: 1}
    queue = [(0, [initial_state], initial_state)]
    
    while queue:
        _, path, current_city = heapq.heappop(queue)
        
        # Check if we have visited the goal cities the required number of times
        if path.count('V') == num_visits and path.count('I') == num_visits:
            return path
        
        # Explore all possible next cities to visit
        for next_city, connected in adjacency_matrix[current_city].items():
            if visited.get(next_city, 0) < num_visits:
                visited[next_city] = visited.get(next_city, 0) + 1
                new_path = path + [next_city]
                new_cost = len(new_path)
                heapq.heappush(queue, (new_cost, new_path, next_city))
    
    return None

print(a_star())
