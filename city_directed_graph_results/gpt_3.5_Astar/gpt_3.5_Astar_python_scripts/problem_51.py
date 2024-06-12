
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'O': {'B': 1},
        'C': {'O': 1, 'F': 1, 'P': 1},
        'F': {'C': 1, 'U': 1, 'H': 1, 'Q': 1},
        'W': {'O': 1, 'C': 1, 'I': 1, 'P': 1},
        'I': {'C': 1, 'W': 1, 'P': 1, 'H': 1, 'Q': 1, 'S': 1},
        'P': {'C': 1, 'F': 1, 'I': 1, 'B': 1},
        'U': {'F': 1, 'W': 1},
        'B': {'P': 1, 'F': 1},
        'H': {'F': 1, 'I': 1, 'Q': 1, 'S': 1},
        'Q': {'F': 1, 'I': 1, 'H': 1, 'S': 1},
        'G': {'P': 1},
        'S': {'I': 1, 'H': 1}
    }
    
    # Define the initial state, goal state, and other variables
    initial_state = 'G'
    goal_state = ['F', 'U', 'F', 'U']
    visited = set()
    path = []
    
    # Initialize a priority queue to store the cities to visit, with the initial state as the first element
    queue = [(0, initial_state, [])]
    
    # While there are cities to visit in the queue
    while queue:
        _, current_city, current_path = heapq.heappop(queue)
        
        # If we reach one of the goal states, add it to the path and mark it as visited
        if current_city in goal_state:
            path.append(current_city)
            visited.add(current_city)
            
            # If we have visited both F and U twice, return the path
            if path.count('F') == 2 and path.count('U') == 2:
                return current_path + path
        
        # Add the current city to the path and mark it as visited
        current_path = current_path + [current_city]
        visited.add(current_city)
        
        # Explore the connections of the current city
        for neighbor, _ in adjacency_matrix[current_city].items():
            if neighbor not in visited:
                # Calculate the cost of reaching the neighbor (not used in this problem)
                cost = 1
                # Calculate the heuristic (not used in this problem)
                heuristic = 0
                # Add the neighbor to the queue with the updated path
                heapq.heappush(queue, (cost + heuristic, neighbor, current_path))
    
    return None

print(a_star())
