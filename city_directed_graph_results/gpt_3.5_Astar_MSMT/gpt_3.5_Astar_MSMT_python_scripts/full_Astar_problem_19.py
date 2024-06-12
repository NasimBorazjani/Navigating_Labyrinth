
import heapq

def initialize():
    # Define the adjacency matrix representing the connections between cities
    adjacency_matrix = [[0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
                        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                        [1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
                        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
                        [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                        [1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0]]
    
    # Encoding other variables given in the problem statement
    start_city = 'E'
    target_cities = ['T', 'Y']
    num_visits = 2

    # Initialize a dictionary to store the cost of reaching each visited city
    visited_costs = {}
    visited_costs[start_city] = 0

    # Initialize a priority queue of cities not yet visited, with the start city as the first element
    queue = [(0, 0, [start_city], start_city)]

    return adjacency_matrix, start_city, target_cities, num_visits, visited_costs, queue

def a_star():
    adjacency_matrix, start_city, target_cities, num_visits, visited_costs, queue = initialize()

    while queue:
        _, g, path, current_city = heapq.heappop(queue)

        # If we have visited each target city the required number of times, return the path
        if all(path.count(city) == num_visits for city in target_cities):
            return path

        # Find the index of the current city in the adjacency matrix
        current_city_index = ord(current_city) - ord('A')

        # Generate all possible actions from the current city, which includes moving to any city connected by a one-way road
        for i, connected in enumerate(adjacency_matrix[current_city_index]):
            if connected == 1:
                new_city = chr(i + ord('A'))
                new_cost = g + 1

                # If the new city is not visited or we found a new path with a lower cost to reach this city, add it to the queue of un-visited cities
                if new_city not in visited_costs or new_cost < visited_costs[new_city]:
                    visited_costs[new_city] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_city, target_cities, num_visits), new_cost, path + [new_city], new_city))

    return None

def heuristic(city, target_cities, num_visits):
    # A heuristic to estimate the cost to reach the goal state by counting the number of target cities that still need to be visited the required number of times
    # This heuristic is admissible because it never overestimates the cost to reach the goal state
    # It is consistent because the estimated cost of the successor node is higher if the target city is not visited the required number of times, or equal if the target city is visited the required number of times
    remaining_visits = sum(1 for target_city in target_cities if city != target_city or path.count(target_city) < num_visits)
    return remaining_visits

print(a_star())
