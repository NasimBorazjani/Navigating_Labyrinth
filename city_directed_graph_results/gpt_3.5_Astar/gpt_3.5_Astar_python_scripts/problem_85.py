
import heapq


def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'I': {'S': 1},
        'P': {'G': 1, 'S': 1, 'A': 1, 'D': 1, 'E': 1},
        'G': {'I': 1, 'P': 1, 'U': 1, 'H': 1, 'X': 1},
        'S': {'Y': 1, 'A': 1},
        'Y': {'S': 1},
        'A': {'P': 1, 'E': 1},
        'D': {'U': 1, 'H': 1},
        'U': {'P': 1, 'G': 1, 'E': 1, 'W': 1, 'V': 1},
        'E': {'A': 1, 'U': 1},
        'W': {'D': 1, 'Z': 1},
        'V': {'I': 1, 'P': 1, 'G': 1, 'Z': 1},
        'H': {'A': 1, 'D': 1, 'U': 1},
        'Z': {'W': 1, 'V': 1},
        'X': {'P': 1, 'G': 1, 'U': 1, 'V': 1}
    }
    
    # Define the initial state, goal state, and other variables
    initial_city = 'Y'
    goal_cities = ['H', 'X']
    num_visits = 2
    visited = {initial_city: 1}
    queue = [(0, [initial_city], initial_city)]
    
    # While there are cities to visit in the queue
    while queue:
        _, path, current_city = heapq.heappop(queue)
        
        # Check if we have visited both goal cities twice
        if path.count('H') == num_visits and path.count('X') == num_visits:
            return path
        
        # Explore all possible connections from the current city
        for neighbor, cost in adjacency_matrix[current_city].items():
            if neighbor not in visited or visited[neighbor] < num_visits:
                visited_cities = visited.copy()
                visited_cities[neighbor] = visited_cities.get(neighbor, 0) + 1
                new_path = path + [neighbor]
                new_cost = len(new_path)
                heapq.heappush(queue, (new_cost, new_path, neighbor))
    
    return None


print(a_star())
