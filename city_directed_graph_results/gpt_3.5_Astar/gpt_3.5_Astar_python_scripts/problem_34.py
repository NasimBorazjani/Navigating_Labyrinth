
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'J': {'N': 1},
        'S': {'W': 1, 'G': 1},
        'T': {'B': 1},
        'W': {'J': 1, 'S': 1, 'G': 1, 'P': 1, 'U': 1},
        'G': {'S': 1, 'W': 1, 'B': 1},
        'N': {'T': 1, 'W': 1, 'G': 1, 'P': 1, 'U': 1},
        'M': {},
        'Z': {'N': 1, 'B': 1, 'U': 1},
        'B': {'S': 1, 'W': 1, 'G': 1, 'Z': 1},
        'P': {'T': 1, 'N': 1, 'Z': 1},
        'U': {'W': 1, 'G': 1, 'N': 1}
    }
    
    # Define the initial state, goal state, and other variables
    initial_state = 'T'
    goal_state = ['N', 'W']
    num_visits = {city: 0 for city in goal_state}
    path = [initial_state]
    
    # Initialize a priority queue to store the cities to visit, with the initial state as the first element
    queue = [(0, initial_state, path, num_visits)]
    
    while queue:
        _, current_city, current_path, current_visits = heapq.heappop(queue)
        
        # Check if we have visited both destination cities twice
        if all(value == 2 for value in current_visits.values()):
            return current_path
        
        # Explore the connections of the current city
        for neighbor, _ in adjacency_matrix[current_city].items():
            # Check if we can visit the neighbor city
            if current_visits[neighbor] < 2:
                # Update the number of visits to the neighbor city
                new_visits = current_visits.copy()
                new_visits[neighbor] += 1
                # Add the neighbor city to the path
                new_path = current_path + [neighbor]
                # Calculate the cost of the path (number of cities visited)
                cost = len(new_path)
                # Add the new path to the priority queue
                heapq.heappush(queue, (cost, neighbor, new_path, new_visits))
    
    return None

print(a_star())
