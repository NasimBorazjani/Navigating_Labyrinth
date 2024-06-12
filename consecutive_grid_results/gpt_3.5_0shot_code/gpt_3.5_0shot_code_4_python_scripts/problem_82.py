
import numpy as np
from itertools import permutations

def check_valid(grid):
    for i in range(4):
        row = grid[i]
        col = grid[:, i]
        if not (all(row[:-1] < row[1:]) or all(row[:-1] > row[1:]) or all(col[:-1] < col[1:]) or all(col[:-1] > col[1:])):
            return False
    return True

def calculate_sum(grid):
    diagonal_sum = np.sum(np.diag(grid))
    top_row_sum = np.sum(grid[0])
    right_col_sum = np.sum(grid[:, -1])
    return diagonal_sum + top_row_sum + right_col_sum

def solve(grid):
    x_positions = np.argwhere(grid == 'x')
    numbers = [str(i) for i in range(14, 64)]
    perms = permutations(numbers, len(x_positions))

    min_sum = float('inf')
    min_grid = None

    for perm in perms:
        temp_grid = np.copy(grid)
        for i, (x, y) in enumerate(x_positions):
            temp_grid[x, y] = perm[i]

        if check_valid(temp_grid):
            temp_sum = calculate_sum(temp_grid)
            if temp_sum < min_sum:
                min_sum = temp_sum
                min_grid = temp_grid

    replacements = []
    for i, (x, y) in enumerate(x_positions):
        replacements.append((x, y, int(min_grid[x, y])))

    return replacements

initial_grid = np.array([['20', '21', '33', '60'],
                          ['x', 'x', 'x', '49'],
                          ['x', '38', 'x', 'x'],
                          ['36', 'x', '46', 'x']])

replacements = solve(initial_grid)
print(replacements)
