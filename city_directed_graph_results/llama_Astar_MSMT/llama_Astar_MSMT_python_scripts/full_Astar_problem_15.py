
import heapq


def initialize():
    # Define the adjacency matrix of the directed graph
    adj_matrix = [
        [0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    ]
    num_cities = len(adj_matrix)
    start_city = 'E'
    goal_cities = ['W', 'X']
    goal_count = 2

    # Initialize the visited_costs dictionary and the priority queue
    visited_costs = {}
    visited_costs[(start_city, goal_cities, goal_count)] = 0

    queue = [(0, 0, [], (start_city, goal_cities, goal_count))]

    return adj_matrix, num_cities, start_city, goal_cities, goal_count, visited_costs, queue


def a_star():
    adj_matrix, num_cities, start_city, goal_cities, goal_count, visited_costs, queue = initialize()

    while queue:
        _, g, path, state = heapq.heappop(queue)

        current_city, remaining_goals, goal_count = state

        # If we have visited all the goal cities the required number of times, return the path
        if not remaining_goals:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
        for city_index in range(num_cities):
            if adj_matrix[current_city][city_index] == 1:
                # If the city is a goal city and we have not visited it the required number of times, decrement the count
                if city_index in goal_cities:
                    remaining_goals_new = remaining_goals.copy()
                    remaining_goals_new[city_index] -= 1
                else:
                    remaining_goals_new = remaining_goals

                # Generate the new state
                new_state = (city_index, remaining_goals_new, goal_count)
                # Cost of the new state is the travel time to get to the new city
                new_cost = g + 1

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The city must be added to the path
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_cities), new_cost, path + [city_index], new_state))

    return None


def heuristic(state, goal_cities):
    # The heuristic function can be a simulation of visiting the goal cities in the order they appear in the goal_cities list
    # This heuristic is admissible because it is greedy, always opting for the city that leads to the goal city that is currently the furthest from being visited the required number of times
    # The heuristic is consistent as the estimated cost of the next node is higher if we visit a city that is further from being visited the required number of times, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of actions required to visit the goal city is by visiting the city that is currently the furthest from being visited the required number of times
    h = 0
    for city_index in range(len(state[0])):
        if city_index in goal_cities:
            h += abs(state[1][city_index])
    return h


print(a_star())
