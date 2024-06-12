
import heapq

def initialize():
    # Define the adjacency matrix representing the connections between cities
    adjacency_matrix = [[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                        [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
                        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                        [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                        [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
                        [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0]]

    # Define the cities and the start city
    cities = ['J', 'U', 'T', 'S', 'N', 'F', 'Y', 'C', 'H', 'A', 'M', 'P']
    start_city = 'F'

    # Define the goal cities that need to be visited exactly twice
    goal_cities = ['N', 'H']

    # Initialize the dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[start_city] = 0

    # Initialize a priority queue of states not yet visited, with the start city as the first element
    queue = [(0, 0, [], start_city)]

    return adjacency_matrix, cities, start_city, goal_cities, visited_costs, queue

def a_star():
    # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem
    adjacency_matrix, cities, start_city, goal_cities, visited_costs, queue = initialize()

    while queue:
        _, g, actions, current_city = heapq.heappop(queue)

        # If the current city is one of the goal cities that need to be visited twice, update the count for that city
        if current_city in goal_cities:
            goal_cities.remove(current_city)
            if not goal_cities:
                return actions

        # Generate all possible actions from the current city, which includes moving to a connected city
        for i, connected in enumerate(adjacency_matrix[cities.index(current_city)]):
            if connected == 1:
                new_city = cities[i]
                # Calculate the cost to reach the new city
                new_cost = g + 1

                # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of unvisited cities
                if new_city not in visited_costs or new_cost < visited_costs[new_city]:
                    visited_costs[new_city] = new_cost
                    heapq.heappush(queue, (new_cost, new_cost, actions + [new_city], new_city))

    return None

print(a_star())
