
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'Y': {'J': 1},
        'E': {'D': 1, 'G': 1},
        'L': {'B': 1, 'E': 1, 'K': 1},
        'P': {'C': 1},
        'M': {'D': 1, 'K': 1},
        'C': {'D': 1, 'E': 1, 'G': 1},
        'B': {'J': 1, 'D': 1, 'K': 1},
        'I': {'A': 1, 'B': 1, 'D': 1, 'H': 1},
        'G': {'A': 1, 'B': 1, 'E': 1},
        'V': {'E': 1},
        'J': {'D': 1, 'F': 1, 'K': 1, 'L': 1},
        'T': {'F': 1, 'H': 1, 'I': 1}
    }
    
    # Define the start city, the two destination cities, and the number of times we need to visit each destination
    start_city = 'Y'
    destination_cities = ['E', 'M']
    num_visits = 2
    
    # Initialize a priority queue to store the paths to explore, with the initial path containing only the start city
    queue = []
    heapq.heappush(queue, (0, [start_city], {start_city: 1}))
    
    # While there are paths to explore
    while queue:
        _, path, visited = heapq.heappop(queue)
        
        # Get the last city visited in the path
        current_city = path[-1]
        
        # Check if we have visited both destination cities the required number of times
        if visited.get('E', 0) == num_visits and visited.get('M', 0) == num_visits:
            return path
        
        # Explore all possible connections from the current city
        for neighbor, _ in adjacency_matrix[current_city].items():
            # Check if we have not visited the neighbor city before
            if neighbor not in visited:
                # Create a new path by extending the current path
                new_path = path + [neighbor]
                # Create a new visited dictionary by updating the count of visits to the neighbor city
                new_visited = visited.copy()
                new_visited[neighbor] = new_visited.get(neighbor, 0) + 1
                # Calculate the cost of the new path (number of cities visited)
                cost = len(new_path)
                # Add the new path to the priority queue
                heapq.heappush(queue, (cost, new_path, new_visited))
    
    return None

print(a_star())
