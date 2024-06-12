
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (3, 1)
    goal_state = (5, 13)
    # Define the map of the city as a 2d numpy array
    city_map = np.array([[np.inf, 7, np.inf, 13, 8, 2, 15, 2, 5, 15, 6, 4, 7, np.inf],
                         [np.inf, 6, 19, 17, 5, 13, 15, 2, 11, 5, np.inf, np.inf, 9, 8],
                         [16, 12, 10, 7, 8, 19, 19, 9, 5, 10, 2, np.inf, np.inf, 12],
                         [np.inf, 1, 19, 20, np.inf, 3, 4, 18, np.inf, np.inf, 10, 1, 12, 2],
                         [np.inf, 1, 4, 1, 1, 10, 4, np.inf, 12, np.inf, 5, 10, 3, 8],
                         [np.inf, np.inf, np.inf, 7, np.inf, np.inf, 16, 12, np.inf, np.inf, np.inf, 13, 6, 10],
                         [np.inf, np.inf, 11, 12, 13, 15, 8, np.inf, 12, 1, 16, 14, 8, 15],
                         [np.inf, 11, np.inf, 15, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 5, np.inf, np.inf, 14],
                         [1, np.inf, np.inf, 8, np.inf, 13, 17, np.inf, 3, 12, np.inf, np.inf, np.inf, np.inf],
                         [14, 3, np.inf, 4, np.inf, np.inf, np.inf, 12, np.inf, 7, np.inf, np.inf, np.inf, np.inf],
                         [np.inf, 5, 15, np.inf, 10, 17, np.inf, np.inf, 6, 9, 2, np.inf, np.inf, np.inf],
                         [1, 7, 17, 1, np.inf, np.inf, np.inf, np.inf, 11, np.inf, np.inf, np.inf, np.inf, 12],
                         [np.inf, np.inf, 14, 18, 8, 19, 19, 16, np.inf, 6, 5, 16, 17, 7],
                         [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 19, 17, np.inf, np.inf, 2, 12, np.inf, np.inf]])
    num_rows, num_cols = city_map.shape
    # Define the districts of the city
    districts = [range(0, 4), range(4, 6), range(6, 14)]
    # Define the visited costs dictionary
    visited_costs = {}
    visited_costs[(initial_state, frozenset())] = 0
    # Define the priority queue
    queue = [(0, 0, [], initial_state, frozenset())]
    # Define the directions in which Ben can move
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # While there are unvisited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state, visited_districts = heapq.heappop(queue)
        # If the current state is the goal state and Ben has visited all districts, return the actions taken
        if state == goal_state and len(visited_districts) == len(districts):
            return actions
        # Generate all possible actions from the current state, which includes moving in any of the 4 directions
        for d_row, d_col in directions:
            new_state = (state[0] + d_row, state[1] + d_col)
            # Check if the new state is valid, ie within the bounds of the city and not a closed workshop
            if (0 <= new_state[0] < num_rows and 0 <= new_state[1] < num_cols and
                city_map[new_state] != np.inf):
                # The cost so far is the sum of the travel times
                new_cost = g + city_map[new_state]
                # Update the set of visited districts
                new_visited_districts = visited_districts.copy()
                for i, district in enumerate(districts):
                    if new_state[0] in district:
                        new_visited_districts.add(i)
                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of unvisited states
                if (new_state, frozenset(new_visited_districts)) not in visited_costs or new_cost < visited_costs[(new_state, frozenset(new_visited_districts))]:
                    visited_costs[(new_state, frozenset(new_visited_districts))] = new_cost
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, frozenset(new_visited_districts)))
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current state to the goal state
    # The heuristic is admissible because it never overestimates the cost to reach the goal, as it assumes Ben can move directly to the goal without any obstacles
    # The heuristic is consistent because the cost of moving to a neighboring state is always 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal state
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
