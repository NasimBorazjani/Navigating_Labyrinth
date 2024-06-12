
import heapq


def a_star():
    # Define the adjacency matrix as a dictionary of dictionaries, where the keys are the city names and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'N': {'W': 0, 'X': 1, 'P': 0, 'J': 0, 'E': 1, 'L': 0, 'M': 1, 'I': 0, 'K': 0, 'Q': 1},
        'W': {'N': 1, 'X': 0, 'P': 1, 'J': 1, 'E': 0, 'L': 0, 'M': 0, 'I': 0, 'K': 0, 'Q': 0},
        'X': {'N': 0, 'W': 1, 'P': 1, 'J': 0, 'E': 1, 'L': 0, 'M': 0, 'I': 0, 'K': 1, 'Q': 1},
        'P': {'N': 1, 'W': 1, 'X': 0, 'J': 1, 'E': 0, 'L': 0, 'M': 0, 'I': 0, 'K': 0, 'Q': 1},
        'J': {'N': 0, 'W': 0, 'X': 1, 'P': 0, 'E': 1, 'L': 0, 'M': 0, 'I': 0, 'K': 0, 'Q': 0},
        'E': {'N': 1, 'W': 1, 'X': 0, 'P': 0, 'J': 0, 'L': 0, 'M': 0, 'I': 0, 'K': 0, 'Q': 0},
        'L': {'N': 1, 'W': 0, 'X': 0, 'P': 0, 'J': 0, 'E': 0, 'M': 0, 'I': 0, 'K': 0, 'Q': 1},
        'M': {'N': 1, 'W': 1, 'X': 0, 'P': 0, 'J': 0, 'E': 1, 'L': 0, 'I': 0, 'K': 0, 'Q': 0},
        'I': {'N': 0, 'W': 0, 'X': 1, 'P': 0, 'J': 1, 'E': 0, 'L': 1, 'M': 1, 'K': 0, 'Q': 0},
        'K': {'N': 0, 'W': 0, 'X': 1, 'P': 0, 'J': 0, 'E': 1, 'L': 0, 'M': 0, 'I': 1, 'Q': 0},
        'Q': {'N': 1, 'W': 1, 'X': 0, 'P': 0, 'J': 0, 'E': 0, 'L': 1, 'M': 0, 'I': 1, 'K': 0}
    }

    # Define the initial state, goal state, and other variables
    initial_state = 'K'
    goal_state = ['N', 'P']
    num_visits = 2

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, current_city = heapq.heappop(queue)

        # Check if we have visited the goal cities the required number of times
        if actions.count(goal_state[0]) == num_visits and actions.count(goal_state[1]) == num_visits:
            return actions

        # Generate all possible actions from the current city
        for next_city in adjacency_matrix[current_city]:
            # Check if the next city has not been visited before
            if actions.count(next_city) < 1:
                new_cost = g + 1
                if next_city not in visited_costs or new_cost < visited_costs[next_city]:
                    visited_costs[next_city] = new_cost
                    heapq.heappush(queue, (new_cost, new_cost, actions + [next_city], next_city))

    return None


print(a_star())
