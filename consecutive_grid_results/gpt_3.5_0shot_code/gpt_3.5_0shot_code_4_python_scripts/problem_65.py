
import numpy as np
from itertools import permutations

def is_valid(grid):
    for row in grid:
        if 'x' in row:
            continue
        if any(row[i] >= row[i+1] for i in range(len(row)-1)) and any(row[i] <= row[i+1] for i in range(len(row)-1)):
            return False
    for col in grid.T:
        if 'x' in col:
            continue
        if any(col[i] >= col[i+1] for i in range(len(col)-1)) and any(col[i] <= col[i+1] for i in range(len(col)-1)):
            return False
    return True

def calculate_sum(grid):
    diagonal_sum = np.sum([grid[i][i] for i in range(4)])
    top_row_sum = np.sum(grid[0])
    right_col_sum = np.sum(grid[:,3])
    return diagonal_sum + top_row_sum + right_col_sum

def solve(grid):
    min_sum = float('inf')
    min_perm = None
    for perm in permutations(range(31, 76), 12):
        temp_grid = grid.copy()
        idx = 0
        for i in range(4):
            for j in range(4):
                if temp_grid[i][j] == 'x':
                    temp_grid[i][j] = perm[idx]
                    idx += 1
        if is_valid(temp_grid):
            current_sum = calculate_sum(temp_grid)
            if current_sum < min_sum:
                min_sum = current_sum
                min_perm = temp_grid
    result = []
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 'x':
                result.append((i, j, min_perm[i][j]))
    return result

grid = np.array([['x', '68', '71', 'x'],
                 ['x', 'x', '62', 'x'],
                 ['43', 'x', '55', 'x'],
                 ['44', '45', '52', '58']])

solution = solve(grid)
print(solution)
