
import heapq

def initialize():
    # Define the adjacency matrix representing the connections between cities
    adjacency_matrix = [
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
        [0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0]
    ]
    
    # Define the cities and the start city
    cities = ['S', 'A', 'J', 'U', 'E', 'B', 'N', 'P', 'L', 'X', 'F']
    start_city = 'J'
    
    # Initialize the visited costs dictionary and the priority queue
    visited_costs = {}
    visited_costs[start_city] = 0
    queue = [(0, 0, [start_city], start_city)]
    
    return adjacency_matrix, cities, start_city, visited_costs, queue

def a_star():
    # Initialize the variables using the initialize function
    adjacency_matrix, cities, start_city, visited_costs, queue = initialize()
    
    while queue:
        _, g, path, current_city = heapq.heappop(queue)
        
        # Check if we have visited both destination cities twice
        if path.count('U') == 2 and path.count('E') == 2:
            return path
        
        # Find the index of the current city in the cities list
        current_city_index = cities.index(current_city)
        
        # Generate all possible actions from the current city
        for i in range(len(cities)):
            # Check if there is a road from the current city to the next city and if we have not visited the next city before
            if adjacency_matrix[current_city_index][i] == 1 and cities[i] not in path:
                new_path = path + [cities[i]]
                new_cost = g + 1
                
                # If the new city has not been visited before or we found a new path with a lower cost, add it to the queue
                if cities[i] not in visited_costs or new_cost < visited_costs[cities[i]]:
                    visited_costs[cities[i]] = new_cost
                    heapq.heappush(queue, (new_cost, new_cost, new_path, cities[i]))
    
    return None

print(a_star())
