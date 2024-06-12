
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1],
        [0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0]
    ]

    # Define the city names
    city_names = ['G', 'T', 'M', 'U', 'K', 'Y', 'D', 'A', 'P', 'R', 'E', 'S', 'I']

    # Define the initial state and goal state
    initial_state = (city_names.index('R'), False, False)
    goal_state = (city_names.index('R'), True, True)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, ['R'], initial_state)]

    while queue:
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the connected cities
        for i in range(len(city_names)):
            if adjacency_matrix[state[0]][i] == 1:
                # Check if the new state is valid, ie if the city has not been visited before, or if it is city A or Y
                if city_names[i] not in path or city_names[i] in ['A', 'Y']:
                    # Generate the new state
                    visited_A = state[1] or city_names[i] == 'A'
                    visited_Y = state[2] or city_names[i] == 'Y'
                    new_state = (i, visited_A, visited_Y)

                    # The cost so far is the number of actions taken, as the task is to minimize the number of actions required
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost, new_cost, path + [city_names[i]], new_state))

    return None

print(a_star())
