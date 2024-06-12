
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((8, 1),)
    destination = (0, 5)
    num_rows = 9
    num_cols = 9
    grid = [[0, 0, 1, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 0, 1, 1, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 0, 0, 1, 0, 1],
            [0, 1, 0, 0, 0, 1, 1, 0, 1],
            [0, 0, 1, 0, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 1, 0, 0, 1, 1]]

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        if state[0] == destination:
            return actions

        # Generate all possible actions from the current state, which includes jumping to any of the eight adjacent trampolines
        for d_row in [-1, 0, 1]:
            for d_col in [-1, 0, 1]:
                new_row = state[-1][0] + d_row
                new_col = state[-1][1] + d_col
                # Check if the new position is within the bounds of the grid and the trampoline is functional
                if 0 <= new_row < num_rows and 0 <= new_col < num_cols and grid[new_row][new_col] == 0:
                    # Calculate the number of diagonal jumps made so far
                    num_diagonal_jumps = sum(1 for i in range(len(state) - 1) if abs(state[i][0] - state[i + 1][0]) == 1 and abs(state[i][1] - state[i + 1][1]) == 1)
                    # Check if the number of diagonal jumps is less than 3
                    if num_diagonal_jumps < 3:
                        new_state = state + ((new_row, new_col),)
                        new_cost = g + 1
                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            h = heuristic(new_state, destination)
                            heapq.heappush(queue, (new_cost + h, new_cost, actions + [(new_row, new_col)], new_state))
    return None


def heuristic(state, destination):
    # The heuristic is the Manhattan distance from the current position to the destination
    # This heuristic is admissible because it never overestimates the cost to reach the goal
    # It is consistent because the cost of moving from one position to another is always 1, which is exactly the decrease in the heuristic estimate
    h = 0
    for pos in state:
        h += abs(pos[0] - destination[0]) + abs(pos[1] - destination[1])
    return h


print(a_star())
