
import numpy as np
from itertools import permutations

def is_valid(grid):
    for row in grid:
        if row[0] != 'x' and row[1] != 'x' and row[2] != 'x':
            if not (row[0] < row[1] < row[2] or row[0] > row[1] > row[2]):
                return False
    for col in range(3):
        if grid[0][col] != 'x' and grid[1][col] != 'x' and grid[2][col] != 'x':
            if not (grid[0][col] < grid[1][col] < grid[2][col] or grid[0][col] > grid[1][col] > grid[2][col]):
                return False
    return True

def calculate_sum(grid):
    diagonal_sum = int(grid[0][0]) + int(grid[1][1]) + int(grid[2][2])
    top_row_sum = sum([int(num) for num in grid[0] if num != 'x'])
    right_col_sum = sum([int(num) for num in [row[2] for row in grid] if num != 'x'])
    return diagonal_sum + top_row_sum + right_col_sum

def solve(grid):
    min_sum = float('inf')
    min_perm = None
    for perm in permutations(range(45, 98)):
        temp_grid = np.copy(grid)
        idx = 0
        for i in range(3):
            for j in range(3):
                if temp_grid[i][j] == 'x':
                    temp_grid[i][j] = str(perm[idx])
                    idx += 1
        if is_valid(temp_grid):
            temp_sum = calculate_sum(temp_grid)
            if temp_sum < min_sum:
                min_sum = temp_sum
                min_perm = temp_grid
    result = []
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'x':
                result.append((i, j, int(min_perm[i][j])))
    return result

grid = np.array([['46', '80', '90'],
                 ['51', 'x', 'x'],
                 ['x', 'x', 'x']])

solution = solve(grid)
print(solution)
