
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((8, 2), (1, 8))
    grid = [[0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
            [0, 0, 1, 0, 0, 1, 1, 1, 1, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 1, 0, 1, 1, 0, 0],
            [1, 0, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]]
    num_rows = 10
    num_cols = 10

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If Alex reaches the destination, return the actions taken
        if state[0] == (1, 8):
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the eight adjacent trampolines
        for d_row in [-1, 0, 1]:
            for d_col in [-1, 0, 1]:
                new_row = state[0][0] + d_row
                new_col = state[0][1] + d_col
                # Check if the new position is within the grid and not a broken trampoline
                if 0 <= new_row < num_rows and 0 <= new_col < num_cols and grid[new_row][new_col] == 0:
                    # Calculate the cost of moving to the new position
                    new_cost = g + 1
                    new_state = ((new_row, new_col), state[1])
                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of unvisited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        # Calculate the heuristic cost to reach the destination
                        h = heuristic(new_state)
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [(new_row, new_col)], new_state))
    return None


def heuristic(state):
    # The heuristic function calculates the Manhattan distance between the current position and the destination
    # This heuristic is admissible as it never overestimates the cost to reach the destination
    # It is consistent because the cost of moving to a neighboring position is always 1, which is exactly the decrease in the Manhattan distance
    h = abs(state[0][0] - 1) + abs(state[0][1] - 8)
    return h


print(a_star())
