
import heapq

def initialize():
    # Define the adjacency matrix representing the connections between cities
    adjacency_matrix = [[0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0]]
    
    # Encode the cities and the start city
    cities = ['S', 'V', 'U', 'W', 'G', 'E', 'H', 'P', 'T', 'Q', 'Z']
    start_city = 'G'
    # Encode the goal cities and the number of times they need to be visited
    goal_cities = ['H', 'P']
    num_visits = 2

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[start_city] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the path taken to get to each state in a list; no path taken to reach the initial state
    queue = [(0, 0, [start_city], start_city)]

    return adjacency_matrix, cities, start_city, goal_cities, num_visits, visited_costs, queue

def a_star():
    # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the adjacency matrix, cities, start city, goal cities, and number of visits)
    adjacency_matrix, cities, start_city, goal_cities, num_visits, visited_costs, queue = initialize()

    while queue:
        _, g, path, current_city = heapq.heappop(queue)

        # Check if the current city is one of the goal cities and has been visited the required number of times
        if current_city in goal_cities and path.count(current_city) == num_visits:
            return path

        # Find the index of the current city in the cities list to access the corresponding row in the adjacency matrix
        current_city_index = cities.index(current_city)

        # Generate all possible actions from the current city, which includes moving to any city connected by a one-way road
        for i, connected in enumerate(adjacency_matrix[current_city_index]):
            if connected == 1:
                next_city = cities[i]
                new_cost = g + 1

                # If the new city has not been visited or we found a new path with a lower cost to reach this city, add it to the queue of unvisited cities
                if next_city not in visited_costs or new_cost < visited_costs[next_city]:
                    visited_costs[next_city] = new_cost
                    h = heuristic(next_city, goal_cities, num_visits)
                    heapq.heappush(queue, (new_cost + h, new_cost, path + [next_city], next_city))

    return None

def heuristic(city, goal_cities, num_visits):
    # An admissible and consistent heuristic is the number of visits remaining to the goal cities
    # This heuristic is admissible because it underestimates the cost to reach the goal, as it does not consider the actual distances between cities
    # The heuristic is consistent because the cost of reaching a city is always 1, which is exactly the decrease in the heuristic estimate for the successor node
    # The heuristic estimate for the goal state is 0, as the number of visits remaining to the goal cities is 0
    h = num_visits - goal_cities.count(city)
    return h

print(a_star())
