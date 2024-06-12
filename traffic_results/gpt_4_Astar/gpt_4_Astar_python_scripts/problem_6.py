
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (5, 5)
    goal_state = (1, 0)
    # Define the map of the city as a 2d numpy array
    city_map = np.array([[6, 16, 'x', 'x', 15, 'x', 14, 11, 'x'],
                         [5, 2, 1, 'x', 3, 'x', 4, 13, 'x'],
                         ['x', 7, 'x', 'x', 13, 'x', 10, 14, 5],
                         [6, 16, 'x', 13, 6, 'x', 16, 'x', 'x'],
                         ['x', 1, 17, 'x', 6, 3, 'x', 'x', 3],
                         [11, 10, 7, 19, 15, 8, 12, 6, 'x'],
                         [18, 'x', 'x', 9, 8, 9, 'x', 'x', 13],
                         [4, 'x', 'x', 'x', 18, 20, 'x', 'x', 'x'],
                         ['x', 'x', 8, 'x', 18, 2, 6, 13, 'x']])
    num_rows, num_cols = city_map.shape
    # Define the districts of the city
    districts = {1: range(0, 2), 2: range(2, 5), 3: range(5, 9)}

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], initial_state, {1, 2, 3})]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state, districts_to_visit = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state and not districts_to_visit:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops
        for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = state[0] + d_row, state[1] + d_col
            # Check if the move is valid, ie if the coordinate of the workshop to move to is a valid coordinate within the bounds of the city map and the workshop is not closed
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
                # The move is valid, generate the new state
                new_state = (new_row, new_col)
                # The cost so far is the sum of the travel times, as our objective is to minimize the total travel time
                new_cost = g + city_map[new_row][new_col]
                # Update the set of districts to visit
                new_districts_to_visit = districts_to_visit.copy()
                for district, rows in districts.items():
                    if new_row in rows:
                        new_districts_to_visit.discard(district)

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [new_state], new_state, new_districts_to_visit))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current state to the goal state
    # The heuristic relaxes the constraint that Ben can only move to a neighboring workshop and presumes Ben can move directly to the goal workshop
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring workshop is always 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal workshop, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal workshop from itself would be 0.
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
