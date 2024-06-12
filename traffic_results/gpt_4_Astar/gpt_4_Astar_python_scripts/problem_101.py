
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (7, 0)
    goal_state = (4, 13)
    # Define the map of the city as a 2d numpy array
    city_map = np.array([[np.inf, 3, 1, 19, 8, 1, 4, 18, 15, 17, 4, 3, np.inf, 3, np.inf],
                         [np.inf, 11, np.inf, np.inf, np.inf, 12, np.inf, 19, 15, 4, np.inf, np.inf, np.inf, np.inf, np.inf],
                         [4, 1, np.inf, 8, np.inf, 12, 17, np.inf, 14, 4, 9, 11, 13, 6, 19],
                         [2, np.inf, 6, 14, 15, np.inf, 18, 9, np.inf, 10, 10, np.inf, np.inf, 1, np.inf],
                         [np.inf, 11, np.inf, 8, np.inf, 5, np.inf, 8, 7, 6, np.inf, np.inf, 13, 6, np.inf],
                         [np.inf, np.inf, np.inf, 17, np.inf, 13, np.inf, np.inf, np.inf, np.inf, 18, 19, 5, np.inf, np.inf],
                         [np.inf, 12, 18, np.inf, np.inf, np.inf, 19, np.inf, 12, np.inf, 11, 7, 19, 12, np.inf],
                         [6, 6, np.inf, 6, 4, np.inf, 18, np.inf, np.inf, 15, 18, np.inf, 6, 8, np.inf],
                         [10, 10, np.inf, np.inf, 6, 4, 11, 19, np.inf, 9, np.inf, 2, np.inf, 3, 14],
                         [np.inf, 18, 14, 10, np.inf, 1, np.inf, 6, np.inf, 15, np.inf, 6, np.inf, 14, np.inf],
                         [np.inf, np.inf, 7, 10, np.inf, 2, np.inf, 7, 14, 4, 11, np.inf, np.inf, np.inf, np.inf],
                         [12, np.inf, 6, np.inf, 8, 5, 6, 6, 8, np.inf, np.inf, np.inf, np.inf, 4, 7],
                         [np.inf, np.inf, 1, 8, 10, 4, 10, 17, 19, 11, 2, np.inf, np.inf, np.inf, 16],
                         [np.inf, np.inf, np.inf, 17, 8, 19, np.inf, 14, np.inf, 17, 17, 5, 7, 6, 7],
                         [1, np.inf, 14, np.inf, 3, np.inf, 18, 6, 18, 8, np.inf, 13, 10, np.inf, np.inf]])
    num_rows, num_cols = city_map.shape
    # Define the districts of the city
    districts = [range(0, 5), range(5, 9), range(9, 15)]
    # Define the directions in which Ben can move
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


    visited_costs = {}
    visited_costs[(initial_state, frozenset())] = 0


    queue = [(0, 0, [], initial_state, frozenset())]


    while queue:
        _, g, actions, state, visited_districts = heapq.heappop(queue)


        # Check if the current state is the goal state
        if state == goal_state and len(visited_districts) == len(districts):
            return actions


        # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops
        for d_row, d_col in directions:
            new_row, new_col = state[0] + d_row, state[1] + d_col
            # Check if the new state is valid, ie within the bounds of the city and not a closed workshop
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != np.inf:
                # Generate the new state
                new_state = (new_row, new_col)
                # The cost so far is the sum of the travel times, as the task is to minimize the total travel time
                new_cost = g + city_map[new_row][new_col]
                # Update the set of visited districts
                new_visited_districts = visited_districts.copy()
                for i, district in enumerate(districts):
                    if new_row in district:
                        new_visited_districts.add(i)


                if (new_state, frozenset(new_visited_districts)) not in visited_costs or new_cost < visited_costs[(new_state, frozenset(new_visited_districts))]:
                    visited_costs[(new_state, frozenset(new_visited_districts))] = new_cost
                    h = heuristic(new_state, goal_state, city_map)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, frozenset(new_visited_districts)))
    return None


def heuristic(state, goal, city_map):
    # An admissible and consistent heuristic for this problem is the straight-line distance (Euclidean distance) from the current state to the goal state, divided by the maximum speed (minimum travel time) in the city
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as it assumes Ben can travel in a straight line to the goal, which is not possible in the actual problem where Ben can only move in 4 directions
    # The heuristic is consistent because the cost of moving from one state to a neighboring state is always greater than or equal to the decrease in the heuristic, as the straight-line distance to the goal decreases by at most 1 unit (equal to the cost of reaching the successor state, ie the travel time to the neighboring state), and the heuristic estimate for the goal state is 0, as the distance of the goal state from itself is 0
    max_speed = np.min(city_map[city_map != np.inf])
    return np.sqrt((state[0] - goal[0]) ** 2 + (state[1] - goal[1]) ** 2) / max_speed


print(a_star())
