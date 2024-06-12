
import numpy as np
from itertools import permutations

def check_valid(grid):
    for i in range(3):
        row = grid[i]
        col = grid[:, i]
        if not (all(row[0] < row[1] < row[2]) or all(row[0] > row[1] > row[2])):
            return False
        if not (all(col[0] < col[1] < col[2]) or all(col[0] > col[1] > col[2])):
            return False
    return True

def calculate_sum(grid):
    diagonal_sum = grid[0, 0] + grid[1, 1] + grid[2, 2]
    top_row_sum = np.sum(grid[0, :])
    right_col_sum = np.sum(grid[:, 2])
    return diagonal_sum + top_row_sum + right_col_sum

def solve_grid(grid):
    min_sum = float('inf')
    min_perm = None
    for perm in permutations(range(29, 82)):
        perm = np.array(perm).reshape(3, 3)
        temp_grid = np.copy(grid)
        temp_grid[temp_grid == 'x'] = perm[temp_grid == 'x']
        if check_valid(temp_grid):
            temp_sum = calculate_sum(temp_grid)
            if temp_sum < min_sum:
                min_sum = temp_sum
                min_perm = perm
    replacements = []
    for i in range(3):
        for j in range(3):
            if grid[i, j] == 'x':
                replacements.append((i, j, min_perm[i, j]))
    return replacements

grid = np.array([['x', 'x', 'x'],
                 ['39', 'x', '50'],
                 ['32', 'x', '55']])

replacements = solve_grid(grid)
print(replacements)
