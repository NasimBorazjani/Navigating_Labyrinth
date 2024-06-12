
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries of connected cities
    adjacency_matrix = {
        'R': {'B': 1, 'F': 1, 'N': 1},
        'B': {'F': 1, 'A': 1},
        'F': {'Z': 1, 'N': 1},
        'Z': {'A': 1, 'H': 1},
        'N': {'R': 1},
        'H': {'F': 1, 'J': 1},
        'A': {'P': 1, 'M': 1},
        'P': {'F': 1, 'M': 1, 'J': 1},
        'M': {'R': 1, 'J': 1},
        'J': {'Z': 1}
    }
    
    # Define the start city, destination cities, and the number of times each destination city should be visited
    start_city = 'Z'
    destination_cities = ['B', 'H']
    visit_count = {city: 2 for city in destination_cities}
    
    visited_costs = {}
    visited_costs[start_city] = 0
    
    queue = [(0, 0, [start_city], start_city, visit_count.copy())]
    
    while queue:
        _, g, path, current_city, visit_count = heapq.heappop(queue)
        
        # Check if we have visited both destination cities twice
        if all(count == 0 for count in visit_count.values()):
            return path
        
        # Generate all possible actions from the current city
        for neighbor in adjacency_matrix[current_city]:
            # Check if we can visit the neighbor city
            if visit_count.get(neighbor, 0) > 0:
                new_path = path + [neighbor]
                new_visit_count = visit_count.copy()
                new_visit_count[neighbor] -= 1
                new_cost = g + 1
                
                # If the new city has not been visited or we found a new path with a lower cost, add it to the queue
                if neighbor not in visited_costs or new_cost < visited_costs[neighbor]:
                    visited_costs[neighbor] = new_cost
                    heapq.heappush(queue, (new_cost, new_cost, new_path, neighbor, new_visit_count))
    
    return None

print(a_star())
