
import heapq
import numpy as np


def a_star():
    # Define the initial state of the puzzle
    initial_state = [[94, 92, 77, 88, '_'], [82, 43, 76, 85, 87], [24, 66, 17, 79, 75]]
    goal_state = [[94, 92, 87, 85, 79], [88, 82, 77, 76, 75], [66, 43, 24, 17, '_']]
    num_rows = 3
    num_cols = 5

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state:
            return actions

        # Find the position of the empty spot in the current state
        empty_spot = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == '_'][0]

        # Generate all possible actions from the current state, which includes swapping the empty spot with a neighboring tile
        for d_row, d_col in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_row, new_col = empty_spot[0] + d_row, empty_spot[1] + d_col

            # Check if the new position is within the bounds of the puzzle
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                # Create a new state by swapping the empty spot with the neighboring tile
                new_state = [list(row) for row in state]
                new_state[empty_spot[0]][empty_spot[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_spot[0]][empty_spot[1]]
                new_state_str = str(new_state)
                # The cost of the new state is the value of the tile swapped with the empty spot
                new_cost = g + new_state[new_row][new_col]

                if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                    visited_costs[new_state_str] = new_cost
                    heapq.heappush(queue, (g + 1, new_cost, actions + [new_state[new_row][new_col]], new_state))

    return None


print(a_star())
