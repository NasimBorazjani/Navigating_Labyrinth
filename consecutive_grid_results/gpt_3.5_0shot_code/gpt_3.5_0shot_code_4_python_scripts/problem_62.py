
import numpy as np
from itertools import permutations

def check_valid(grid):
    for i in range(4):
        row = grid[i]
        col = grid[:, i]
        if not (all(row[:-1] < row[1:]) or all(row[:-1] > row[1:])):
            return False
        if not (all(col[:-1] < col[1:]) or all(col[:-1] > col[1:])):
            return False
    return True

def calculate_sum(grid):
    diagonal_sum = np.trace(grid)
    top_row_sum = np.sum(grid[0])
    right_col_sum = np.sum(grid[:, -1])
    return diagonal_sum + top_row_sum + right_col_sum

def solve(grid):
    x_positions = np.argwhere(grid == 'x')
    numbers = [str(i) for i in range(41, 86)]
    min_sum = float('inf')
    best_solution = None

    for perm in permutations(numbers, len(x_positions)):
        new_grid = grid.copy()
        for i, (x, num) in enumerate(zip(x_positions, perm)):
            new_grid[tuple(x)] = num
        if check_valid(new_grid):
            current_sum = calculate_sum(new_grid)
            if current_sum < min_sum:
                min_sum = current_sum
                best_solution = list(zip(x_positions, perm))

    return best_solution

initial_grid = np.array([['69', '70', 'x', 'x'],
                         ['64', '66', 'x', '75'],
                         ['62', '64', 'x', 'x'],
                         ['60', 'x', '48', '46']])

solution = solve(initial_grid)
print(solution)
