
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the puzzle, represented as 2d tuples
    initial_state = ((5, 1),)
    goal_state = (3, 9)
    # Define the map of the city
    city_map = np.array([[18, 19, 9, 'x', 'x', 'x', 3, 'x', 8, 'x'],
                         [13, 2, 3, 15, 3, 'x', 8, 9, 'x', 'x'],
                         ['x', 6, 18, 1, 20, 7, 16, 8, 1, 19],
                         ['x', 'x', 'x', 20, 14, 'x', 19, 11, 9, 6],
                         [2, 'x', 'x', 6, 5, 6, 7, 1, 'x', 8],
                         [17, 9, 5, 3, 3, 'x', 16, 18, 'x', 8],
                         [10, 'x', 14, 16, 'x', 8, 'x', 9, 6, 'x'],
                         ['x', 17, 8, 11, 12, 'x', 4, 8, 'x', 13],
                         ['x', 'x', 6, 'x', 'x', 'x', 'x', 13, 'x', 7],
                         [9, 'x', 'x', 'x', 3, 10, 'x', 3, 10, 1]])
    num_rows = 10
    num_cols = 10
    # Define the districts
    districts = [range(0, 4), range(4, 5), range(5, 10)]

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        # The goal state is where the last workshop in the state is the goal workshop and Ben has visited at least 1 workshop in each district
        if state[-1] == goal_state and all(any(workshop[0] in district for workshop in state) for district in districts):
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops from the current workshop
        # Generate the coordinates of the neighboring workshops
        current_workshop = state[-1]
        for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            neighbor_workshop = (current_workshop[0] + d_row, current_workshop[1] + d_col)
            # Check if the move is valid, ie if the coordinate of the workshop to be moved to is a valid coordinate within the bounds of the city and the workshop is not closed
            if (0 <= neighbor_workshop[0] < num_rows and 0 <= neighbor_workshop[1] < num_cols and
                city_map[neighbor_workshop[0]][neighbor_workshop[1]] != 'x'):
                # The move is valid, generate the new state
                new_state = state + (neighbor_workshop,)
                # The cost so far is the sum of the travel times from the initial workshop to the current workshop
                new_cost = g + int(city_map[neighbor_workshop[0]][neighbor_workshop[1]])

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(neighbor_workshop, goal_state), new_cost, actions + [neighbor_workshop], new_state))
    return None


def heuristic(workshop, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) of the current workshop from the goal workshop
    # The heuristic relaxes the constraint that Ben can only move to a neighboring workshop and presumes Ben can move directly to the goal workshop
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring workshop is always 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal workshop, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal workshop from itself would be 0.
    return abs(workshop[0] - goal[0]) + abs(workshop[1] - goal[1])


print(a_star())
