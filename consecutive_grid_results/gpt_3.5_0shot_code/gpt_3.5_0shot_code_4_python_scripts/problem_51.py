
import numpy as np
from itertools import permutations

def check_valid(grid):
    for i in range(4):
        row = grid[i]
        col = grid[:, i]
        if not (all(row[1:] > row[:-1]) or all(row[1:] < row[:-1])):
            return False
        if not (all(col[1:] > col[:-1]) or all(col[1:] < col[:-1])):
            return False
    return True

def calculate_sum(grid):
    diagonal_sum = np.sum(np.diag(grid))
    top_row_sum = np.sum(grid[0])
    right_col_sum = np.sum(grid[:, 3])
    return diagonal_sum + top_row_sum + right_col_sum

def solve(grid):
    x_positions = np.argwhere(grid == 'x')
    numbers = [i for i in range(20, 60) if str(i) not in grid]
    min_sum = float('inf')
    min_perm = None

    for perm in permutations(numbers):
        new_grid = grid.copy()
        for i, (x, num) in enumerate(zip(x_positions, perm)):
            new_grid[x[0], x[1]] = str(num)
        
        if check_valid(new_grid):
            current_sum = calculate_sum(new_grid)
            if current_sum < min_sum:
                min_sum = current_sum
                min_perm = perm

    replacements = [(x[0], x[1], num) for x, num in zip(x_positions, min_perm)]
    return replacements

initial_grid = np.array([['x', '36', 'x', '55'],
                         ['30', '34', 'x', '56'],
                         ['x', '33', 'x', '57'],
                         ['x', '32', '46', 'x']])

replacements = solve(initial_grid)
print(replacements)
