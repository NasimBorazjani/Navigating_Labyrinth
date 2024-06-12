
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
    diagonal_sum = sum(grid[i][i] for i in range(len(grid)))
    top_row_sum = sum(grid[0])
    right_col_sum = sum(grid.T[-1])
    return diagonal_sum + top_row_sum + right_col_sum

def solve(grid):
    x_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    numbers = [num for num in range(39, 94) if num not in grid]
    min_sum = float('inf')
    min_permutation = None

    for perm in permutations(numbers):
        new_grid = grid.copy()
        for (i, j), num in zip(x_positions, perm):
            new_grid[i][j] = num
        if is_valid(new_grid):
            current_sum = calculate_sum(new_grid)
            if current_sum < min_sum:
                min_sum = current_sum
                min_permutation = [(i, j, num) for (i, j), num in zip(x_positions, perm)]

    return min_permutation

grid = np.array([[71, 'x', 57, 'x'],
                 [67, 68, 'x', 73],
                 [51, 'x', 72, 'x'],
                 [50, 'x', 75, 'x']])

solution = solve(grid)
print(solution)