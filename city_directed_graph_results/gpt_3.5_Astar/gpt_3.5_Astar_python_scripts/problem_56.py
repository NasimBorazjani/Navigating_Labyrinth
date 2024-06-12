
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are lists of connected cities
    adjacency_matrix = {
        'K': ['M', 'X'],
        'M': ['V', 'I', 'L'],
        'B': ['K', 'I'],
        'X': ['K', 'M', 'R'],
        'N': ['F'],
        'D': ['F', 'I', 'R'],
        'V': ['I'],
        'C': ['B'],
        'I': ['N', 'D', 'W'],
        'R': ['M'],
        'F': ['N', 'W', 'L'],
        'W': ['B', 'M', 'L'],
        'L': ['C', 'F', 'W']
    }
    
    # Define the start city, destination cities, and the number of times each destination city should be visited
    start_city = 'C'
    destination_cities = ['B', 'L']
    visit_count = {city: 2 for city in destination_cities}
    
    # Initialize a priority queue to store the paths to be explored, starting with the start city
    queue = [(0, [start_city])]
    
    # While there are paths to explore
    while queue:
        # Pop the path with the lowest cost from the priority queue
        cost, path = heapq.heappop(queue)
        
        # Get the current city from the end of the path
        current_city = path[-1]
        
        # Check if the current city is one of the destination cities and if we still need to visit it
        if current_city in destination_cities and visit_count[current_city] > 0:
            visit_count[current_city] -= 1
            
            # If we have visited both destination cities twice, return the path
            if all(count == 0 for count in visit_count.values()):
                return path
        
        # Explore all possible next cities from the current city
        for next_city in adjacency_matrix[current_city]:
            # Ensure we do not revisit a city already visited in the path
            if next_city not in path:
                # Calculate the cost of the path by incrementing the cost for each step
                new_cost = cost + 1
                # Add the new path to the priority queue
                heapq.heappush(queue, (new_cost, path + [next_city]))
    
    return None

print(a_star())
