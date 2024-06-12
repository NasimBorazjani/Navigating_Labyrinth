
import numpy as np
from itertools import permutations

def is_valid(grid):
    for row in grid:
        if 'x' not in row:
            if not (row[0] > row[1] > row[2] or row[0] < row[1] < row[2]):
                return False
    for col in grid.T:
        if 'x' not in col:
            if not (col[0] > col[1] > col[2] or col[0] < col[1] < col[2]):
                return False
    return True

def calculate_sum(grid):
    diagonal_sum = grid[0, 0] + grid[1, 1] + grid[2, 2]
    top_row_sum = np.sum(grid[0, :])
    right_col_sum = np.sum(grid[:, 2])
    return diagonal_sum + top_row_sum + right_col_sum

def solve(grid):
    min_sum = float('inf')
    min_perm = None
    for perm in permutations(range(19, 52), 6):
        perm = np.array(perm).reshape(3, 2)
        temp_grid = grid.copy()
        temp_grid[temp_grid == 'x'] = perm[:, 0]
        if is_valid(temp_grid):
            temp_sum = calculate_sum(temp_grid)
            if temp_sum < min_sum:
                min_sum = temp_sum
                min_perm = perm
    result = []
    for i in range(3):
        for j in range(2):
            if grid[i, j] == 'x':
                result.append((i, j, min_perm[i, j]))
    return result

grid = np.array([['x', 'x', 'x'],
                 ['x', '36', '44'],
                 ['x', '34', 'x']])

solution = solve(grid)
print(solution)
