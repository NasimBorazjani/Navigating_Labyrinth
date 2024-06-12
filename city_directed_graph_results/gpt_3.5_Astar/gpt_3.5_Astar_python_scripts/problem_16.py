
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries of connected cities
    adjacency_matrix = {
        'C': {'G': 1, 'P': 1},
        'V': {'P': 1},
        'A': {'V': 1, 'Z': 1},
        'G': {'Y': 1},
        'Y': {'G': 1, 'Z': 1},
        'P': {'Y': 1, 'Z': 1},
        'Z': {'Y': 1, 'P': 1, 'I': 1},
        'S': {'A': 1},
        'J': {'P': 1},
        'I': {'C': 1, 'Y': 1, 'Z': 1}
    }
    
    # Define the start city, destination cities, and the number of times each destination city should be visited
    start_city = 'S'
    destination_cities = ['P', 'G']
    visit_count = {city: 2 for city in destination_cities}
    
    # Initialize a priority queue to store the paths to be explored, starting with the start city
    queue = [(0, [start_city])]
    
    # While there are paths to explore
    while queue:
        # Pop the path with the lowest cost from the priority queue
        cost, path = heapq.heappop(queue)
        
        # Get the current city from the end of the path
        current_city = path[-1]
        
        # Check if we have visited both destination cities the required number of times
        if all(visit_count[city] == 0 for city in destination_cities):
            return path
        
        # Explore all possible next cities to visit from the current city
        for next_city in adjacency_matrix[current_city]:
            # Check if we can visit the next city and if we have not visited it before in the current path
            if visit_count.get(next_city, 0) > 0 and next_city not in path:
                # Update the visit count for the next city
                visit_count[next_city] -= 1
                # Calculate the new cost of the path
                new_cost = cost + 1
                # Create a new path by extending the current path
                new_path = path + [next_city]
                # Add the new path to the priority queue
                heapq.heappush(queue, (new_cost, new_path))
    
    return None

print(a_star())
