
import heapq

def a_star():
    # Define the adjacency matrix representing the connections between cities
    adjacency_matrix = [[0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
                        [0, 0, 1, 0, 1, 1, 0, 0, 1, 1],
                        [1, 1, 1, 1, 0, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
                        [0, 0, 0, 0, 1, 0, 1, 0, 0, 0]]
    
    # Define the cities and their indices
    cities = ['G', 'X', 'R', 'L', 'Y', 'E', 'V', 'T', 'B', 'H']
    start_city = 'H'
    end_cities = ['E', 'X']
    
    # Initialize a dictionary to store the cost of reaching each visited city
    visited_costs = {}
    visited_costs[start_city] = 0
    
    # Initialize a priority queue of cities not yet visited, with the start city as the first element
    queue = [(0, [start_city], start_city)]
    
    # While there are unvisited cities
    while queue:
        _, path, current_city = heapq.heappop(queue)
        
        # If we have visited both destination cities twice, return the path
        if path.count('E') == 2 and path.count('X') == 2:
            return path
        
        # Find the index of the current city in the cities list
        current_city_index = cities.index(current_city)
        
        # Iterate through all cities to find the next possible city to visit
        for i in range(len(cities)):
            # Check if there is a road from the current city to the next city and the next city has not been visited yet
            if adjacency_matrix[current_city_index][i] == 1 and cities[i] not in path:
                new_path = path + [cities[i]]
                new_cost = len(new_path) - 1
                
                # If the new city has not been visited or we found a new path with a lower cost to reach this city, add it to the queue
                if cities[i] not in visited_costs or new_cost < visited_costs[cities[i]]:
                    visited_costs[cities[i]] = new_cost
                    heapq.heappush(queue, (new_cost, new_path, cities[i]))
    
    return None

print(a_star())
