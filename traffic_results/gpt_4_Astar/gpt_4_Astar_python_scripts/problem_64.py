
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (3, 0)
    goal_state = (6, 12)
    # Define the map of the city as a 2d numpy array
    city_map = np.array([[8, 'x', 12, 'x', 16, 'x', 'x', 'x', 7, 'x', 'x', 'x', 'x'],
                         ['x', 'x', 'x', 'x', 16, 'x', 7, 8, 'x', 17, 'x', 19, 'x'],
                         [7, 'x', 13, 'x', 19, 'x', 6, 'x', 14, 'x', 18, 'x', 19],
                         [9, 20, 2, 'x', 10, 6, 'x', 18, 'x', 'x', 'x', 18, 'x'],
                         ['x', 'x', 8, 12, 7, 14, 13, 9, 8, 6, 14, 11, 7],
                         ['x', 14, 'x', 'x', 'x', 19, 13, 15, 3, 12, 16, 16, 3],
                         ['x', 'x', 'x', 13, 'x', 9, 13, 10, 'x', 14, 'x', 4, 18],
                         [6, 12, 10, 'x', 'x', 18, 7, 20, 18, 'x', 13, 1, 'x'],
                         ['x', 5, 'x', 18, 12, 'x', 'x', 3, 12, 14, 19, 16, 'x'],
                         [10, 'x', 19, 'x', 'x', 'x', 'x', 11, 14, 16, 12, 'x', 8],
                         [8, 'x', 'x', 'x', 'x', 'x', 'x', 9, 16, 15, 'x', 'x', 8],
                         ['x', 'x', 2, 'x', 1, 'x', 'x', 16, 'x', 'x', 3, 'x', 'x'],
                         [9, 'x', 5, 'x', 'x', 15, 'x', 'x', 'x', 7, 15, 9, 'x']])
    num_rows, num_cols = city_map.shape
    # Define the districts of the city
    districts = [(0, 3), (4, 5), (6, 12)]
    # Define the directions in which Ben can move
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]


    visited_costs = {}
    visited_costs[(initial_state, frozenset([0]))] = 0


    queue = [(0, 0, [], initial_state, frozenset([0]))]


    while queue:
        _, g, actions, state, visited_districts = heapq.heappop(queue)


        # Check if the current state is the goal state
        if state == goal_state and len(visited_districts) == len(districts):
            return actions


        # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring cells
        for d_row, d_col in directions:
            new_row, new_col = state[0] + d_row, state[1] + d_col
            # Check if the new state would be valid, ie the new cell must be within the bounds of the city map and not be a closed workshop
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
                # Generate the new state
                new_state = (new_row, new_col)
                # The cost so far is the sum of the travel times, as the task is to minimize the total travel time
                new_cost = g + int(city_map[new_row][new_col])
                # Update the set of visited districts
                new_visited_districts = visited_districts.copy()
                for i, (start, end) in enumerate(districts):
                    if start <= new_row <= end:
                        new_visited_districts.add(i)
                        break


                if (new_state, frozenset(new_visited_districts)) not in visited_costs or new_cost < visited_costs[(new_state, frozenset(new_visited_districts))]:
                    visited_costs[(new_state, frozenset(new_visited_districts))] = new_cost
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, frozenset(new_visited_districts)))
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the Manhattan distance (the shortest path) from the current cell to the goal cell
    # The heuristic relaxes the constraint that Ben cannot move through closed workshops and presumes Ben can move directly to the goal cell
    # Thus the heuristic reports a lower estimate on the cost to reach the goal cell and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring cell is always 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal cell, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal cell is 0, as the distance of the goal cell from itself would be 0.
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
