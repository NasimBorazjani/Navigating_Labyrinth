
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((11, 3), (1, 10))
    num_rows = 13
    num_cols = 13
    grid = [[1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
            [1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1],
            [1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1],
            [0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
            [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0],
            [1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
            [1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1],
            [1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1])

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If Alex reaches the destination, return the actions taken
        if state[0] == (1, 10):
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the eight adjacent trampolines
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_row = state[0][0] + i
                new_col = state[0][1] + j
                # Check if the new position is within the grid and the trampoline is functional
                if 0 <= new_row < num_rows and 0 <= new_col < num_cols and grid[new_row][new_col] == 0:
                    # Calculate the cost of moving to the new position
                    new_cost = g + math.sqrt(i**2 + j**2)
                    new_state = ((new_row, new_col), state[1])
                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        # Calculate the heuristic cost using the Euclidean distance to the destination
                        h = math.sqrt((new_row - 1)**2 + (new_col - 10)**2)
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [(new_row, new_col)], new_state))
    return None

print(a_star())
