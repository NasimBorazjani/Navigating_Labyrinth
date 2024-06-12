
import numpy as np
from itertools import permutations

def is_valid(grid):
    for row in grid:
        if 'x' in row:
            continue
        if not (row[0] < row[1] < row[2] or row[0] > row[1] > row[2]):
            return False
    for col in grid.T:
        if 'x' in col:
            continue
        if not (col[0] < col[1] < col[2] or col[0] > col[1] > col[2]):
            return False
    return True

def calculate_sum(grid):
    diagonal_sum = np.sum(np.diag(grid))
    top_row_sum = np.sum(grid[0])
    right_col_sum = np.sum(grid[:, 2])
    return diagonal_sum + top_row_sum + right_col_sum

def solve(grid):
    min_sum = float('inf')
    min_perm = None
    for perm in permutations(range(45, 98)):
        new_grid = grid.copy()
        idx = 0
        for i in range(3):
            for j in range(3):
                if new_grid[i, j] == 'x':
                    new_grid[i, j] = perm[idx]
                    idx += 1
        if is_valid(new_grid):
            current_sum = calculate_sum(new_grid)
            if current_sum < min_sum:
                min_sum = current_sum
                min_perm = new_grid
    return min_perm

grid = np.array([['x', '89', '95'],
                 ['x', 'x', '96'],
                 ['74', '93', 'x']])

solution = solve(grid)

result = []
for i in range(3):
    for j in range(3):
        if grid[i, j] == 'x' and solution[i, j] != 'x':
            result.append((i, j, solution[i, j]))

print(result)
