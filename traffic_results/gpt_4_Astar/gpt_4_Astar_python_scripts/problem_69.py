
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the puzzle, represented as 2d tuples
    initial_state = ((1, 12),)
    goal_state = (6, 3)
    # Define the map of the city
    city_map = np.array([[17, 'x', 'x', 'x', 5, 'x', 'x', 12, 16, 'x', 'x', 5, 16],
                         ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 12, 4, 6],
                         [9, 'x', 'x', 'x', 'x', 'x', 19, 'x', 'x', 13, 6, 11, 19],
                         [1, 'x', 'x', 'x', 13, 'x', 'x', 'x', 3, 2, 7, 4, 3],
                         ['x', 'x', 'x', 14, 19, 20, 10, 13, 14, 2, 'x', 9, 3],
                         [15, 'x', 11, 7, 'x', 11, 6, 16, 'x', 'x', 'x', 8, 19],
                         [19, 16, 4, 8, 5, 5, 5, 11, 10, 17, 9, 'x', 5],
                         ['x', 3, 17, 'x', 'x', 6, 17, 19, 'x', 'x', 14, 'x', 'x'],
                         ['x', 'x', 'x', 'x', 'x', 14, 'x', 10, 14, 13, 'x', 13, 'x'],
                         [15, 5, 4, 'x', 'x', 'x', 'x', 2, 12, 6, 'x', 16, 14],
                         [10, 'x', 'x', 'x', 9, 'x', 'x', 'x', 'x', 'x', 13, 2, 'x'],
                         ['x', 'x', 17, 'x', 'x', 'x', 'x', 7, 'x', 'x', 16, 'x', 'x'],
                         [12, 10, 'x', 15, 16, 'x', 'x', 7, 11, 7, 'x', 17, 'x']])
    # Define the districts
    districts = [range(0, 2), range(2, 6), range(6, 13)]
    # Define the number of rows and columns
    num_rows, num_cols = city_map.shape

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state[-1] == goal_state:
            # Check if Ben has visited at least 1 workshop in each district
            if all(any(workshop[0] in district for workshop in state) for district in districts):
                return actions

        # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops
        for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            new_workshop = (state[-1][0] + d_row, state[-1][1] + d_col)
            # Check if the move is valid, ie if the coordinate of the new workshop is a valid coordinate within the bounds of the city map and the workshop is not closed
            if (0 <= new_workshop[0] < num_rows and 0 <= new_workshop[1] < num_cols and
                city_map[new_workshop[0]][new_workshop[1]] != 'x'):
                # Generate the new state
                new_state = state + (new_workshop,)
                # The cost so far is the sum of the travel times from the initial state to the current state
                new_cost = g + city_map[new_workshop[0]][new_workshop[1]]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    h = heuristic(new_workshop, goal_state, city_map)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_workshop], new_state))
    return None


def heuristic(workshop, goal, city_map):
    # An admissible and consistent heuristic is the straight-line distance (the shortest path) from the current workshop to the goal workshop, multiplied by the minimum travel time in the city map
    # The heuristic relaxes the constraint that Ben can only move to a neighboring workshop and presumes he can move to any workshop in the city map
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring workshop is always greater than or equal to the decrease in the straight-line distance, if the workshop is moved toward the goal workshop, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal workshop from itself would be 0.
    h = ((abs(workshop[0] - goal[0]) + abs(workshop[1] - goal[1])) *
         np.min(city_map[city_map != 'x']))
    return h


print(a_star())
