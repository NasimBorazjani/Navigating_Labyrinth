
import heapq
import math


def a_star():
    # Define the initial state of the grid and the goal state
    initial_state = [[0, 1, 0, 1, 0, 1, 1, 1, 0],
                      [1, 0, 1, 0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 1, 1, 1, 0, 1, 1],
                      [1, 0, 0, 0, 0, 1, 1, 0, 1],
                      [0, 0, 0, 0, 1, 0, 0, 1, 0],
                      [1, 0, 0, 0, 1, 1, 1, 0, 1],
                      [0, 1, 0, 0, 1, 0, 1, 1, 0],
                      [0, 1, 0, 0, 1, 0, 0, 0, 1],
                      [1, 1, 0, 0, 0, 0, 0, 1, 0]]
    goal_state = (2, 1)
    num_rows = 9
    num_cols = 9

    visited_costs = {}
    visited_costs[(8, 8)] = 0

    queue = [(0, 0, [], (8, 8))]

    while queue:
        _, g, actions, current_pos = heapq.heappop(queue)

        # If Alex reaches the goal state, return the actions taken
        if current_pos == goal_state:
            return actions

        # Generate all possible actions from the current position, which includes moving to any of the eight adjacent trampolines
        for d_row in [-1, 0, 1]:
            for d_col in [-1, 0, 1]:
                new_row = current_pos[0] + d_row
                new_col = current_pos[1] + d_col
                # Check if the new position is within the bounds of the grid and the trampoline is functional
                if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] == 0:
                    # Calculate the Euclidean distance from the new position to the goal position
                    h = math.sqrt((new_row - goal_state[0]) ** 2 + (new_col - goal_state[1]) ** 2)
                    new_cost = g + 1

                    if (new_row, new_col) not in visited_costs or new_cost < visited_costs[(new_row, new_col)]:
                        visited_costs[(new_row, new_col)] = new_cost
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [(new_row, new_col)], (new_row, new_col)))

    return None


print(a_star())
