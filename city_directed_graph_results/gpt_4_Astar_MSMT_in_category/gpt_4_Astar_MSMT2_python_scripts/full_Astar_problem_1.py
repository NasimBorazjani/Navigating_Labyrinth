
import heapq

def initialize():
    # Define the adjacency matrix of the city graph
    city_graph = [['G', 'D', 'X', 'N', 'Y', 'W', 'A', 'P', 'V', 'H'],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                  [1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
                  [0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                  [1, 1, 1, 0, 0, 0, 0, 0, 1, 0],
                  [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                  [1, 1, 0, 1, 0, 0, 1, 1, 0, 0]]

    # Define the initial state of the problem
    # The initial state includes the current city, the cities that need to be visited twice, and the cities visited so far
    initial_state = ('W', ('A', 'A', 'H', 'H'), ('W',))

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, ['W'], initial_state)]

    return city_graph, visited_costs, queue

def a_star():
    city_graph, visited_costs, queue = initialize()

    while queue:
        _, g, path, state = heapq.heappop(queue)

        current_city, cities_to_visit, visited_cities = state

        # If there are no more cities to visit, return the path
        if not cities_to_visit:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the connected cities
        for i in range(1, len(city_graph)):
            if city_graph[0][i] not in visited_cities and city_graph[city_graph[0].index(current_city)][i] == 1:
                new_city = city_graph[0][i]
                new_visited_cities = visited_cities + (new_city,)
                if new_city in cities_to_visit:
                    new_cities_to_visit = list(cities_to_visit)
                    new_cities_to_visit.remove(new_city)
                    new_cities_to_visit = tuple(new_cities_to_visit)
                else:
                    new_cities_to_visit = cities_to_visit
                new_state = (new_city, new_cities_to_visit, new_visited_cities)
                new_cost = g + 1

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, path + [new_city], new_state))

    return None

def heuristic(state):
    # An admissible and consistent heuristic for this problem is the number of cities that still need to be visited
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as each city that needs to be visited requires at least one move
    # It's consistent because moving to a new city reduces the heuristic cost of the successor node by a max of 1, which is equal to the cost of reaching the successor node
    return len(state[1])

print(a_star())
