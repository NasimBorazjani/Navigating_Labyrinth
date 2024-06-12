
import heapq
import numpy as np


def a_star():
    # Define the initial state of the puzzle
    initial_state = [[46, 82, 90], [36, 41, 38], [28, 55, '_']]
    goal_state = [[90, 82, 55], [46, 41, 38], [36, 28, '_']]

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state:
            return actions

        # Find the position of the empty spot in the current state
        empty_spot = np.argwhere(np.array(state) == '_')[0]

        # Generate all possible actions from the current state, which includes swapping the empty spot with a neighboring tile
        for d_row, d_col in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_row, new_col = empty_spot[0] + d_row, empty_spot[1] + d_col

            # Check if the new position is within the bounds of the puzzle
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                # Generate the new state by swapping the empty spot with the neighboring tile
                new_state = [list(row) for row in state]
                new_state[empty_spot[0]][empty_spot[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_spot[0]][empty_spot[1]]
                new_state = [[cell for cell in row] for row in new_state]
                new_state_str = str(new_state)

                # Calculate the cost of the new state
                new_cost = g + 1

                if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                    visited_costs[new_state_str] = new_cost
                    # Add the number on the tile that was swapped with the empty spot to the actions list
                    heapq.heappush(queue, (g + 1, new_cost, actions + [state[new_row][new_col]], new_state))

    return None


print(a_star())
