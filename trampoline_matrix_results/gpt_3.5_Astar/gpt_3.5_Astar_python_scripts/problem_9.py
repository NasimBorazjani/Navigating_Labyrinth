
import heapq
import math


def a_star():
    # Define the initial state of the grid and the goal position
    initial_state = ((1, 2),)
    goal_state = (8, 8)
    grid = [[1, 0, 1, 1, 1, 0, 1, 1, 1],
            [0, 1, 0, 0, 1, 1, 1, 0, 0],
            [1, 0, 1, 0, 1, 1, 1, 0, 0],
            [1, 1, 1, 0, 0, 0, 1, 1, 0],
            [1, 1, 0, 1, 0, 1, 0, 1, 1],
            [1, 0, 1, 1, 0, 1, 1, 1, 0],
            [0, 1, 0, 0, 0, 1, 1, 0, 0],
            [0, 1, 0, 0, 0, 1, 0, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0]]
    num_rows = 9
    num_cols = 9

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If Alex reaches the goal position, return the sequence of trampolines he jumped on
        if state[-1] == goal_state and len([pos for pos in state if pos[0] != pos[1]]) == 3:
            return actions

        # Generate all possible actions from the current state, which includes jumping to any of the eight adjacent trampolines
        for d_row in [-1, 0, 1]:
            for d_col in [-1, 0, 1]:
                new_row = state[-1][0] + d_row
                new_col = state[-1][1] + d_col
                # Check if the new position is within the bounds of the grid and the trampoline is functional
                if 0 <= new_row < num_rows and 0 <= new_col < num_cols and grid[new_row][new_col] == 0:
                    new_state = state + ((new_row, new_col),)
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        # Calculate the heuristic based on the Euclidean distance to the goal position
                        h = math.sqrt((new_row - goal_state[0]) ** 2 + (new_col - goal_state[1]) ** 2)
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [(new_row, new_col)], new_state))
    return None


print(a_star())
