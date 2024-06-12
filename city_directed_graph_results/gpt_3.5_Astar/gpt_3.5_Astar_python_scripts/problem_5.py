
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'K': {'Z': 1, 'S': 1, 'H': 1, 'E': 1},
        'B': {'O': 1, 'H': 1},
        'Z': {'B': 1, 'S': 1, 'O': 1, 'V': 1},
        'S': {'K': 1, 'Z': 1, 'X': 1},
        'X': {'K': 1, 'B': 1, 'V': 1},
        'H': {'S': 1, 'O': 1, 'E': 1},
        'O': {'Z': 1, 'S': 1, 'H': 1},
        'E': {'K': 1, 'O': 1, 'V': 1},
        'U': {'O': 1, 'E': 1},
        'V': {'X': 1}
    }
    
    # Define the start city, the goal cities, and the number of times we need to visit each goal city
    start_city = 'H'
    goal_cities = ['Z', 'K']
    goal_count = {city: 2 for city in goal_cities}
    
    # Initialize the priority queue with the start city and the initial cost
    queue = [(0, [start_city])]
    
    while queue:
        _, path = heapq.heappop(queue)
        current_city = path[-1]
        
        # Check if we have visited both goal cities twice
        if all(goal_count[city] == 0 for city in goal_cities):
            return path
        
        # Explore all possible next cities to visit
        for neighbor, _ in adjacency_matrix[current_city].items():
            if neighbor not in path:
                new_path = path + [neighbor]
                new_cost = len(new_path) - 1  # Cost is the number of cities visited so far
                
                # Update the number of times we need to visit each goal city
                if neighbor in goal_cities:
                    goal_count[neighbor] -= 1
                
                # Add the new path to the priority queue
                heapq.heappush(queue, (new_cost, new_path))
    
    return None

print(a_star())
