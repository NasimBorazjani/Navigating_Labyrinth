
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (6, 12)
    goal_state = (4, 1)
    # Define the map of the city as a 2d numpy array
    city_map = np.array([[np.inf, 12, np.inf, np.inf, np.inf, 5, 9, 14, 6, np.inf, 3, 14, np.inf],
                         [np.inf, np.inf, 3, np.inf, 11, np.inf, 13, np.inf, np.inf, np.inf, np.inf, 9, 8],
                         [np.inf, 18, np.inf, np.inf, np.inf, 13, 4, 5, np.inf, np.inf, np.inf, 13, np.inf],
                         [10, 4, np.inf, np.inf, np.inf, np.inf, np.inf, 18, np.inf, 15, np.inf, np.inf, np.inf],
                         [np.inf, 1, 7, np.inf, 7, 6, np.inf, 3, np.inf, 2, np.inf, np.inf, 5],
                         [np.inf, 15, 5, np.inf, np.inf, 10, np.inf, 19, np.inf, np.inf, np.inf, 10, 6],
                         [np.inf, 18, 1, 2, np.inf, 7, 16, 19, np.inf, np.inf, 10, 8, 8],
                         [8, np.inf, np.inf, 6, 2, np.inf, np.inf, np.inf, 7, 11, 5, 11, 2],
                         [np.inf, 4, 1, 1, 5, 12, 3, 6, 2, 1, np.inf, 3, 8],
                         [np.inf, np.inf, 5, 5, 14, 15, 7, np.inf, np.inf, 11, np.inf, 7, 9],
                         [np.inf, 6, 12, 16, 17, np.inf, np.inf, 4, np.inf, 19, 9, 5, np.inf],
                         [12, np.inf, 4, np.inf, 8, 4, np.inf, 5, np.inf, np.inf, np.inf, 5, np.inf],
                         [np.inf, 5, np.inf, np.inf, np.inf, np.inf, np.inf, 7, np.inf, np.inf, 11, np.inf, np.inf]])
    num_rows, num_cols = city_map.shape
    # Define the districts of the city
    districts = [set(range(0, 5)), set(range(5, 6)), set(range(6, 13))]

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], initial_state, set())]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state, visited_districts = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state and len(visited_districts) == len(districts):
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring cells
        for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            new_row, new_col = state[0] + d_row, state[1] + d_col
            # Check if the new state is valid, ie if the new cell is within the bounds of the city map and is not a closed workshop
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != np.inf:
                # Generate the new state
                new_state = (new_row, new_col)
                # The cost so far is the sum of the travel times, as the task is to minimize the total travel time
                new_cost = g + city_map[new_row][new_col]
                # Update the set of visited districts
                new_visited_districts = visited_districts.copy()
                for i, district in enumerate(districts):
                    if new_row in district:
                        new_visited_districts.add(i)

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, new_visited_districts))
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current state to the goal state
    # The heuristic relaxes the constraint that Ben can't move through closed workshops and presumes Ben can move directly to the goal state
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring cell is always 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal state, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal state from itself would be 0.
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
