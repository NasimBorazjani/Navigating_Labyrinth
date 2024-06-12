
import numpy as np
from itertools import permutations

def is_valid(grid):
    for row in grid:
        if 'x' not in row:
            if not all(row[i] < row[i+1] or row[i] > row[i+1] for i in range(len(row)-1)):
                return False
    for col in grid.T:
        if 'x' not in col:
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
    numbers = [num for num in range(40, 80) if num not in grid]
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

initial_grid = np.array([['x', 'x', '63', 'x'],
                         ['x', '53', '57', '73'],
                         ['x', 'x', '56', 'x'],
                         ['42', 'x', 'x', '68']])

solution = solve(initial_grid)
print(solution)
