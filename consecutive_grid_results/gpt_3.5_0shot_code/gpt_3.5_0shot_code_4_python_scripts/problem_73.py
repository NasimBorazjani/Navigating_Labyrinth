
import numpy as np
from itertools import permutations

def is_valid(grid):
    for row in grid:
        if 'x' in row:
            continue
        if not all(row[i] < row[i+1] or row[i] > row[i+1] for i in range(len(row)-1)):
            return False
    for col in grid.T:
        if 'x' in col:
            continue
        if not all(col[i] < col[i+1] or col[i] > col[i+1] for i in range(len(col)-1)):
            return False
    return True

def calculate_sum(grid):
    diagonal_sum = sum(grid[i][i] for i in range(4))
    top_row_sum = sum(grid[0])
    right_col_sum = sum(grid[:,3])
    return diagonal_sum + top_row_sum + right_col_sum

def solve(grid):
    x_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [val for val in range(22, 67) if val not in grid]
    min_sum = float('inf')
    min_grid = None

    for perm in permutations(possible_values):
        new_grid = grid.copy()
        for (i, j), val in zip(x_positions, perm):
            new_grid[i][j] = val
        if is_valid(new_grid):
            current_sum = calculate_sum(new_grid)
            if current_sum < min_sum:
                min_sum = current_sum
                min_grid = new_grid

    replacements = [(i, j, min_grid[i][j]) for i, j in x_positions]
    return replacements

initial_grid = np.array([[22, 'x', 'x', 66],
                          ['x', 'x', 'x', 'x'],
                          [50, 52, 'x', 57],
                          ['x', 55, 'x', 'x']])

replacements = solve(initial_grid)
print(replacements)
