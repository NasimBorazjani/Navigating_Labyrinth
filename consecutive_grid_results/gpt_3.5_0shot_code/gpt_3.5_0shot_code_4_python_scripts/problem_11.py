
import numpy as np
from itertools import permutations

def check_valid(grid):
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
    grid = np.array([['x', 'x', '55'],
                     ['50', 'x', '56'],
                     ['40', '43', 'x']], dtype=object)
    
    possible_values = [i for i in range(33, 71) if i != 55]
    perms = permutations(possible_values, 3)
    
    min_sum = float('inf')
    min_grid = None
    
    for perm in perms:
        temp_grid = np.copy(grid)
        temp_grid[temp_grid == 'x'] = perm
        
        if check_valid(temp_grid):
            temp_sum = calculate_sum(temp_grid)
            if temp_sum < min_sum:
                min_sum = temp_sum
                min_grid = temp_grid
    
    replacements = []
    for i in range(3):
        for j in range(3):
            if grid[i, j] == 'x':
                replacements.append((i, j, min_grid[i, j]))
    
    return replacements

solution = solve_grid()
print(solution)
