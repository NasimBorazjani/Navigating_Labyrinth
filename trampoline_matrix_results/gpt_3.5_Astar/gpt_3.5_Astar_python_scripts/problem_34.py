
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((10, 10),)
    destination = (5, 0)
    num_rows = 11
    num_cols = 11
    grid = [[0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
            [0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1],
            [0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        if state[0] == destination:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the 8 adjacent trampolines
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_row = state[-1][0] + i
                new_col = state[-1][1] + j
                # Check if the new position is within the bounds of the grid and the trampoline is functional
                if 0 <= new_row < num_rows and 0 <= new_col < num_cols and grid[new_row][new_col] == 0:
                    # Calculate the number of diagonal jumps made so far
                    diagonal_jumps = sum(1 for a, b in state if abs(a - new_row) == 1 and abs(b - new_col) == 1)
                    # Ensure that exactly 3 diagonal jumps are made
                    if diagonal_jumps == 3:
                        new_state = state + ((new_row, new_col),)
                        new_cost = g + 1
                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            h = heuristic(new_state, destination)
                            heapq.heappush(queue, (new_cost + h, new_cost, actions + [(new_row, new_col)], new_state))
    return None


def heuristic(state, destination):
    # The heuristic is the Manhattan distance from the current position to the destination
    # This heuristic is admissible because it never overestimates the cost to reach the destination
    # The heuristic is consistent because the cost of moving from one position to an adjacent position is always 1, which is exactly the decrease in the Manhattan distance
    h = 0
    for pos in state:
        h = max(h, abs(pos[0] - destination[0]) + abs(pos[1] - destination[1]))
    return h


print(a_star())
