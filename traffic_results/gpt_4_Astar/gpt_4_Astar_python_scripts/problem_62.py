
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (8, 2)
    goal_state = (2, 9)
    # Define the districts
    districts = [(0, 2), (3, 7), (8, 12)]
    # Define the map of the city
    city_map = np.array([[5, 15, 15, 5, 6, 19, 'x', 9, 2, 'x', 16, 'x', 15],
                         [16, 'x', 'x', 7, 5, 'x', 'x', 'x', 5, 2, 19, 'x', 3],
                         ['x', 11, 2, 19, 17, 5, 11, 6, 3, 18, 15, 16, 'x'],
                         [2, 'x', 12, 'x', 20, 11, 7, 19, 2, 'x', 4, 14, 'x'],
                         [3, 'x', 19, 'x', 11, 19, 'x', 14, 'x', 12, 'x', 18, 7],
                         [6, 'x', 5, 8, 3, 12, 12, 11, 5, 14, 'x', 6, 'x'],
                         ['x', 'x', 13, 2, 'x', 20, 'x', 'x', 'x', 18, 18, 'x', 3],
                         ['x', 'x', 13, 1, 10, 18, 'x', 'x', 'x', 'x', 10, 'x', 15],
                         [10, 'x', 9, 2, 17, 19, 16, 8, 'x', 18, 10, 'x', 13],
                         ['x', 'x', 2, 8, 2, 7, 'x', 17, 'x', 1, 'x', 9, 'x'],
                         ['x', 13, 'x', 19, 15, 3, 15, 13, 1, 12, 4, 7, 'x'],
                         [14, 'x', 'x', 'x', 'x', 'x', 'x', 16, 'x', 15, 'x', 'x', 'x'],
                         [3, 15, 'x', 6, 'x', 9, 'x', 'x', 9, 1, 6, 'x', 5]])

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [initial_state], initial_state, [0])]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state, visited_districts = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state and len(set(visited_districts)) == len(districts):
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring cells
        for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            new_state = (state[0] + d_row, state[1] + d_col)
            # Check if the new state is valid, ie within the bounds of the city map and not a closed workshop
            if (0 <= new_state[0] < city_map.shape[0] and 0 <= new_state[1] < city_map.shape[1] and
                    city_map[new_state] != 'x'):
                # The cost so far is the sum of the travel times
                new_cost = g + int(city_map[new_state])
                # Check which district the new state is in
                for i, district in enumerate(districts):
                    if district[0] <= new_state[0] <= district[1]:
                        new_visited_districts = visited_districts + [i]
                        break

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, new_visited_districts))
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current state to the goal state
    # The heuristic relaxes the constraint that Ben must visit at least 1 workshop in each district and presumes Ben can move to the goal state directly
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring cell is always greater than or equal to 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal state, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal state from itself is 0.
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
