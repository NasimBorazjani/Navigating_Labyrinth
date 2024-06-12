
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (4, 12)
    goal_state = (7, 0)
    # Define the map of the city
    city_map = np.array([['x', 'x', 17, 7, 'x', 'x', 11, 4, 5, 15, 17, 6, 6, 2],
                         [17, 'x', 'x', 6, 'x', 'x', 'x', 'x', 1, 8, 'x', 'x', 'x', 7],
                         ['x', 'x', 'x', 17, 4, 10, 6, 4, 'x', 8, 16, 11, 'x', 'x'],
                         ['x', 4, 'x', 'x', 10, 'x', 8, 10, 'x', 11, 'x', 'x', 1, 'x'],
                         ['x', 'x', 11, 9, 4, 'x', 8, 8, 'x', 'x', 'x', 16, 13, 8],
                         ['x', 12, 3, 15, 13, 13, 'x', 15, 19, 'x', 2, 2, 6, 'x'],
                         [15, 1, 'x', 'x', 'x', 'x', 5, 4, 'x', 5, 12, 2, 5, 'x'],
                         [20, 13, 7, 18, 8, 18, 5, 2, 17, 7, 11, 'x', 15, 13],
                         [4, 11, 'x', 'x', 10, 9, 'x', 18, 14, 'x', 19, 'x', 'x', 'x'],
                         [19, 'x', 2, 'x', 18, 17, 10, 'x', 'x', 'x', 13, 15, 'x', 10],
                         [16, 5, 2, 3, 13, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 3],
                         ['x', 'x', 'x', 'x', 17, 9, 'x', 'x', 'x', 'x', 'x', 6, 'x', 'x'],
                         [11, 'x', 'x', 9, 14, 'x', 'x', 16, 'x', 15, 13, 13, 15, 1],
                         [9, 'x', 'x', 10, 14, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 1, 19]])
    num_rows, num_cols = city_map.shape
    # Define the districts of the city
    districts = [set(range(0, 5)), set(range(5, 7)), set(range(7, 14))]

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], initial_state, [initial_state])]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state, path = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state:
            # Check if Ben has visited at least 1 workshop in each district
            if all(any(workshop[0] in district for workshop in path) for district in districts):
                return actions

        # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops
        for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            new_row, new_col = state[0] + d_row, state[1] + d_col
            # Check if the move is valid, ie if the coordinate of the workshop to move to is a valid coordinate within the bounds of the city map and the workshop is not closed
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
                # The action is valid, generate the new state
                new_state = (new_row, new_col)
                # The cost so far is the travel time to the new workshop, as our objective is to minimize the travel time
                new_cost = g + city_map[new_row][new_col]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [new_state], new_state, path + [new_state]))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) of the current workshop from the goal workshop
    # The heuristic relaxes the constraint that Ben can only move to a neighboring workshop and presumes Ben can move directly to the goal workshop
    # Thus the heuristic reports a lower estimate on the travel time to reach the goal workshop and is admissible
    # The heuristic is consistent because the travel time to move to a neighboring workshop is always greater than or equal to 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal workshop, otherwise the estimated travel time of the successor workshop is the same or higher, and the heuristic estimate for the goal workshop is 0, as the distance of the goal workshop from itself would be 0.
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
