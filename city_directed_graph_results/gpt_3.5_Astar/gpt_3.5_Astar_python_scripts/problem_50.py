
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are lists of connected cities
    adjacency_matrix = {
        'I': ['A'],
        'E': ['I', 'V'],
        'A': ['I', 'E', 'G', 'K', 'B', 'O'],
        'G': ['V'],
        'V': ['E', 'A', 'K'],
        'K': ['E', 'A', 'B'],
        'B': ['A', 'N'],
        'N': ['A', 'O'],
        'F': ['G', 'V', 'J'],
        'W': ['E', 'A', 'F', 'O'],
        'J': ['G', 'V', 'O'],
        'O': ['A', 'N', 'F', 'J']
    }
    
    # Define the start city, the two destination cities, and the number of times we need to visit each destination
    start_city = 'E'
    destination_cities = ['N', 'O']
    visit_count = {city: 2 for city in destination_cities}
    
    # Initialize a priority queue to store the paths to be explored, starting with the start city
    queue = [(0, [start_city])]
    
    # While there are paths to explore
    while queue:
        # Pop the path with the lowest cost from the priority queue
        cost, path = heapq.heappop(queue)
        
        # Get the current city from the end of the path
        current_city = path[-1]
        
        # Check if we have visited both destination cities twice
        if all(visit_count[city] == 0 for city in destination_cities):
            return path
        
        # Explore all possible next cities from the current city
        for next_city in adjacency_matrix[current_city]:
            # Check if we can visit the next city
            if next_city not in path:
                # Update the visit count for the destination cities
                if next_city in destination_cities:
                    visit_count[next_city] -= 1
                
                # Calculate the new cost of the path
                new_cost = cost + 1
                
                # Add the new path to the priority queue
                heapq.heappush(queue, (new_cost, path + [next_city]))
    
    return None

print(a_star())
