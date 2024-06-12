
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((0, 9), (10, 0))
    num_rows = 12
    num_cols = 12
    grid = [[1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
            [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1],
            [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
            [0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
            [1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0],
            [1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0]]

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If Alex reaches the destination, return the sequence of trampolines he jumped on
        if state == ((10, 0), (10, 0)):
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the 8 adjacent trampolines
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_row = state[1][0] + i
                new_col = state[1][1] + j
                # Check if the new position is within the grid and the trampoline is functional
                if 0 <= new_row < num_rows and 0 <= new_col < num_cols and grid[new_row][new_col] == 0:
                    # Calculate the number of diagonal jumps made so far
                    diagonal_jumps = sum(1 for a, b in actions if abs(a[0] - b[0]) == 1 and abs(a[1] - b[1]) == 1)
                    # Ensure Alex makes exactly 4 diagonal jumps
                    if abs(i) == 1 and abs(j) == 1 and diagonal_jumps < 4:
                        new_state = (state[1], (new_row, new_col))
                        new_cost = g + 1

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            # Calculate the heuristic based on the Manhattan distance to the destination
                            h = abs(new_row - 10) + abs(new_col - 0)
                            heapq.heappush(queue, (new_cost + h, new_cost, actions + [(state[1], (new_row, new_col))], new_state))

    return None


print(a_star())
