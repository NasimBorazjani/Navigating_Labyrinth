
import numpy as np
from itertools import permutations

def is_valid(grid):
    for row in grid:
        if 'x' in row:
            continue
        if row[0] < row[1] < row[2] or row[0] > row[1] > row[2]:
            continue
        return False
    for col in grid.T:
        if 'x' in col:
            continue
        if col[0] < col[1] < col[2] or col[0] > col[1] > col[2]:
            continue
        return False
    return True

def calculate_sum(grid):
    diagonal_sum = np.trace(grid)
    top_row_sum = np.sum(grid[0])
    right_col_sum = np.sum(grid[:, 2])
    return diagonal_sum + top_row_sum + right_col_sum

def solve(grid):
    min_sum = float('inf')
    min_perm = None
    for perm in permutations(range(48, 101), 6):
        temp_grid = grid.copy()
        idx = 0
        for i in range(3):
            for j in range(3):
                if temp_grid[i, j] == 'x':
                    temp_grid[i, j] = perm[idx]
                    idx += 1
        if is_valid(temp_grid):
            current_sum = calculate_sum(temp_grid)
            if current_sum < min_sum:
                min_sum = current_sum
                min_perm = temp_grid
    result = []
    for i in range(3):
        for j in range(3):
            if grid[i, j] == 'x':
                result.append((i, j, min_perm[i, j]))
    return result

grid = np.array([['57', 'x', '86'],
                 ['x', '75', 'x'],
                 ['x', '76', '90']])

result = solve(grid)
print(result)
