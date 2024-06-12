
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'J': {'N': 1},
        'U': {'D': 1, 'E': 1, 'M': 1},
        'X': {'A': 1, 'B': 1, 'K': 1, 'L': 1, 'M': 1},
        'R': {'I': 1, 'J': 1, 'H': 1},
        'L': {'D': 1, 'F': 1, 'G': 1},
        'Z': {'G': 1, 'H': 1, 'M': 1},
        'O': {'C': 1, 'F': 1},
        'F': {'B': 1, 'I': 1, 'K': 1, 'M': 1},
        'Q': {'B': 1, 'E': 1, 'H': 1, 'K': 1},
        'C': {'G': 1, 'I': 1, 'L': 1},
        'N': {'D': 1, 'E': 1, 'F': 1, 'K': 1},
        'V': {'A': 1, 'B': 1, 'G': 1, 'L': 1, 'M': 1},
        'M': {'H': 1, 'O': 1}
    }
    
    # Define the start city, the two destination cities, and the number of times we need to visit each destination
    start_city = 'J'
    destination_cities = ['Z', 'M']
    num_visits = {city: 2 for city in destination_cities}
    
    # Initialize a dictionary to store the cost of reaching each visited city
    visited_costs = {}
    visited_costs[start_city] = 0
    
    # Initialize a priority queue of cities not yet visited, with the start city as the first element
    queue = [(0, 0, [start_city], start_city, num_visits.copy())]
    
    # While there are unvisited cities
    while queue:
        _, g, path, current_city, remaining_visits = heapq.heappop(queue)
        
        # If we have visited both destination cities twice, return the path
        if all(remaining_visits[city] == 0 for city in destination_cities):
            return path
        
        # Generate all possible actions from the current city, which includes moving to any connected city
        for neighbor in adjacency_matrix[current_city]:
            # Check if we can visit the neighbor city
            if remaining_visits[current_city] > 0:
                new_path = path + [neighbor]
                new_remaining_visits = remaining_visits.copy()
                new_remaining_visits[current_city] -= 1
                
                # Calculate the cost of reaching the neighbor city
                new_cost = g + 1
                
                # If the neighbor city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of unvisited cities
                if neighbor not in visited_costs or new_cost < visited_costs[neighbor]:
                    visited_costs[neighbor] = new_cost
                    heapq.heappush(queue, (new_cost, new_cost, new_path, neighbor, new_remaining_visits))
    
    return None

print(a_star())
