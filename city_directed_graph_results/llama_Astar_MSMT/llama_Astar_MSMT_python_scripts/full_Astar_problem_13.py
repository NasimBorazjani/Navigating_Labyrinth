
import heapq


def initialize():
    # Define the adjacency matrix of the directed graph
    adj_matrix = [
        [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
        [0, 0, 1, 0, 1, 1, 0, 0, 1, 1],
        [1, 1, 1, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 1, 0, 0, 0]
    ]
    # Define the start city and the destination cities
    start = 'H'
    destinations = ['E', 'X']
    num_cities = len(adj_matrix)

    # Initialize the visited_costs dictionary and the priority queue
    visited_costs = {}
    visited_costs[(start, 0, 0)] = 0
    queue = [(0, 0, [], (start, 0, 0))]

    return adj_matrix, start, destinations, num_cities, visited_costs, queue


def a_star():
    adj_matrix, start, destinations, num_cities, visited_costs, queue = initialize()

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        city, e_visits, x_visits = state

        # If we have visited both destination cities exactly twice, return the path
        if e_visits == 2 and x_visits == 2:
            return actions

        # Generate all possible actions from the current state, which includes moving to any directly connected city
        for i in range(num_cities):
            if adj_matrix[city][i] == 1:
                # If the city is a destination city, increment the number of visits
                if chr(i + 65) in destinations:
                    if chr(i + 65) == 'E':
                        e_visits_new = e_visits + 1
                    else:
                        x_visits_new = x_visits + 1
                else:
                    e_visits_new, x_visits_new = e_visits, x_visits

                # Generate the new state
                new_state = (i, e_visits_new, x_visits_new)
                # The cost of the new state is the travel time to get to the new city plus the cost of the current state
                new_cost = g + 1

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The city must be added to the path
                    heapq.heappush(queue, (new_cost + heuristic(new_state, destinations), new_cost, actions + [chr(i + 65)], new_state))

    return None


def heuristic(state, destinations):
    # The heuristic is the sum of the number of visits to the destination cities minus the number of visits to the current city
    city, e_visits, x_visits = state
    h = (2 - e_visits) + (2 - x_visits)
    return h


print(a_star())
