
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (1, 13)
    goal_state = (7, 4)
    # Define the map of the city as a 2d numpy array
    city_map = np.array([[15, 19, 13, 4, 'x', 'x', 13, 7, 16, 6, 'x', 'x', 17, 'x'],
                         [2, 2, 'x', 7, 'x', 12, 12, 'x', 19, 'x', 10, 4, 14, 2],
                         [11, 'x', 'x', 3, 7, 'x', 7, 'x', 'x', 6, 'x', 19, 'x', 1],
                         ['x', 'x', 11, 'x', 3, 'x', 17, 'x', 1, 20, 17, 8, 15, 1],
                         ['x', 'x', 13, 'x', 12, 17, 5, 4, 'x', 16, 9, 'x', 19, 14],
                         ['x', 16, 'x', 'x', 13, 17, 14, 6, 2, 17, 19, 6, 13, 6],
                         ['x', 1, 'x', 'x', 3, 10, 2, 18, 7, 8, 'x', 8, 'x', 'x'],
                         [12, 2, 1, 6, 11, 7, 10, 'x', 'x', 'x', 4, 2, 8, 'x'],
                         ['x', 'x', 'x', 13, 16, 2, 'x', 6, 9, 2, 11, 7, 14, 6],
                         ['x', 'x', 'x', 'x', 'x', 11, 'x', 16, 'x', 'x', 'x', 'x', 'x', 3],
                         ['x', 'x', 'x', 'x', 10, 'x', 3, 'x', 18, 9, 'x', 'x', 'x', 15],
                         ['x', 'x', 11, 9, 3, 'x', 'x', 16, 'x', 5, 'x', 4, 10, 'x'],
                         [18, 1, 13, 'x', 7, 'x', 7, 5, 'x', 11, 10, 2, 'x', 2],
                         ['x', 'x', 'x', 'x', 'x', 'x', 'x', 11, 'x', 10, 'x', 'x', 14, 6]])
    num_rows, num_cols = city_map.shape
    # Define the districts of the city
    districts = [range(0, 2), range(2, 7), range(7, 14)]
    # Define the set of visited states
    visited_states = set()
    # Define the priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, [initial_state], initial_state, {initial_state[0]})]
    # While there are unvisited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state, visited_districts = heapq.heappop(queue)
        # If the current state is the goal state and all districts have been visited, return the path to this state
        if state == goal_state and len(visited_districts) == len(districts):
            return path
        # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops
        for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = state[0] + d_row, state[1] + d_col
            # Check if the new state is valid, ie within the bounds of the city and not a closed workshop
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
                new_state = (new_row, new_col)
                # Check if the new state has been visited before
                if new_state not in visited_states:
                    visited_states.add(new_state)
                    # The cost so far is the sum of the travel times of the workshops visited
                    new_cost = g + int(city_map[new_state[0]][new_state[1]])
                    # Update the set of visited districts
                    new_visited_districts = visited_districts.copy()
                    for i, district in enumerate(districts):
                        if new_state[0] in district:
                            new_visited_districts.add(i)
                    # Add the new state to the queue of not yet visited states
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [new_state], new_state, new_visited_districts))
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current state to the goal state
    # The heuristic relaxes the constraint that Ben cannot move through closed workshops and presumes Ben can move directly to the goal state
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring workshop is always greater than or equal to 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal state, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal state from itself is 0
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
