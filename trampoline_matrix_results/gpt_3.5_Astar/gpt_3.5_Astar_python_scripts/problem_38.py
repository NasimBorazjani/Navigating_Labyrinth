
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((8, 8),)
    num_rows = 11
    num_cols = 11
    destination = (0, 0)
    grid = [[0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
            [1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
            [0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
            [1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1],
            [0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1],
            [1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0]]
  
    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If Alex reaches the destination, return the actions taken
        if state[0] == destination:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the eight adjacent trampolines
        for d_row in [-1, 0, 1]:
            for d_col in [-1, 0, 1]:
                # Check if the new state would be valid, ie the new position must be within the bounds of the grid, not broken, and the move must be diagonal
                new_row = state[0][0] + d_row
                new_col = state[0][1] + d_col
                if 0 <= new_row < num_rows and 0 <= new_col < num_cols and grid[new_row][new_col] == 0 and (d_row != 0 and d_col != 0):
                    new_state = ((new_row, new_col),)
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        h = heuristic(new_state, destination)
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state[0]], new_state))
    return None


def heuristic(state, destination):
    # The heuristic function is the Manhattan distance between the current position and the destination
    # This heuristic is admissible because it never overestimates the cost to reach the destination
    # The heuristic is consistent because the cost of moving from one position to an adjacent position is always 1, which is exactly the decrease in the Manhattan distance
    h = abs(state[0][0] - destination[0]) + abs(state[0][1] - destination[1])
    return h


print(a_star())
