
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (1, 0)
    goal_state = (8, 10)
    # Define the map of the city as a 2d numpy array
    city_map = np.array([[3, 14, 2, 'x', 'x', 'x', 19, 13, 17, 12, 8, 'x'],
                         [1, 2, 13, 1, 4, 19, 'x', 'x', 16, 'x', 'x', 12],
                         [9, 8, 9, 15, 'x', 12, 'x', 'x', 'x', 'x', 'x', 14],
                         [11, 1, 10, 18, 'x', 16, 1, 'x', 12, 'x', 'x', 'x'],
                         [7, 16, 13, 10, 13, 'x', 14, 'x', 'x', 9, 'x', 7],
                         [19, 7, 7, 20, 13, 14, 18, 'x', 'x', 7, 5, 'x'],
                         [4, 'x', 11, 'x', 'x', 2, 7, 1, 5, 'x', 'x', 'x'],
                         ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 18, 'x', 1, 'x'],
                         [4, 'x', 'x', 9, 19, 2, 18, 8, 16, 14, 19, 7],
                         ['x', 'x', 'x', 'x', 9, 'x', 17, 17, 1, 2, 2, 15],
                         [18, 'x', 'x', 'x', 'x', 'x', 'x', 11, 10, 'x', 17, 'x'],
                         [9, 'x', 'x', 'x', 10, 3, 'x', 'x', 13, 'x', 2, 'x']])
    # Define the districts of the city
    districts = [(0, 1), (2, 7), (8, 11)]
    num_rows, num_cols = city_map.shape

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [initial_state], initial_state, [1])]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state, visited_districts = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state and len(set(visited_districts)) == len(districts):
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops
        for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            new_row, new_col = state[0] + d_row, state[1] + d_col
            # Check if the move is valid, ie if the coordinate of the workshop to move to is a valid coordinate within the bounds of the city map and the workshop is not closed
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
                # The move is valid, generate the new state
                new_state = (new_row, new_col)
                # The cost so far is the travel time to the new workshop, as our objective is to minimize the total travel time
                new_cost = g + int(city_map[new_row][new_col])

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # Check if the new state is in a new district
                    for i, district in enumerate(districts):
                        if district[0] <= new_row <= district[1]:
                            new_visited_districts = visited_districts + [i + 1]
                            break
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [new_state], new_state, new_visited_districts))
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current state to the goal state
    # The heuristic relaxes the constraint that Ben must visit at least 1 workshop in each district and presumes Ben can move to the goal state directly from the current state
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal state, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal state from itself is 0.
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
