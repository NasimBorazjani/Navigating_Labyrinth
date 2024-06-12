
import heapq

def initialize():
    # Define the adjacency matrix representing the connections between cities
    adjacency_matrix = [[0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
                        [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1],
                        [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                        [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                        [1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0]]
    
    # Define the cities and the starting city
    cities = ['N', 'W', 'X', 'P', 'J', 'E', 'L', 'M', 'I', 'K', 'Q']
    start_city = 'K'
    
    # Initialize the visited_costs dictionary and the priority queue
    visited_costs = {}
    visited_costs[start_city] = 0
    queue = [(0, 0, [], start_city)]
    
    return adjacency_matrix, cities, start_city, visited_costs, queue

def a_star():
    adjacency_matrix, cities, start_city, visited_costs, queue = initialize()
    
    while queue:
        _, g, actions, current_city = heapq.heappop(queue)
        
        # Check if we have visited both destination cities twice
        if actions.count('N') == 2 and actions.count('P') == 2:
            return actions
        
        # Generate all possible actions from the current city
        for i, connected in enumerate(adjacency_matrix[cities.index(current_city)]):
            if connected == 1 and cities[i] not in actions:
                new_city = cities[i]
                new_cost = g + 1
                
                if new_city not in visited_costs or new_cost < visited_costs[new_city]:
                    visited_costs[new_city] = new_cost
                    heapq.heappush(queue, (new_cost, new_cost, actions + [new_city], new_city))
    
    return None

print(a_star())
