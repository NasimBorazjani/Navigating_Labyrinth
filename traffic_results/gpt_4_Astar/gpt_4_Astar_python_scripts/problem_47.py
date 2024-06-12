
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (4, 11)
    goal_state = (6, 0)
    # Define the map of the city
    city_map = np.array([[5, 'x', 'x', 4, 'x', 12, 7, 11, 8, 3, 19, 'x'],
                         ['x', 'x', 6, 15, 16, 'x', 'x', 4, 'x', 7, 8, 19],
                         [18, 'x', 'x', 15, 'x', 'x', 'x', 8, 4, 16, 7, 9],
                         ['x', 19, 'x', 'x', 'x', 16, 'x', 'x', 17, 15, 'x', 9],
                         [15, 8, 19, 'x', 4, 4, 'x', 'x', 'x', 3, 3, 10],
                         [18, 6, 14, 5, 'x', 18, 19, 15, 18, 19, 12, 5],
                         [12, 'x', 2, 2, 6, 3, 3, 8, 3, 1, 'x', 15],
                         [10, 4, 'x', 9, 15, 3, 'x', 7, 'x', 17, 'x', 'x'],
                         [5, 18, 'x', 17, 'x', 17, 'x', 'x', 15, 'x', 18, 'x'],
                         [4, 'x', 16, 11, 10, 3, 12, 'x', 11, 14, 3, 'x'],
                         ['x', 9, 9, 14, 19, 15, 'x', 1, 10, 19, 6, 'x'],
                         ['x', 'x', 17, 4, 'x', 2, 'x', 7, 'x', 4, 4, 18]])
    num_rows, num_cols = city_map.shape
    # Define the districts
    districts = [set(), set(), set()]
    for i in range(num_rows):
        for j in range(num_cols):
            if city_map[i, j] != 'x':
                if i < 5:
                    districts[0].add((i, j))
                elif i == 5:
                    districts[1].add((i, j))
                else:
                    districts[2].add((i, j))

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[(initial_state, frozenset())] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], (initial_state, frozenset()))]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, (state, visited_districts) = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state and len(visited_districts) == 3:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops
        for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = state[0] + d_row, state[1] + d_col
            # Check if the move is valid, ie if the coordinate of the workshop to move to is a valid coordinate within the bounds of the city map and the workshop is not closed
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row, new_col] != 'x':
                # The move is valid, generate the new state
                new_state = (new_row, new_col)
                # The cost so far is the sum of the travel times, as our objective is to minimize the total travel time
                new_cost = g + city_map[new_row, new_col]
                # Update the visited districts
                new_visited_districts = set(visited_districts)
                for i, district in enumerate(districts):
                    if new_state in district:
                        new_visited_districts.add(i)

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if (new_state, frozenset(new_visited_districts)) not in visited_costs or new_cost < visited_costs[(new_state, frozenset(new_visited_districts))]:
                    visited_costs[(new_state, frozenset(new_visited_districts))] = new_cost
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state], (new_state, frozenset(new_visited_districts))))
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current state to the goal state
    # The heuristic relaxes the constraint that Ben can only move to a neighboring workshop and presumes Ben can move directly to the goal workshop
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring workshop is always greater than or equal to 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal workshop, otherwise the estimated cost of the successor state is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal workshop from itself would be 0.
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
