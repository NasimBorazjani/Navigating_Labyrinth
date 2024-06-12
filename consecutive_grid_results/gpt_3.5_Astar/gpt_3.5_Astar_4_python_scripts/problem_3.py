
import heapq
import numpy as np


def a_star():
    # Define the initial state of the grid
    grid = np.array([[22, 'x', 48], [27, 'x', 'x'], ['x', 42, 52]])
    num_rows, num_cols = grid.shape
    available_numbers = set(range(20, 54))

    visited_costs = {}
    visited_costs[tuple(map(tuple, grid))] = 0

    queue = []
    heappush(queue, (0, 0, [], grid, available_numbers))

    while queue:
        _, g, actions, state, available_nums = heappop(queue)

        # Unpack the state
        state = np.array(state)

        # If there are no more unknown numbers in the grid, return the actions taken
        if 'x' not in state:
            return actions

        # Generate all possible actions from the current state
        for i in range(num_rows):
            for j in range(num_cols):
                if state[i][j] == 'x':
                    for num in available_nums:
                        new_state = state.copy()
                        new_state[i][j] = num
                        new_available_nums = available_nums.copy()
                        new_available_nums.remove(num)
                        new_cost = g + heuristic(new_state, num)

                        if tuple(map(tuple, new_state)) not in visited_costs or new_cost < visited_costs[tuple(map(tuple, new_state))]:
                            visited_costs[tuple(map(tuple, new_state))] = new_cost
                            heappush(queue, (new_cost + heuristic(new_state, num), new_cost, actions + [(i, j, num)], new_state, new_available_nums))

    return None


def heuristic(state, num):
    # Calculate the sum of the numbers in the top row, rightmost column, and diagonal
    top_row_sum = np.sum(state[0][state[0] != 'x'])
    right_col_sum = np.sum(state[state[:, -1] != 'x', -1])
    diagonal_sum = np.trace(state)

    # Calculate the sum of the numbers in the top row, rightmost column, and diagonal after replacing the 'x' with the new number
    top_row_sum += num if 'x' in state[0] else 0
    right_col_sum += num if 'x' in state[:, -1] else 0
    diagonal_sum += num if 'x' in np.diag(state) else 0

    # Return the sum of the three sums as the heuristic value
    return top_row_sum + right_col_sum + diagonal_sum


print(a_star())
