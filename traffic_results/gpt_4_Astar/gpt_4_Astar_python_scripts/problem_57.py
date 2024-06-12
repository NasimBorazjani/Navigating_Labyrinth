
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (7, 0)
    goal_state = (3, 8)
    # Define the map of the city as a 2d numpy array
    city_map = np.array([[17, 9, 11, 5, 19, 4, 18, 'x', 5, 8, 'x', 'x'],
                         [6, 13, 'x', 9, 2, 20, 11, 20, 7, 'x', 'x', 3],
                         [4, 17, 'x', 18, 2, 10, 'x', 16, 'x', 18, 'x', 'x'],
                         [12, 10, 9, 14, 'x', 'x', 12, 6, 1, 2, 'x', 'x'],
                         [5, 'x', 'x', 3, 'x', 4, 9, 14, 8, 'x', 10, 12],
                         [1, 'x', 6, 3, 18, 18, 17, 17, 10, 'x', 'x', 10],
                         [13, 'x', 'x', 'x', 'x', 'x', 14, 'x', 1, 19, 'x', 7],
                         [11, 'x', 'x', 5, 9, 'x', 18, 19, 13, 13, 'x', 10],
                         ['x', 'x', 11, 'x', 17, 'x', 'x', 'x', 14, 17, 'x', 13],
                         [19, 'x', 'x', 'x', 'x', 19, 12, 7, 3, 14, 'x', 9],
                         ['x', 12, 7, 15, 1, 'x', 16, 11, 9, 17, 'x', 'x'],
                         ['x', 'x', 'x', 10, 'x', 1, 7, 'x', 'x', 'x', 6, 12]])
    num_rows, num_cols = city_map.shape
    # Define the districts of the city
    districts = {1: range(0, 4), 2: range(4, 7), 3: range(7, 12)}
    # Define the directions in which Ben can move
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # left, right, up, down

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], initial_state, {1: False, 2: False, 3: False})]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state, visited_districts = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state and all(visited_districts.values()):
            return actions

        # Generate all possible actions from the current state, which includes moving in any of the 4 directions
        for direction in directions:
            new_state = (state[0] + direction[0], state[1] + direction[1])
            # Check if the new state is valid, ie within the bounds of the city map and not a closed workshop
            if (0 <= new_state[0] < num_rows and 0 <= new_state[1] < num_cols and city_map[new_state] != 'x'):
                # The cost so far is the travel time from the current workshop to the new workshop
                new_cost = g + int(city_map[new_state])
                # Update the visited districts
                new_visited_districts = visited_districts.copy()
                for district, rows in districts.items():
                    if new_state[0] in rows:
                        new_visited_districts[district] = True

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, new_visited_districts))
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current state to the goal state
    # The heuristic relaxes the constraint that Ben can only move to neighboring workshops and presumes he can move directly to the goal workshop
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring workshop is always 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal workshop, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal workshop from itself would be 0.
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
