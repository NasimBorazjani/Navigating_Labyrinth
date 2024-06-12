
import heapq

def a_star():
    # Define the adjacency matrix of the graph, with the cities represented as indices of the rows and columns
    adjacency_matrix = [[0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
                        [1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                        [0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1],
                        [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]
    num_cities = 12
    # Define the initial state and the goal state of the problem
    initial_state = (11, [0]*num_cities, 0, 0)
    goal_state = (11, [0]*num_cities, 2, 2)
    # Define the indices of the destination cities
    M = 6
    Q = 1
    # Define the mapping of city indices to their names
    city_names = ['R', 'Q', 'Y', 'U', 'F', 'K', 'M', 'T', 'X', 'W', 'H', 'L']

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [city_names[initial_state[0]]], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the cities directly connected to the current city
        for next_city in range(num_cities):
            if adjacency_matrix[state[0]][next_city] == 1:
                # Check if the new state would be valid, ie the city must not have been visited before, unless it's one of the destination cities
                if (state[1][next_city] == 0 or (next_city == M and state[2] < 2) or (next_city == Q and state[3] < 2)):
                    # Generate the new state
                    new_state = list(state)
                    new_state[0] = next_city
                    new_state[1] = list(state[1])
                    new_state[1][next_city] += 1
                    if next_city == M:
                        new_state[2] += 1
                    if next_city == Q:
                        new_state[3] += 1
                    new_state = tuple(new_state)
                    # The cost so far is the number of moves made, as the task is to minimize the number of moves required to visit the destination cities twice
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [city_names[next_city]], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of remaining visits to the destination cities
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as each remaining visit to a destination city must be made at least once
    # It's consistent because moving to a city reduces the heuristic cost of the successor node by a max of 1 (if the moved city is a destination city), which is equal to the cost of reaching the successor node
    return goal[2] - state[2] + goal[3] - state[3]

print(a_star())
