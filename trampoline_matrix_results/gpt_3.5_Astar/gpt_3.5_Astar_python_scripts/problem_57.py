
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((11, 2), (3, 10))
    num_rows = 12
    num_cols = 12
    grid = [[1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1],
            [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0],
            [0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
            [1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0]]

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If Alex has made exactly 4 diagonal jumps, check if he has reached the destination
        if len(actions) == 4 and state[0] == (3, 10):
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the 8 adjacent trampolines
        for d_row in [-1, 0, 1]:
            for d_col in [-1, 0, 1]:
                new_row = state[0][0] + d_row
                new_col = state[0][1] + d_col
                # Check if the new position is within the grid and the trampoline is functional
                if 0 <= new_row < num_rows and 0 <= new_col < num_cols and grid[new_row][new_col] == 0:
                    new_state = ((new_row, new_col), state[1])
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        # Calculate the heuristic based on the Euclidean distance to the destination
                        h = math.sqrt((new_row - state[1][0]) ** 2 + (new_col - state[1][1]) ** 2)
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [(new_row, new_col)], new_state))
    return None


print(a_star())
