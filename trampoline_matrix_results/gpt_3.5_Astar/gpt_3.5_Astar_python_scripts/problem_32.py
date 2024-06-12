
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((0, 9), (9, 2))
    num_rows = 11
    num_cols = 11
    grid = [[1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0],
            [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
            [1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
            [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
            [0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1],
            [0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1]]
    
    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If Alex reaches his destination, return the sequence of trampolines he jumped on
        if state[0] == (9, 2):
            return actions

        # Generate all possible actions from the current state, which includes jumping to any of the eight adjacent trampolines
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_row = state[0][0] + i
                new_col = state[0][1] + j
                # Check if the new position is within the bounds of the grid and the trampoline is functional
                if 0 <= new_row < num_rows and 0 <= new_col < num_cols and grid[new_row][new_col] == 0:
                    # Calculate the distance from the destination using the Manhattan distance heuristic
                    h = abs(new_row - 9) + abs(new_col - 2)
                    new_state = ((new_row, new_col), state[1])
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [(new_row, new_col)], new_state))
    return None


print(a_star())
