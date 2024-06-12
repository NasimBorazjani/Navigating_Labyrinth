
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary of dictionaries
    adjacency_matrix = {
        'Y': {'O': 1, 'R': 1, 'A': 1, 'U': 1, 'M': 1},
        'O': {'Q': 1},
        'Q': {'Y': 1, 'K': 1, 'M': 1},
        'X': {'Y': 1, 'Q': 1, 'K': 1, 'A': 1},
        'K': {'O': 1, 'Q': 1, 'R': 1},
        'R': {'K': 1},
        'A': {'Q': 1, 'X': 1, 'M': 1},
        'U': {'L': 1},
        'M': {'Q': 1},
        'L': {'K': 1}
    }
    
    # Define the start city, the two destination cities, and the number of times we need to visit each destination
    start_city = 'U'
    destinations = ['A', 'X']
    num_visits = 2
    
    # Initialize a priority queue to store the paths to be explored, with the initial path as the first element
    queue = []
    heapq.heappush(queue, (0, [start_city], {start_city: 1}))
    
    # While there are paths to explore
    while queue:
        _, path, visited = heapq.heappop(queue)
        
        # Check if we have visited both destination cities the required number of times
        if all(visited.get(dest, 0) == num_visits for dest in destinations):
            return path
        
        # Get the current city from the path
        current_city = path[-1]
        
        # Explore all possible next cities to visit
        for next_city in adjacency_matrix[current_city]:
            # Check if the next city has not been visited yet
            if next_city not in visited:
                # Create a new path by adding the next city to the current path
                new_path = path + [next_city]
                # Create a new visited dictionary with the updated visit count for the next city
                new_visited = visited.copy()
                new_visited[next_city] = new_visited.get(next_city, 0) + 1
                # Calculate the cost of the new path (number of cities visited)
                new_cost = len(new_path)
                # Add the new path to the priority queue
                heapq.heappush(queue, (new_cost, new_path, new_visited))
    
    return None

print(a_star())
