
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'S': {'X': 1, 'V': 1, 'F': 1},
        'X': {'O': 1, 'R': 1},
        'Y': {'S': 1, 'X': 1, 'R': 1},
        'Q': {'X': 1, 'D': 1},
        'O': {'R': 1, 'D': 1},
        'R': {'X': 1, 'H': 1, 'F': 1},
        'D': {'S': 1, 'H': 1},
        'V': {'Y': 1, 'D': 1, 'J': 1},
        'H': {'X': 1, 'V': 1, 'F': 1},
        'J': {'Y': 1, 'R': 1},
        'F': {'D': 1, 'C': 1},
        'C': {'S': 1, 'H': 1}
    }
    
    # Define the initial state, goal state, and other variables
    initial_state = 'Q'
    goal_state = ['V', 'F']
    num_visits = 2
    visited = {initial_state: 1}
    queue = [(0, [initial_state], initial_state)]
    
    while queue:
        _, path, current_city = heapq.heappop(queue)
        
        # Check if we have visited both destination cities twice
        if path.count('V') == num_visits and path.count('F') == num_visits:
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
