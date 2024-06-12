
import heapq
import numpy as np


def a_star():
    # Define the initial grid state
    grid = np.array([['x', 'x', 23],
                     [31, 'x', 'x'],
                     ['x', 42, 51]])

    # Define the range of numbers that can replace 'x' in the grid
    numbers = set(range(18, 57))

    visited_costs = {}
    visited_costs[tuple(map(tuple, grid))] = 0

    queue = []
    heappush(queue, (0, 0, [], grid))

    while queue:
        _, g, actions, state = heappop(queue)

        # Unpack the state to access the grid and the set of available numbers
        grid_state = np.array(state)
        available_numbers = numbers - set(grid_state.flatten())

        # If there are no more unknown numbers in the grid, return the actions taken
        if 'x' not in grid_state:
            return actions

        # Generate all possible actions from the current state
        for i in range(3):
            for j in range(3):
                if grid_state[i][j] == 'x':
                    for num in available_numbers:
                        new_grid = grid_state.copy()
                        new_grid[i][j] = num
                        new_cost = g + calculate_cost(new_grid)

                        new_state = tuple(map(tuple, new_grid))

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            new_available_numbers = available_numbers - {num}
                            heappush(queue, (new_cost + heuristic(new_grid, new_available_numbers), new_cost, actions + [(i, j, num)], new_grid))

    return None


def heuristic(grid, available_numbers):
    # Calculate the sum of the numbers in the top row, rightmost column, and diagonal
    top_row_sum = np.sum(grid[0][grid[0] != 'x'])
    right_col_sum = np.sum(grid[:, 2][grid[:, 2] != 'x'])
    diagonal_sum = np.sum(np.diag(grid))

    # Calculate the sum of the numbers in the diagonal connecting the top-left corner to the bottom-right corner
    diag_sum = grid[0][0] + grid[1][1] + grid[2][2]

    # Calculate the heuristic value as the sum of the top row, rightmost column, and diagonal sums
    h = top_row_sum + right_col_sum + diagonal_sum

    return h


def calculate_cost(grid):
    # Calculate the sum of the numbers in the top row, rightmost column, and diagonal
    top_row_sum = np.sum(grid[0][grid[0] != 'x'])
    right_col_sum = np.sum(grid[:, 2][grid[:, 2] != 'x'])
    diagonal_sum = np.sum(np.diag(grid))

    # Calculate the cost as the sum of the top row, rightmost column, and diagonal sums
    cost = top_row_sum + right_col_sum + diagonal_sum

    return cost


print(a_star())
