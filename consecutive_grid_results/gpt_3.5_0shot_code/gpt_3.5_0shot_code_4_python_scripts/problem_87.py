
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
    right_col_sum = np.sum(grid[:, -1])
    return diagonal_sum + top_row_sum + right_col_sum

def solve(grid):
    x_positions = np.argwhere(grid == 'x')
    numbers = [str(i) for i in range(14, 64)]
    perms = permutations(numbers, len(x_positions))
    
    min_sum = float('inf')
    min_grid = None
    min_replacements = None
    
    for perm in perms:
        new_grid = grid.copy()
        replacements = []
        for i, (x, (r, c)) in enumerate(zip(perm, x_positions)):
            new_grid[r, c] = x
            replacements.append((r, c, int(x)))
        
        if check_valid(new_grid):
            current_sum = calculate_sum(new_grid)
            if current_sum < min_sum:
                min_sum = current_sum
                min_grid = new_grid
                min_replacements = replacements
    
    return min_replacements

initial_grid = np.array([['x', '33', 'x', '54'],
                          ['x', '39', '51', '58'],
                          ['41', '48', 'x', 'x'],
                          ['x', 'x', 'x', 'x']])

replacements = solve(initial_grid)
print(replacements)
