
import heapq

def initialize():
    # Define the adjacency matrix of the city graph
    city_graph = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                  [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
                  [0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                  [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                  [0, 1, 0, 1, 1, 1, 0, 0, 1, 0]]
    # Define the city names
    city_names = ['S', 'U', 'X', 'D', 'I', 'Z', 'R', 'M', 'K', 'Q']
    # Define the initial state, which includes the current city, the cities to visit, and the cities visited so far
    initial_state = ('D', ('K', 'K', 'Q', 'Q'), ('D',))
    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0
    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, ['D'], initial_state)]
    return city_graph, city_names, initial_state, visited_costs, queue

def a_star():
    city_graph, city_names, initial_state, visited_costs, queue = initialize()
    while queue:
        _, g, path, state = heapq.heappop(queue)
        current_city, cities_to_visit, cities_visited = state
        # If there are no more cities to visit, return the path
        if not cities_to_visit:
            return path
        # Generate all possible actions from the current state, which includes moving to any of the cities connected to the current city
        for i in range(len(city_graph)):
            if city_graph[city_names.index(current_city)][i] == 1:
                next_city = city_names[i]
                # Check if the next city is one of the cities to visit or has not been visited yet
                if next_city in cities_to_visit or next_city not in cities_visited:
                    # Generate the new state
                    new_cities_to_visit = list(cities_to_visit)
                    if next_city in new_cities_to_visit:
                        new_cities_to_visit.remove(next_city)
                    new_cities_visited = list(cities_visited) + [next_city]
                    new_state = (next_city, tuple(new_cities_to_visit), tuple(new_cities_visited))
                    # The cost so far is the number of cities visited, as the travel time between any two directly connected cities is the same
                    new_cost = g + 1
                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost, new_cost, path + [next_city], new_state))
    return None

print(a_star())
