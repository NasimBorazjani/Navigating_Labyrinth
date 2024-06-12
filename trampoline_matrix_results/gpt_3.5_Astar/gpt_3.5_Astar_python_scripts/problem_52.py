
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((8, 1),)
    destination = (1, 11)
    grid = [[1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
            [0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1],
            [0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1],
            [0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
            [0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0],
            [1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0],
            [1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0]]
    num_rows = 12
    num_cols = 12

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If Alex reaches the destination, return the actions taken
        if state[-1] == destination:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the 8 adjacent trampolines
        current_position = state[-1]
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_row = current_position[0] + i
                new_col = current_position[1] + j
                # Check if the new position is within the grid and not broken
                if 0 <= new_row < num_rows and 0 <= new_col < num_cols and grid[new_row][new_col] == 0:
                    # Calculate the number of diagonal jumps made so far
                    diagonal_jumps = sum(1 for pos in state if abs(pos[0] - pos[1]) == 10)
                    # Check if the number of diagonal jumps is exactly 4
                    if diagonal_jumps == 4:
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
    # It is consistent because the cost of moving from one position to an adjacent position is always 1, which is exactly the decrease in the Manhattan distance
    current_position = state[-1]
    return abs(current_position[0] - destination[0]) + abs(current_position[1] - destination[1])


print(a_star())
