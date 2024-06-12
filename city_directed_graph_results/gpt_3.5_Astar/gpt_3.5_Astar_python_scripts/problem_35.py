
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary
    adjacency_matrix = {
        'A': {'V': 1, 'S': 1, 'M': 1, 'G': 1},
        'V': {'N': 1, 'H': 1},
        'N': {'P': 1, 'E': 1},
        'Q': {'A': 1, 'V': 1, 'P': 1},
        'P': {'V': 1, 'E': 1, 'L': 1},
        'S': {'N': 1},
        'M': {'V': 1, 'S': 1, 'E': 1, 'W': 1, 'G': 1},
        'E': {'N': 1, 'P': 1, 'L': 1},
        'L': {'E': 1, 'H': 1, 'W': 1, 'G': 1},
        'H': {'M': 1},
        'W': {'A': 1, 'V': 1, 'N': 1, 'E': 1, 'G': 1},
        'G': {'A': 1, 'V': 1}
    }
    
    # Define the start city
    start_city = 'G'
    # Define the goal cities
    goal_cities = ['L', 'P']
    
    # Initialize a priority queue to store the states to be visited
    queue = []
    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    
    # Add the start city to the queue with cost 0 and empty path
    heapq.heappush(queue, (0, start_city, []))
    
    while queue:
        # Pop the state with the lowest cost from the queue
        cost, current_city, path = heapq.heappop(queue)
        
        # Check if we have reached one of the goal cities twice
        if path.count('L') == 2 and path.count('P') == 2:
            return path + [current_city]
        
        # Check if the current city has been visited before
        if current_city in visited_costs:
            # If the cost to reach the current city is lower than the previous cost, update the cost
            if cost < visited_costs[current_city]:
                visited_costs[current_city] = cost
            else:
                continue
        else:
            visited_costs[current_city] = cost
        
        # Add the neighbors of the current city to the queue
        for neighbor, road_time in adjacency_matrix[current_city].items():
            new_cost = cost + road_time
            heapq.heappush(queue, (new_cost, neighbor, path + [current_city]))
    
    return None

print(a_star())
