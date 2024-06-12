
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (3, 12)
    goal_state = (6, 2)
    # Define the map of the city as a 2d numpy array
    city_map = np.array([[13, 13, 16, 8, 'x', 19, 1, 18, 13, 8, 'x', 7, 'x'],
                         ['x', 13, 'x', 15, 'x', 12, 20, 1, 13, 19, 4, 17, 'x'],
                         ['x', 12, 9, 11, 13, 12, 2, 12, 19, 5, 19, 16, 8],
                         ['x', 12, 18, 19, 'x', 7, 'x', 12, 3, 2, 'x', 16, 11],
                         ['x', 7, 'x', 'x', 8, 13, 15, 3, 1, 'x', 15, 15, 'x'],
                         [11, 9, 'x', 16, 2, 10, 1, 2, 16, 1, 'x', 10, 12],
                         ['x', 'x', 9, 9, 7, 'x', 6, 'x', 'x', 10, 7, 2, 'x'],
                         ['x', 13, 10, 8, 1, 11, 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
                         [11, 14, 'x', 'x', 'x', 'x', 4, 8, 'x', 'x', 18, 'x', 'x'],
                         [13, 14, 'x', 10, 'x', 'x', 16, 'x', 'x', 'x', 'x', 'x', 'x'],
                         ['x', 'x', 16, 'x', 10, 'x', 17, 'x', 12, 'x', 10, 'x', 5],
                         [9, 'x', 10, 'x', 19, 16, 'x', 14, 16, 12, 15, 7, 'x'],
                         [1, 'x', 8, 10, 14, 'x', 6, 9, 'x', 'x', 8, 11, 11]])
    num_rows = city_map.shape[0]
    num_cols = city_map.shape[1]
    # Define the districts of the city
    districts = [(0, 1), (2, 5), (6, 12)]
    # Define the visited costs dictionary
    visited_costs = {}
    visited_costs[(initial_state, frozenset())] = 0
    # Define the priority queue
    queue = [(0, 0, [], initial_state, frozenset())]
    # Define the directions in which Ben can move
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    # While there are unvisited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state, visited_districts = heapq.heappop(queue)
        # If the current state is the goal state and Ben has visited all districts, return the actions taken
        if state == goal_state and len(visited_districts) == len(districts):
            return actions
        # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops
        for d_row, d_col in directions:
            new_row, new_col = state[0] + d_row, state[1] + d_col
            # Check if the move is valid, ie if the coordinate of the workshop to move to is a valid coordinate within the bounds of the city map and the workshop is not closed
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
                # The action is valid, generate the new state
                new_state = (new_row, new_col)
                # The cost so far is the travel time to the new workshop
                new_cost = g + int(city_map[new_row][new_col])
                # Update the set of visited districts
                new_visited_districts = visited_districts.copy()
                for i, district in enumerate(districts):
                    if district[0] <= new_row <= district[1]:
                        new_visited_districts.add(i)
                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if (new_state, frozenset(new_visited_districts)) not in visited_costs or new_cost < visited_costs[(new_state, frozenset(new_visited_districts))]:
                    visited_costs[(new_state, frozenset(new_visited_districts))] = new_cost
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, frozenset(new_visited_districts)))
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the Manhattan distance (the shortest path) from the current workshop to the goal workshop
    # The heuristic relaxes the constraint that Ben can only move to a neighboring workshop and presumes Ben can move directly to the goal workshop
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring workshop is always 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal workshop, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal workshop from itself would be 0.
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
