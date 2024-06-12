
import heapq


def a_star():
    # Define the adjacency matrix as a dictionary of dictionaries
    adjacency_matrix = {
        'D': {'D': 0, 'E': 1, 'Z': 1, 'R': 1, 'N': 0, 'I': 0, 'K': 0, 'G': 1, 'L': 1, 'B': 1},
        'E': {'D': 0, 'E': 0, 'Z': 1, 'R': 0, 'N': 0, 'I': 1, 'K': 0, 'G': 0, 'L': 0, 'B': 0},
        'Z': {'D': 0, 'E': 0, 'Z': 0, 'R': 0, 'N': 1, 'I': 0, 'K': 0, 'G': 0, 'L': 0, 'B': 0},
        'R': {'D': 1, 'E': 0, 'Z': 1, 'R': 0, 'N': 0, 'I': 0, 'K': 0, 'G': 0, 'L': 0, 'B': 1},
        'N': {'D': 0, 'E': 1, 'Z': 0, 'R': 0, 'N': 0, 'I': 1, 'K': 1, 'G': 1, 'L': 0, 'B': 0},
        'I': {'D': 1, 'E': 0, 'Z': 0, 'R': 0, 'N': 1, 'I': 0, 'K': 1, 'G': 0, 'L': 1, 'B': 0},
        'K': {'D': 0, 'E': 0, 'Z': 1, 'R': 0, 'N': 1, 'I': 0, 'K': 0, 'G': 0, 'L': 0, 'B': 0},
        'G': {'D': 0, 'E': 0, 'Z': 1, 'R': 1, 'N': 0, 'I': 1, 'K': 0, 'G': 0, 'L': 0, 'B': 0},
        'L': {'D': 0, 'E': 0, 'Z': 1, 'R': 0, 'N': 0, 'I': 0, 'K': 0, 'G': 1, 'L': 0, 'B': 0},
        'B': {'D': 0, 'E': 1, 'Z': 0, 'R': 0, 'N': 0, 'I': 1, 'K': 1, 'G': 0, 'L': 0, 'B': 0}
    }
    
    # Define the start city
    start_city = 'L'
    # Define the goal cities
    goal_cities = ['D', 'N']
    
    # Initialize a dictionary to store the cost of reaching each visited city
    visited_costs = {}
    visited_costs[start_city] = 0
    
    # Initialize a priority queue of cities not yet visited, with the start city as the first element
    queue = [(0, 0, [start_city], start_city)]
    
    # While there are un-visited cities
    while queue:
        _, g, path, current_city = heapq.heappop(queue)
        
        # If we have visited both goal cities twice, return the path
        if path.count('D') == 2 and path.count('N') == 2:
            return path
        
        # Generate all possible actions from the current city, which includes moving to any directly connected city
        for neighbor_city in adjacency_matrix[current_city]:
            # Check if the neighbor city has not been visited and there is a direct road to it
            if neighbor_city not in path and adjacency_matrix[current_city][neighbor_city] == 1:
                # Generate the new path
                new_path = path + [neighbor_city]
                # The cost so far is the number of cities visited
                new_cost = g + 1
                
                # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of un-visited cities
                if neighbor_city not in visited_costs or new_cost < visited_costs[neighbor_city]:
                    visited_costs[neighbor_city] = new_cost
                    heapq.heappush(queue, (new_cost, new_cost, new_path, neighbor_city))
    
    return None

print(a_star())
