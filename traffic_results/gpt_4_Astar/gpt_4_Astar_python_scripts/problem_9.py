
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (1, 8)
    goal_state = (4, 0)
    # Define the districts in the city
    districts = [(0, 1), (2, 4), (5, 8)]
    # Define the map of the city
    city_map = np.array([[6, 9, 19, 'x', 5, 9, 'x', 15, 'x'],
                         [8, 10, 16, 'x', 'x', 'x', 5, 11, 4],
                         [5, 11, 20, 1, 14, 16, 7, 1, 5],
                         [10, 5, 3, 5, 12, 8, 'x', 'x', 2],
                         [16, 15, 15, 14, 'x', 13, 10, 'x', 10],
                         [6, 4, 7, 13, 'x', 'x', 'x', 'x', 13],
                         ['x', 1, 6, 3, 'x', 'x', 17, 9, 5],
                         ['x', 11, 'x', 9, 'x', 5, 7, 'x', 'x'],
                         ['x', 'x', 'x', 18, 'x', 2, 'x', 'x', 12]])
    num_rows, num_cols = city_map.shape

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the path to get to each state in a list; the path to reach the initial state is just the initial state itself
    queue = [(0, 0, [initial_state], initial_state, [1])]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state, visited_districts = heapq.heappop(queue)

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state == goal_state and len(set(visited_districts)) == len(districts):
            return path

        # Generate all valid actions from the current state, which includes moving to any of the neighboring workshops
        # Generate the coordinates of the workshops neighboring the current workshop
        for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            new_row, new_col = state[0] + d_row, state[1] + d_col
            # Check if the move is valid, ie if the coordinate of the workshop to be moved to is a valid coordinate within the bounds of the city map and is not a closed workshop
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
                # The move is valid, generate the new state
                new_state = (new_row, new_col)
                # The cost so far is the travel time from the current workshop to the new workshop, as our objective is to minimize the total travel time
                new_cost = g + city_map[new_row][new_col]
                # Check which district the new workshop is in
                for i, district in enumerate(districts):
                    if district[0] <= new_row <= district[1]:
                        new_district = i + 1
                        break

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, path + [new_state], new_state, visited_districts + [new_district]))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current workshop to the goal workshop
    # The heuristic relaxes the constraint that Ben can only move to neighboring workshops and presumes Ben can move directly to the goal workshop
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring workshop is always 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal workshop, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal workshop from itself would be 0.
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
