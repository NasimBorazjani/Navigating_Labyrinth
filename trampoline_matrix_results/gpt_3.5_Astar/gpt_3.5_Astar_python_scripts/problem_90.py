
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((12, 11), (0, 4))
    grid = [[1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
            [0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
            [1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1],
            [0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1],
            [0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0],
            [1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
            [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1]]
    num_rows = 14
    num_cols = 14
    diagonal_jumps = 4

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If Alex has made exactly 4 diagonal jumps and reached the destination, return the actions taken
        if state[0] == (0, 4) and sum(1 for action in actions if action[0] != action[1]) == diagonal_jumps:
            return actions

        # Generate all possible actions from the current state, which includes jumping to any of the 8 adjacent trampolines
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_row = state[0][0] + i
                new_col = state[0][1] + j
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
