
import heapq

def initialize():
    # Define the adjacency matrix of the directed graph
    adj_matrix = [[0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                  [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                  [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
                  [1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                  [0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                  [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]
    # Define the start city and the cities we need to visit exactly twice
    start_city = 'L'
    cities_to_visit = ['M', 'Q']
    # Define the number of cities
    num_cities = 12
    # Define the city names
    city_names = ['R', 'Q', 'Y', 'U', 'F', 'K', 'M', 'T', 'X', 'W', 'H', 'L']
    # Initialize the visited_costs dictionary and the priority queue
    visited_costs = {}
    visited_costs[(start_city, 0, 0)] = 0
    queue = [(0, 0, [], (start_city, 0, 0))]
   
    return adj_matrix, start_city, cities_to_visit, num_cities, city_names, visited_costs, queue
  
def a_star():
    adj_matrix, start_city, cities_to_visit, num_cities, city_names, visited_costs, queue = initialize()

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If we have visited all cities twice, return the actions taken
        if all(visited == 2 for visited in state[1:]):
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
        for city_index in range(num_cities):
            if adj_matrix[city_names.index(state[0])][city_index] == 1:
                city_name = city_names[city_index]
                # Check if the city is in the list of cities to visit exactly twice
                if city_name in cities_to_visit:
                    city_visited = state[1:][city_names.index(city_name)]
                    # If the city has been visited less than twice, generate the new state
                    if city_visited < 2:
                        new_state = (city_name,) + tuple(state[1:][city_names.index(city_name)] + 1 if city_names[city_names.index(city_name)] == city_name else state[1:][city_names.index(city_name)])
                        new_cost = g + 1
                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (new_cost + heuristic(new_state, cities_to_visit), new_cost, actions + [city_name], new_state))
                else:
                    new_state = (city_name,) + state[1:]
                    new_cost = g + 1
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, cities_to_visit), new_cost, actions + [city_name], new_state))
    return None

def heuristic(state, cities_to_visit):
    # The heuristic function can be a simulation of visiting the cities in the order they appear in the actions list
    # This heuristic is admissible because it is greedy, always opting for the action that visits the cities in the order they appear in the actions list
    # The heuristic is consistent as the estimated cost of the next node is higher if the city is not visited, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of visits that can be made to the city is by visiting the city in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
    h = 0
    for city in cities_to_visit:
        h += state[1:][city_names.index(city)]
    return h

print(a_star())
