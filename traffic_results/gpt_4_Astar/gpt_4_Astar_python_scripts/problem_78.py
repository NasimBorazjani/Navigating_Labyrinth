
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (7, 12)
    goal_state = (2, 0)
    # Define the map of the city as a 2d numpy array
    city_map = np.array([[np.inf, np.inf, np.inf, 16, 11, 12, np.inf, np.inf, 17, 3, np.inf, np.inf, 4, 6],
                         [4, 17, np.inf, np.inf, 3, np.inf, np.inf, 1, 9, 11, 12, 4, np.inf, np.inf],
                         [5, np.inf, np.inf, 7, 14, 4, 5, 7, 13, 4, 7, np.inf, np.inf, np.inf],
                         [6, 6, 19, 3, 15, np.inf, np.inf, np.inf, np.inf, 4, 10, 19, 2, 4],
                         [3, 16, 8, np.inf, 5, np.inf, 12, 17, 16, np.inf, 9, 5, 6, np.inf],
                         [17, 2, np.inf, np.inf, 16, np.inf, 5, np.inf, np.inf, 5, 17, 7, 2, 5],
                         [19, np.inf, np.inf, np.inf, np.inf, 2, 15, 15, np.inf, 3, 11, np.inf, 4, np.inf],
                         [np.inf, np.inf, 11, np.inf, np.inf, 17, 5, np.inf, 5, np.inf, np.inf, 19, 6, np.inf],
                         [16, 17, 16, np.inf, 12, np.inf, 2, 18, 9, 7, np.inf, 13, np.inf, np.inf],
                         [18, 11, np.inf, np.inf, 19, 5, np.inf, np.inf, 18, 4, np.inf, np.inf, np.inf, np.inf],
                         [np.inf, np.inf, np.inf, np.inf, 2, 5, 4, 12, 3, np.inf, 4, 14, 7, 19],
                         [18, np.inf, np.inf, np.inf, 7, 17, np.inf, np.inf, 3, 15, np.inf, 16, np.inf, 10],
                         [np.inf, 11, 15, np.inf, np.inf, np.inf, np.inf, np.inf, 2, 13, np.inf, np.inf, np.inf, 3],
                         [4, 8, np.inf, np.inf, np.inf, np.inf, 12, 13, np.inf, np.inf, 19, np.inf, 6, np.inf]])
    num_rows, num_cols = city_map.shape
    # Define the districts in the city
    districts = [range(0, 3), range(3, 7), range(7, 14)]
    # Define the visited costs dictionary
    visited_costs = {}
    visited_costs[initial_state] = 0
    # Define the queue
    queue = [(0, 0, [], initial_state, [False]*3)]
    # While there are unvisited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state, visited_districts = heapq.heappop(queue)
        # If the current state is the goal state and all districts have been visited, return the actions
        if state == goal_state and all(visited_districts):
            return actions
        # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring cells
        for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = state[0] + d_row, state[1] + d_col
            # Check if the new state is valid, ie within the bounds of the city map and not a closed workshop
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != np.inf:
                # Generate the new state
                new_state = (new_row, new_col)
                # The cost so far is the sum of the travel times, as the task is to minimize the total travel time
                new_cost = g + city_map[new_row][new_col]
                # Update the visited districts
                new_visited_districts = visited_districts[:]
                for i, district in enumerate(districts):
                    if new_row in district:
                        new_visited_districts[i] = True
                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, new_visited_districts))
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current state to the goal state
    # The heuristic relaxes the constraint that Ben cannot move through closed workshops and presumes Ben can move directly to the goal state
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring cell is always equal to the travel time, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal state, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal state from itself is 0.
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
