
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (7, 0)
    goal_state = (2, 9)
    # Define the map of the city
    city_map = np.array([[12, 11, 14, 10, 2, 11, 13, 16, 3, 'x', 12],
                         [10, 9, 'x', 8, 'x', 'x', 1, 16, 11, 'x', 15],
                         [1, 18, 1, 'x', 'x', 'x', 'x', 'x', 12, 9, 'x'],
                         [1, 14, 15, 10, 7, 15, 17, 10, 15, 15, 6],
                         [18, 11, 'x', 'x', 'x', 15, 'x', 'x', 1, 1, 'x'],
                         [14, 'x', 'x', 'x', 18, 14, 16, 7, 'x', 1, 'x'],
                         [11, 15, 'x', 'x', 15, 3, 11, 13, 'x', 'x', 'x'],
                         [5, 'x', 'x', 'x', 'x', 'x', 15, 'x', 6, 'x', 'x'],
                         [12, 11, 7, 2, 11, 'x', 10, 2, 17, 'x', 'x'],
                         [7, 'x', 'x', 'x', 4, 'x', 4, 'x', 'x', 5, 'x'],
                         ['x', 19, 10, 7, 'x', 2, 3, 9, 2, 6, 'x']])
    num_rows, num_cols = city_map.shape
    # Define the districts of the city
    districts = [range(0, 3), range(3, 7), range(7, 11)]
    # Define the visited costs dictionary
    visited_costs = {}
    visited_costs[(initial_state, frozenset())] = 0
    # Define the priority queue
    queue = [(0, 0, [], initial_state, frozenset())]

    while queue:
        _, g, actions, state, visited_districts = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state and len(visited_districts) == len(districts):
            return actions

        # Generate all possible actions from the current state
        for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_state = (state[0] + d_row, state[1] + d_col)
            # Check if the new state is valid
            if (0 <= new_state[0] < num_rows and 0 <= new_state[1] < num_cols and
                city_map[new_state] != 'x'):
                # Calculate the cost of the new state
                new_cost = g + int(city_map[new_state])
                # Update the visited districts
                new_visited_districts = visited_districts.copy()
                for i, district in enumerate(districts):
                    if new_state[0] in district:
                        new_visited_districts.add(i)
                # Check if the new state has been visited or if the new cost is lower
                if (new_state, new_visited_districts) not in visited_costs or new_cost < visited_costs[(new_state, new_visited_districts)]:
                    visited_costs[(new_state, new_visited_districts)] = new_cost
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, new_visited_districts))

    return None


def heuristic(state, goal):
    # Use the Manhattan distance as the heuristic function
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
