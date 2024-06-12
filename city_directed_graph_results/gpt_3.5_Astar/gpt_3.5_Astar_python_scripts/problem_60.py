
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'H': {'Q': 1, 'G': 1, 'N': 1, 'E': 1},
        'T': {'L': 1, 'N': 1},
        'R': {'H': 1, 'L': 1, 'G': 1, 'Y': 1},
        'F': {'T': 1, 'R': 1, 'Q': 1},
        'L': {'F': 1, 'Y': 1},
        'U': {'Q': 1, 'G': 1, 'E': 1},
        'Q': {'R': 1, 'G': 1, 'N': 1, 'Y': 1},
        'G': {'H': 1, 'T': 1, 'R': 1, 'N': 1},
        'N': {'T': 1, 'R': 1, 'G': 1, 'E': 1},
        'E': {'R': 1, 'L': 1, 'G': 1},
        'Y': {'R': 1, 'Q': 1, 'L': 1},
        'I': {'H': 1},
        'X': {'T': 1, 'L': 1, 'U': 1}
    }
    
    # Define the start city and the goal cities
    start_city = 'I'
    goal_cities = ['F', 'U']
    
    # Initialize a dictionary to store the cost of reaching each visited city
    visited_costs = {}
    visited_costs[start_city] = 0
    
    # Initialize a priority queue of cities not yet visited, with the start city as the first element
    queue = [(0, 0, [start_city], start_city)]
    
    # While there are unvisited cities
    while queue:
        _, g, path, current_city = heapq.heappop(queue)
        
        # Check if the current city is one of the goal cities
        if current_city in goal_cities:
            # If we have visited both goal cities twice, return the path
            if path.count('F') == 2 and path.count('U') == 2:
                return path
        
        # Generate all possible actions from the current city, which includes moving to any connected city
        for neighbor, cost in adjacency_matrix[current_city].items():
            # Check if the new city is unvisited or we found a new path with a lower cost to reach this city
            if neighbor not in visited_costs or g + cost < visited_costs[neighbor]:
                visited_costs[neighbor] = g + cost
                # Calculate the heuristic cost as the number of goal cities not visited twice
                h = 4 - path.count('F') - path.count('U')
                heapq.heappush(queue, (g + cost + h, g + cost, path + [neighbor], neighbor))
    
    return None

print(a_star())
