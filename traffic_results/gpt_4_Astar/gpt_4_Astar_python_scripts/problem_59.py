
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (2, 0)
    goal_state = (7, 8)
    # Define the map of the city as a 2d numpy array
    city_map = np.array([[4, 1, 20, 15, 9, 'x', 8, 6, 'x', 'x', 14, 'x'],
                         [5, 11, 9, 12, 10, 4, 15, 18, 7, 'x', 'x', 13],
                         [15, 9, 1, 'x', 18, 3, 1, 19, 'x', 'x', 17, 17],
                         ['x', 17, 11, 10, 'x', 19, 8, 'x', 'x', 'x', 'x', 7],
                         [5, 'x', 1, 'x', 14, 13, 4, 8, 5, 'x', 13, 14],
                         [16, 6, 'x', 'x', 'x', 17, 'x', 15, 4, 'x', 'x', 15],
                         ['x', 'x', 'x', 15, 'x', 19, 10, 'x', 16, 18, 11, 1],
                         [6, 8, 'x', 3, 'x', 5, 5, 'x', 3, 8, 9, 14],
                         [10, 14, 'x', 'x', 'x', 'x', 'x', 'x', 6, 2, 'x', 'x'],
                         [12, 'x', 'x', 6, 11, 4, 'x', 'x', 12, 'x', 4, 16],
                         [4, 'x', 'x', 'x', 11, 'x', 'x', 'x', 18, 16, 'x', 10],
                         ['x', 6, 'x', 'x', 11, 'x', 5, 13, 8, 1, 17, 9]])
    num_rows, num_cols = city_map.shape
    # Define the districts of the city
    districts = [range(0, 2), range(2, 7), range(7, 12)]
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
            # Check if the new state would be valid, ie the new workshop must be within the bounds of the city and not be closed
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
                # Generate the new state
                new_state = (new_row, new_col)
                # The cost so far is the sum of the travel times, as the task is to minimize the total travel time
                new_cost = g + int(city_map[new_row][new_col])
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
    # An admissible and consistent heuristic for this problem is the Manhattan distance (the shortest path) from the current workshop to the goal workshop, multiplied by the minimum travel time
    # The heuristic relaxes the constraint that Ben can only move to a neighboring workshop and presumes he can move directly to the goal workshop
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring workshop is always greater than or equal to the minimum travel time, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal workshop, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal workshop from itself would be 0.
    min_travel_time = np.min(city_map[city_map != 'x'].astype(int))
    h = (abs(state[0] - goal[0]) + abs(state[1] - goal[1])) * min_travel_time
    return h


print(a_star())
