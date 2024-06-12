
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary
    adjacency_matrix = {
        'O': {'Q', 'Z'},
        'M': {'L'},
        'U': {'M', 'L', 'Q', 'B', 'K'},
        'L': {'O', 'P', 'D', 'A', 'K'},
        'Q': {'L', 'P', 'D', 'A', 'S', 'K', 'E'},
        'P': {'U', 'D', 'B', 'Z'},
        'D': {'M', 'U', 'P', 'S', 'K'},
        'A': {'M', 'U', 'B', 'E', 'Z'},
        'S': {'O', 'M', 'B'},
        'B': {'U', 'L', 'A', 'K'},
        'K': {'U', 'L', 'Q', 'D', 'B', 'V', 'Z'},
        'V': {'O', 'Z'},
        'E': {'O', 'Z'},
        'Z': {'P', 'A', 'K', 'V', 'E'}
    }
    
    # Define the start city
    start_city = 'M'
    # Define the destination cities
    destinations = ['L', 'Z']
    
    visited = set()  # Set to keep track of visited cities
    path = []  # List to store the path taken
    
    # Initialize a priority queue to store the cities to visit, with the start city as the first element
    queue = [(0, start_city, [start_city])]
    
    while queue:
        _, current_city, current_path = heapq.heappop(queue)
        
        # If the current city is one of the destination cities and it has been visited once, add it to the path
        if current_city in destinations and current_path.count(current_city) == 1:
            path.extend(current_path)
            visited.add(current_city)
        
        # If both destination cities have been visited twice, return the path
        if 'L' in visited and 'Z' in visited and current_path.count('L') == 2 and current_path.count('Z') == 2:
            return path
        
        # Add the current city to the visited set
        visited.add(current_city)
        
        # Explore the neighbors of the current city
        for neighbor in adjacency_matrix[current_city]:
            if neighbor not in visited:
                new_path = current_path + [neighbor]
                # Calculate the cost of the path based on the number of cities visited
                cost = len(new_path)
                heapq.heappush(queue, (cost, neighbor, new_path))
    
    return None

print(a_star())
