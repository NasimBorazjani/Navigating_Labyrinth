
import numpy as np
from itertools import permutations

def check_valid(grid):
    for i in range(3):
        row = grid[i]
        col = grid[:, i]
        if not (all(row[0] > row[1] > row[2]) or all(row[0] < row[1] < row[2])):
            return False
        if not (all(col[0] > col[1] > col[2]) or all(col[0] < col[1] < col[2])):
            return False
    return True

def calculate_sum(grid):
    diagonal_sum = grid[0, 0] + grid[1, 1] + grid[2, 2]
    top_row_sum = np.sum(grid[0, :])
    right_col_sum = np.sum(grid[:, 2])
    return diagonal_sum + top_row_sum + right_col_sum

def solve_grid():
    grid = np.array([['x', 'x', 'x'],
                     ['65', 'x', 'x'],
                     ['79', '73', '50']], dtype=object)
    
    numbers = list(range(34, 87))
    perms = permutations(numbers, 6)
    
    min_sum = float('inf')
    min_grid = None
    
    for perm in perms:
        temp_grid = grid.copy()
        temp_grid[0, 0] = perm[0]
        temp_grid[0, 1] = perm[1]
        temp_grid[0, 2] = perm[2]
        temp_grid[1, 1] = perm[3]
        temp_grid[1, 2] = perm[4]
        temp_grid[2, 0] = perm[5]
        
        if check_valid(temp_grid):
            current_sum = calculate_sum(temp_grid)
            if current_sum < min_sum:
                min_sum = current_sum
                min_grid = temp_grid.copy()
    
    replacements = []
    for i in range(3):
        for j in range(3):
            if grid[i, j] == 'x':
                replacements.append((i, j, min_grid[i, j]))
    
    return replacements

solution = solve_grid()
print(solution)
