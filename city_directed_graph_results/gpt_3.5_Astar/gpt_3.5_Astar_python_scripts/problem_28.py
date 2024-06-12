
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries of connected cities
    adjacency_matrix = {
        'A': {'M': 1, 'O': 1, 'E': 1},
        'N': {'Q': 1, 'P': 1},
        'B': {'Z': 1, 'O': 1, 'G': 1},
        'M': {'N': 1, 'O': 1},
        'Z': {'E': 1},
        'O': {'M': 1, 'Q': 1, 'G': 1, 'L': 1},
        'E': {'A': 1, 'B': 1, 'O': 1, 'P': 1},
        'Q': {'M': 1},
        'G': {'N': 1, 'Q': 1},
        'L': {'N': 1, 'P': 1},
        'P': {'O': 1}
    }
    
    # Define the start city, destination cities, and the number of times to visit each destination
    start_city = 'B'
    destination_cities = ['E', 'N']
    visit_count = {city: 2 for city in destination_cities}
    
    # Initialize the priority queue with the start city and the number of visits left for each destination city
    queue = [(0, start_city, visit_count.copy(), [start_city])]
    
    while queue:
        _, current_city, visit_count, path = heapq.heappop(queue)
        
        # Check if all destination cities have been visited twice
        if all(count == 0 for count in visit_count.values()):
            return path
        
        # Explore all possible next cities to visit
        for next_city, connected in adjacency_matrix[current_city].items():
            if visit_count[next_city] > 0:
                new_visit_count = visit_count.copy()
                new_visit_count[next_city] -= 1
                new_path = path + [next_city]
                # Calculate the cost of the path based on the number of visits left to the destination cities
                cost = sum(new_visit_count.values())
                heapq.heappush(queue, (cost, next_city, new_visit_count, new_path))
    
    return None

print(a_star())
