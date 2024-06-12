
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
        [1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0]
    ]

    # Define the city names
    city_names = ['X', 'T', 'R', 'O', 'M', 'U', 'I', 'P', 'Z', 'F', 'V', 'H', 'Q', 'J', 'B']

    # Define the initial state and goal state
    initial_state = (6, 0, 0, 0)  # (current city, visited H, visited R, visited cities)
    goal_state = (6, 2, 2, 0b111111111111111)  # (current city, visited H, visited R, visited cities)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element.
    queue = [(0, 0, [initial_state[0]], initial_state)]

    while queue:
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return [city_names[i] for i in path]

        # Generate all possible actions from the current state, which includes moving to any of the connected cities
        for i in range(15):
            if adjacency_matrix[state[0]][i] == 1 and ((state[3] & (1 << i)) == 0 or i == 11 or i == 2):
                # If the city is connected and (the city has not been visited or the city is H or R)
                new_state = list(state)
                new_state[0] = i
                new_state[3] |= (1 << i)
                if i == 11:  # If the city is H
                    new_state[1] += 1
                if i == 2:  # If the city is R
                    new_state[2] += 1
                new_state = tuple(new_state)

                new_cost = g + 1
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost, new_cost, path + [new_state[0]], new_state))

    return None

print(a_star())
