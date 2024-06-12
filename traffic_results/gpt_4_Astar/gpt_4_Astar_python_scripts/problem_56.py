
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (6, 9)
    goal_state = (3, 0)
    # Define the map of the city
    city_map = np.array([[2, 'x', 'x', 14, 'x', 19, 6, 'x', 'x', 14, 18, 'x'],
                         ['x', 10, 1, 15, 'x', 'x', 'x', 'x', 17, 2, 9, 12],
                         [13, 14, 'x', 2, 'x', 'x', 10, 10, 'x', 'x', 'x', 'x'],
                         [9, 17, 3, 15, 4, 4, 'x', 9, 15, 16, 'x', 9],
                         [10, 7, 3, 8, 'x', 7, 'x', 16, 3, 7, 'x', 'x'],
                         [16, 20, 16, 19, 18, 3, 'x', 'x', 11, 14, 5, 'x'],
                         [14, 13, 8, 14, 12, 19, 6, 3, 19, 10, 11, 'x'],
                         ['x', 18, 'x', 'x', 4, 19, 6, 14, 15, 17, 7, 'x'],
                         ['x', 2, 'x', 'x', 'x', 'x', 'x', 7, 'x', 19, 'x', 'x'],
                         ['x', 3, 14, 1, 'x', 18, 4, 12, 'x', 3, 10, 'x'],
                         [2, 'x', 16, 13, 'x', 17, 'x', 'x', 17, 16, 4, 10],
                         ['x', 4, 10, 'x', 'x', 'x', 7, 'x', 19, 7, 'x', 'x']])
    num_rows, num_cols = city_map.shape
    # Define the districts
    districts = [range(0, 4), range(4, 7), range(7, 12)]
    # Define the visited costs dictionary
    visited_costs = {}
    visited_costs[(initial_state, frozenset())] = 0
    # Define the queue
    queue = [(0, 0, [], initial_state, frozenset())]
    # While there are unvisited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state, visited_districts = heapq.heappop(queue)
        # If the current state is the goal state and all districts have been visited, return the actions
        if state == goal_state and len(visited_districts) == len(districts):
            return actions
        # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops
        for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = state[0] + d_row, state[1] + d_col
            # Check if the new state is valid, ie within the bounds of the city map and not a closed workshop
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
                # Generate the new state
                new_state = (new_row, new_col)
                # The cost so far is the travel time from the current workshop to the new workshop
                new_cost = g + city_map[new_row][new_col]
                # Update the visited districts
                new_visited_districts = visited_districts.copy()
                for i, district in enumerate(districts):
                    if new_row in district:
                        new_visited_districts.add(i)
                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of unvisited states
                if (new_state, frozenset(new_visited_districts)) not in visited_costs or new_cost < visited_costs[(new_state, frozenset(new_visited_districts))]:
                    visited_costs[(new_state, frozenset(new_visited_districts))] = new_cost
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, frozenset(new_visited_districts)))
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current workshop to the goal workshop
    # The heuristic is admissible because it never overestimates the cost to reach the goal, as the travel time between any two workshops is always greater than or equal to the Manhattan distance between them
    # The heuristic is consistent because the cost of moving to a neighboring workshop is always greater than or equal to 1, which is exactly the decrease in the Manhattan distance, if the workshop is moved toward the goal workshop
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
