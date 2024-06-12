
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (3, 0)
    goal_state = (6, 12)
    # Define the map of the city as a 2d numpy array
    city_map = np.array([['x', 6, 19, 13, 'x', 16, 11, 6, 14, 15, 7, 'x', 'x', 'x'],
                         ['x', 6, 16, 15, 'x', 19, 16, 18, 'x', 8, 10, 'x', 'x', 'x'],
                         ['x', 5, 10, 14, 2, 'x', 'x', 'x', 11, 'x', 11, 'x', 'x', 'x'],
                         [6, 13, 15, 10, 'x', 'x', 'x', 'x', 19, 'x', 'x', 'x', 2, 'x'],
                         ['x', 15, 10, 6, 6, 8, 10, 9, 11, 'x', 'x', 'x', 16, 'x'],
                         ['x', 'x', 'x', 8, 15, 12, 10, 19, 1, 18, 19, 4, 'x', 10],
                         [1, 17, 'x', 'x', 6, 8, 4, 'x', 15, 8, 10, 6, 4, 'x'],
                         ['x', 'x', 'x', 'x', 13, 'x', 5, 'x', 9, 10, 'x', 'x', 'x', 'x'],
                         [12, 'x', 11, 'x', 13, 'x', 11, 7, 5, 13, 'x', 'x', 6, 15],
                         ['x', 18, 19, 'x', 'x', 'x', 3, 'x', 16, 11, 'x', 15, 'x', 'x'],
                         ['x', 'x', 'x', 'x', 'x', 'x', 2, 15, 'x', 'x', 8, 'x', 'x', 'x'],
                         [11, 'x', 6, 13, 12, 'x', 12, 'x', 'x', 9, 'x', 17, 'x', 'x'],
                         ['x', 1, 'x', 18, 18, 3, 'x', 11, 13, 1, 13, 'x', 'x', 'x'],
                         ['x', 'x', 'x', 'x', 'x', 6, 'x', 'x', 8, 'x', 'x', 'x', 4, 11]])
    num_rows, num_cols = city_map.shape
    # Define the districts of the city
    districts = [range(0, 3), range(3, 6), range(6, 14)]
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


        # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring cells
        for d_row, d_col in directions:
            new_row, new_col = state[0] + d_row, state[1] + d_col
            # Check if the new state is valid, ie within the bounds of the city and not a closed workshop
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
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
                    h = heuristic(new_state, goal_state, visited_districts, districts)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, frozenset(new_visited_districts)))
    return None


def heuristic(state, goal, visited_districts, districts):
    # An admissible and consistent heuristic for this problem is the Manhattan distance (the shortest path) from the current state to the goal state
    # The heuristic relaxes the constraint that Ben must visit at least 1 workshop in each district and presumes Ben can move directly to the goal state
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring cell is always 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal state, otherwise the estimated cost of the successor state is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal state from itself is 0.
    h = abs(state[0] - goal[0]) + abs(state[1] - goal[1])
    # Add a penalty for each district not yet visited
    h += len(districts) - len(visited_districts)
    return h


print(a_star())
