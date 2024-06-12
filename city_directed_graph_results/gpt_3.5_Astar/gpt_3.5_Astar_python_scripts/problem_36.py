
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'F': {'U': 1, 'R': 1},
        'I': {'C': 1, 'L': 1, 'Q': 1},
        'C': {'I': 1, 'L': 1, 'Q': 1},
        'G': {'F': 1, 'I': 1, 'L': 1},
        'N': {'F': 1, 'U': 1},
        'L': {'C': 1, 'I': 1, 'G': 1, 'X': 1},
        'X': {'C': 1, 'I': 1, 'Q': 1, 'U': 1},
        'Q': {'C': 1, 'X': 1, 'U': 1},
        'U': {'F': 1, 'N': 1, 'X': 1, 'Q': 1},
        'R': {'I': 1, 'C': 1, 'G': 1, 'O': 1},
        'O': {'L': 1, 'X': 1, 'Q': 1, 'R': 1},
        'B': {'C': 1, 'L': 1, 'Q': 1}
    }
    
    # Define the initial state, goal state, and other variables
    initial_state = 'G'
    goal_state = ['O', 'R', 'O', 'R']
    visited = set()
    queue = [(0, initial_state, [])]
    
    # While there are unvisited cities in the queue
    while queue:
        _, current_city, path = heapq.heappop(queue)
        
        # If we have visited both O and R twice, return the path
        if path.count('O') == 2 and path.count('R') == 2:
            return path + [current_city]
        
        # Add the current city to the visited set
        visited.add(current_city)
        
        # Explore the neighboring cities
        for neighbor, _ in adjacency_matrix[current_city].items():
            if neighbor not in visited:
                # Add the neighbor to the queue with updated path and cost
                new_path = path + [current_city]
                new_cost = len(new_path)
                heapq.heappush(queue, (new_cost, neighbor, new_path))
    
    return None

print(a_star())
