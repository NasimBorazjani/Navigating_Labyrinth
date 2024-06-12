
import heapq

def initialize():
    # Define the adjacency matrix representing the connections between cities
    adjacency_matrix = [[0, 0, 0, 1, 0, 1, 1, 1, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
                        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                        [0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
                        [0, 0, 0, 0, 1, 1, 0, 1, 1, 0],
                        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                        [1, 0, 0, 0, 1, 1, 1, 0, 0, 0]]
    
    # Define the cities and the start city
    cities = ['C', 'V', 'A', 'G', 'Y', 'P', 'Z', 'S', 'J', 'I']
    start_city = 'S'
    
    # Initialize a dictionary to store the cost of reaching each visited city
    visited_costs = {}
    visited_costs[start_city] = 0
    
    # Initialize a priority queue of cities not yet visited, with the start city as the first element
    queue = [(0, 0, [start_city], start_city)]
    
    return adjacency_matrix, cities, start_city, visited_costs, queue

def a_star():
    adjacency_matrix, cities, start_city, visited_costs, queue = initialize()
    
    while queue:
        _, g, path, current_city = heapq.heappop(queue)
        
        # Check if we have visited both destination cities twice
        if path.count('P') == 2 and path.count('G') == 2:
            return path
        
        # Generate all possible actions from the current city, which includes moving to any directly connected city that has not been visited yet
        for i, connected in enumerate(adjacency_matrix[cities.index(current_city)]):
            if connected == 1 and cities[i] not in path:
                new_path = path + [cities[i]]
                new_cost = g + 1
                
                # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of unvisited cities
                if cities[i] not in visited_costs or new_cost < visited_costs[cities[i]]:
                    visited_costs[cities[i]] = new_cost
                    heapq.heappush(queue, (new_cost, new_cost, new_path, cities[i]))
    
    return None

print(a_star())
