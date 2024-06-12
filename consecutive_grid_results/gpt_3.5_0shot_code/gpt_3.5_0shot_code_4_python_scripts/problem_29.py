
import numpy as np
from itertools import permutations

def is_valid(grid):
    for row in grid:
        if 'x' in row:
            continue
        if not (all(row[i] < row[i+1] for i in range(2)) or all(row[i] > row[i+1] for i in range(2))):
            return False
    for col in grid.T:
        if 'x' in col:
            continue
        if not (all(col[i] < col[i+1] for i in range(2)) or all(col[i] > col[i+1] for i in range(2))):
            return False
    return True

def calculate_sum(grid):
    diagonal_sum = sum([grid[i][i] for i in range(3)])
    top_row_sum = sum(grid[0])
    right_col_sum = sum(grid[:,2])
    return diagonal_sum + top_row_sum + right_col_sum

def solve(grid):
    possible_values = [i for i in range(40, 88) if i != 65 and i != 47 and i != 56 and i != 48 and i != 44]
    perms = permutations(possible_values)
    
    min_sum = float('inf')
    min_grid = None
    
    for perm in perms:
        new_grid = grid.copy()
        idx = 0
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 'x':
                    new_grid[i][j] = perm[idx]
                    idx += 1
        
        if is_valid(new_grid):
            current_sum = calculate_sum(new_grid)
            if current_sum < min_sum:
                min_sum = current_sum
                min_grid = new_grid
    
    replacements = []
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'x':
                replacements.append((i, j, min_grid[i][j]))
    
    return replacements

initial_grid = np.array([['x', 'x', 65], ['x', 47, 56], [48, 44, 'x']])
replacements = solve(initial_grid)

print(replacements)
