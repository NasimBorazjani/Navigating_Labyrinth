
import numpy as np
from itertools import permutations

def is_valid(grid):
    for i in range(4):
        row = grid[i]
        col = grid[:, i]
        if not (all(row[1:] > row[:-1]) or all(row[1:] < row[:-1])):
            return False
        if not (all(col[1:] > col[:-1]) or all(col[1:] < col[:-1])):
            return False
    return True

def calculate_sum(grid):
    diagonal_sum = np.trace(grid)
    top_row_sum = np.sum(grid[0])
    right_col_sum = np.sum(grid[:, 3])
    return diagonal_sum + top_row_sum + right_col_sum

def solve(grid):
    x_positions = np.argwhere(grid == 'x')
    numbers = [str(i) for i in range(42, 82)]
    perms = permutations(numbers, len(x_positions))

    min_sum = float('inf')
    best_solution = None

    for perm in perms:
        temp_grid = np.copy(grid)
        for i, (x, y) in enumerate(x_positions):
            temp_grid[x, y] = perm[i]

        if is_valid(temp_grid):
            current_sum = calculate_sum(temp_grid)
            if current_sum < min_sum:
                min_sum = current_sum
                best_solution = temp_grid

    replacements = []
    for i, (x, y) in enumerate(x_positions):
        replacements.append((x, y, int(best_solution[x, y])))

    return replacements

initial_grid = np.array([['79', 'x', 'x', 'x'],
                          ['x', 'x', '65', 'x'],
                          ['56', '60', 'x', 'x'],
                          ['48', '54', 'x', 'x']])

solution = solve(initial_grid)
print(solution)
