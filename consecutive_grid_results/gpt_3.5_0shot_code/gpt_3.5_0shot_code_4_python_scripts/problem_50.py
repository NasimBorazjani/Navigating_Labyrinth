
import numpy as np
from itertools import permutations

def is_valid(grid):
    for row in grid:
        if 'x' in row:
            continue
        if not all(row[i] < row[i+1] for i in range(len(row)-1)) and not all(row[i] > row[i+1] for i in range(len(row)-1)):
            return False
    for col in grid.T:
        if 'x' in col:
            continue
        if not all(col[i] < col[i+1] for i in range(len(col)-1)) and not all(col[i] > col[i+1] for i in range(len(col)-1)):
            return False
    return True

def calculate_sum(grid):
    diagonal_sum = np.trace(grid)
    top_row_sum = np.sum(grid[0])
    right_col_sum = np.sum(grid[:,-1])
    return diagonal_sum + top_row_sum + right_col_sum

def solve(grid):
    x_positions = np.argwhere(grid == 'x')
    numbers = [i for i in range(36, 76)]
    min_sum = float('inf')
    min_grid = None

    for perm in permutations(numbers, len(x_positions)):
        new_grid = grid.copy()
        for i, (x, y) in enumerate(x_positions):
            new_grid[x, y] = perm[i]
        if is_valid(new_grid):
            current_sum = calculate_sum(new_grid)
            if current_sum < min_sum:
                min_sum = current_sum
                min_grid = new_grid

    replacements = []
    for i, (x, y) in enumerate(x_positions):
        replacements.append((x, y, min_grid[x, y]))

    return replacements

initial_grid = np.array([['x', 'x', 'x', '60'],
                         ['47', 'x', '62', '65'],
                         ['x', '58', '67', '68'],
                         ['54', 'x', '74', 'x']])

replacements = solve(initial_grid)
print(replacements)
