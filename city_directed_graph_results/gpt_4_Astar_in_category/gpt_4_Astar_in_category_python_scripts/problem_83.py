
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [
        [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        [1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0],
        [0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0]
    ]

    # Define the city names
    city_names = ['J', 'H', 'X', 'L', 'F', 'A', 'P', 'M', 'D', 'R', 'T', 'Z', 'N', 'K']

    # Define the initial state and goal state
    initial_state = (city_names.index('X'), 0, 0)
    goal_state = (city_names.index('X'), 2, 2)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, ['X'], initial_state)]

    while queue:
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state
        for i in range(len(city_names)):
            if adjacency_matrix[state[0]][i] == 1:
                # If the city is 'N' or 'K', we can visit it twice
                if city_names[i] in ['N', 'K']:
                    if path.count(city_names[i]) < 2:
                        new_state = (i, state[1] + (city_names[i] == 'N'), state[2] + (city_names[i] == 'K'))
                        new_cost = g + 1
                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (new_cost, new_cost, path + [city_names[i]], new_state))
                # For other cities, we can only visit them once
                elif city_names[i] not in path:
                    new_state = (i, state[1], state[2])
                    new_cost = g + 1
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost, new_cost, path + [city_names[i]], new_state))

    return None

print(a_star())
