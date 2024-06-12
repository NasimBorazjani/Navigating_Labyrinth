
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                        [1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                        [1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0],
                        [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                        [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                        [1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1],
                        [0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                        [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0]]

    # Define the city names
    city_names = ['N', 'Y', 'P', 'L', 'Q', 'H', 'C', 'G', 'U', 'K', 'J', 'B', 'R', 'T']

    # Define the initial state and goal state
    initial_state = (2, False, False, [False]*14)  # The third element of the tuple is a list of booleans indicating whether each city has been visited
    goal_state = (2, True, True, [False]*14)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, [city_names[2]], initial_state)]  # The third element of the tuple is a list of city names on the path

    while queue:
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the cities connected to the current city
        for i in range(14):
            if adjacency_matrix[state[0]][i] == 1 and not state[3][i]:  # Check if there is a road to the city and the city has not been visited
                # Generate the new state
                visited_N = state[1] or i == 0
                visited_R = state[2] or i == 12
                visited_cities = state[3][:]
                visited_cities[i] = True
                new_state = (i, visited_N, visited_R, visited_cities)

                # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited
                new_cost = g + 1

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [city_names[i]], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of destination cities not yet visited
    # The heuristic is admissible because it never overestimates the cost to reach the goal, as each unvisited destination city must be visited at least once
    # The heuristic is consistent because the cost of moving to a new city is always 1, which is exactly the decrease in the heuristic cost if the new city is a destination city
    return 2 - state[1] - state[2]


print(a_star())
