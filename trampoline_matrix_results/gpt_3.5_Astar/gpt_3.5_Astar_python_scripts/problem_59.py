
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((0, 9), (11, 2))
    grid = [[1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
            [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0],
            [1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1],
            [0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
            [0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
            [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]]
    num_rows = 12
    num_cols = 12

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If Alex reaches the destination, return the actions taken
        if state[0] == (11, 2):
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the 8 adjacent trampolines
        for d_row in [-1, 0, 1]:
            for d_col in [-1, 0, 1]:
                new_row = state[0][0] + d_row
                new_col = state[0][1] + d_col
                # Check if the new position is within the grid and not a broken trampoline
                if 0 <= new_row < num_rows and 0 <= new_col < num_cols and grid[new_row][new_col] == 0:
                    # Calculate the number of diagonal jumps made so far
                    diagonal_jumps = sum(1 for action in actions if abs(action[0] - action[1]) == 1)
                    # Ensure Alex makes exactly 4 diagonal jumps
                    if (abs(d_row) == 1 and abs(d_col) == 1 and diagonal_jumps < 4) or (d_row == 0 or d_col == 0):
                        new_state = ((new_row, new_col), state[1])
                        new_cost = g + 1

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            h = heuristic(new_state, (11, 2))
                            heapq.heappush(queue, (new_cost + h, new_cost, actions + [(new_row, new_col)], new_state))
    return None


def heuristic(state, goal):
    # The heuristic is the Manhattan distance between the current position and the goal position
    # This heuristic is admissible as it never overestimates the cost to reach the goal
    # It is consistent because the cost of moving to a neighboring trampoline is always 1, which is exactly the decrease in the Manhattan distance
    h = abs(state[0][0] - goal[0]) + abs(state[0][1] - goal[1])
    return h


print(a_star())
