
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (3, 1)
    goal_state = (5, 8)
    # Define the map of the city
    city_map = np.array([[19, 'x', 17, 14, 3, 'x', 10, 5, 2],
                         ['x', 'x', 1, 'x', 'x', 'x', 19, 7, 1],
                         [16, 12, 'x', 3, 19, 2, 14, 1, 14],
                         ['x', 1, 16, 'x', 12, 3, 13, 'x', 3],
                         ['x', 'x', 7, 19, 10, 'x', 5, 'x', 19],
                         [5, 'x', 'x', 6, 14, 'x', 'x', 10, 12],
                         ['x', 'x', 'x', 'x', 18, 'x', 'x', 15, 12],
                         ['x', 'x', 16, 8, 'x', 3, 4, 'x', 'x'],
                         ['x', 'x', 'x', 16, 'x', 'x', 8, 14, 7]])
    # Define the districts of the city
    districts = [set(), set(), set()]
    for i in range(9):
        for j in range(9):
            if city_map[i][j] != 'x':
                if i < 4:
                    districts[0].add((i, j))
                elif i < 5:
                    districts[1].add((i, j))
                else:
                    districts[2].add((i, j))

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[(initial_state, frozenset([0, 1, 2] if initial_state in districts[0] else [1, 2]))] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, [initial_state], initial_state, frozenset([0, 1, 2] if initial_state in districts[0] else [1, 2]))]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state, districts_left = heapq.heappop(queue)

        # If the current state is the goal state and all districts have been visited, return the path
        if state == goal_state and not districts_left:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the neighboring workshops
        for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = state[0] + d_row, state[1] + d_col
            # Check if the move is valid, ie if the coordinate of the workshop to move to is a valid coordinate within the bounds of the city map and the workshop is not closed
            if 0 <= new_row < 9 and 0 <= new_col < 9 and city_map[new_row][new_col] != 'x':
                # The move is valid, generate the new state
                new_state = (new_row, new_col)
                # The cost so far is the sum of the travel times, as our objective is to minimize the total travel time
                new_cost = g + city_map[new_row][new_col]
                # Update the set of districts left to visit
                new_districts_left = districts_left - {0 if new_state in districts[0] else 1 if new_state in districts[1] else 2}

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if (new_state, new_districts_left) not in visited_costs or new_cost < visited_costs[(new_state, new_districts_left)]:
                    visited_costs[(new_state, new_districts_left)] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [new_state], new_state, new_districts_left))
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current state to the goal state
    # The heuristic relaxes the constraint that Ben can only move to neighboring workshops and presumes he can move directly to the goal workshop
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring workshop is always 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal workshop, otherwise the estimated cost of the successor state is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal workshop from itself would be 0
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
