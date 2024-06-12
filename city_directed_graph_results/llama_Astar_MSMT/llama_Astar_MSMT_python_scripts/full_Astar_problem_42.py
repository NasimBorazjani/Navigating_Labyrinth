
import heapq


def initialize():
    # Define the adjacency matrix of the cities and the graph
    adj_matrix = [[0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                  [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1],
                  [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                  [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                  [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                  [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                  [1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                  [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
                  [0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0]]
    start_city = 'F'
    goal_cities = ['H', 'N']
    num_cities = len(adj_matrix)

    # Encoding other variables of the problem
    visited_costs = {}
    visited_costs[start_city] = 0

    queue = [(0, 0, [start_city], start_city)]

    return adj_matrix, num_cities, goal_cities, visited_costs, queue


def a_star():
    adj_matrix, num_cities, goal_cities, visited_costs, queue = initialize()

    while queue:
        _, g, path, state = heapq.heappop(queue)

        # If we have visited both goal cities exactly twice, return the path
        if path.count(goal_cities[0]) == 2 and path.count(goal_cities[1]) == 2:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
        for i in range(num_cities):
            if adj_matrix[state][i] == 1:
                # Check if the new city is not the start city and has not been visited twice
                if i != ord(start_city) - ord('A') and path.count(chr(i + ord('A'))) < 2:
                    # Generate the new state
                    new_state = chr(i + ord('A'))
                    # Cost of the new state is the travel time to get to the new city
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        # The city must be added to the path
                        heapq.heappush(queue, (new_cost + heuristic(state, new_state, goal_cities), new_cost, path + [new_state], new_state))

    return None


def heuristic(state, new_state, goal_cities):
    # The heuristic function can be a simulation of visiting the goal cities in the order they appear in the path
    # This heuristic is admissible because it is greedy, always opting for the city that leads to the goal city in the path, ensuring it never overestimates the cost to reach the goal
    # The heuristic is consistent as the estimated cost of the next node is higher if the current city is not in the goal cities, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of actions that can be added to the path is by visiting the current city in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
    h = 0
    for city in goal_cities:
        if city not in path:
            h += 1
    return h


print(a_star())
