
import numpy as np
from itertools import permutations

def is_valid(grid):
    for i in range(3):
        row = grid[i]
        col = grid[:, i]
        if not (all(row[0] < row[1] < row[2]) or all(row[0] > row[1] > row[2])):
            return False
        if not (all(col[0] < col[1] < col[2]) or all(col[0] > col[1] > col[2])):
            return False
    return True

def calculate_sum(grid):
    diagonal_sum = grid[0, 0] + grid[1, 1] + grid[2, 2]
    top_row_sum = np.sum(grid[0, :])
    right_col_sum = np.sum(grid[:, 2])
    return diagonal_sum + top_row_sum + right_col_sum

def solve_grid():
    grid = np.array([['x', '60', 'x'],
                     ['x', 'x', '53'],
                     ['52', '39', '20']], dtype=object)
    
    numbers = list(range(18, 71))
    perms = permutations(numbers, 6)
    
    min_sum = float('inf')
    best_grid = None
    
    for perm in perms:
        temp_grid = grid.copy()
        temp_grid[temp_grid == 'x'] = perm
        
        if is_valid(temp_grid):
            temp_sum = calculate_sum(temp_grid)
            if temp_sum < min_sum:
                min_sum = temp_sum
                best_grid = temp_grid
    
    replacements = []
    for i in range(3):
        for j in range(3):
            if grid[i, j] == 'x':
                replacements.append((i, j, best_grid[i, j]))
    
    return replacements

solution = solve_grid()
print(solution)
