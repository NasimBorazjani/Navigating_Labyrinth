
import numpy as np
from itertools import permutations

def is_valid(grid):
    for row in grid:
        if 'x' not in row:
            if not (row[0] < row[1] < row[2] or row[0] > row[1] > row[2]):
                return False
    for col in grid.T:
        if 'x' not in col:
            if not (col[0] < col[1] < col[2] or col[0] > col[1] > col[2]):
                return False
    return True

def calculate_sum(grid):
    diagonal_sum = sum([grid[i][i] for i in range(3)])
    top_row_sum = sum(grid[0])
    right_col_sum = sum(grid.T[2])
    return diagonal_sum + top_row_sum + right_col_sum

def solve(grid):
    x_positions = np.argwhere(grid == 'x')
    possible_values = [i for i in range(38, 76) if i not in grid]
    min_sum = float('inf')
    min_permutation = None

    for perm in permutations(possible_values):
        new_grid = grid.copy()
        for i, (x_row, x_col) in enumerate(x_positions):
            new_grid[x_row][x_col] = perm[i]
        
        if is_valid(new_grid):
            current_sum = calculate_sum(new_grid)
            if current_sum < min_sum:
                min_sum = current_sum
                min_permutation = new_grid

    replacements = []
    for i, (x_row, x_col) in enumerate(x_positions):
        replacements.append((x_row, x_col, min_permutation[x_row][x_col]))

    return replacements

initial_grid = np.array([['x', '42', '38'],
                         ['x', 'x', 'x'],
                         ['x', '63', 'x']])

solution = solve(initial_grid)
print(solution)
