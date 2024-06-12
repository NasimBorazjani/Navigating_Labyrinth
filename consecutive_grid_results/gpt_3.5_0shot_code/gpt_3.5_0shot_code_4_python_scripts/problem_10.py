
import numpy as np
from itertools import permutations

def is_valid(grid):
    for i in range(3):
        row = grid[i]
        col = grid[:, i]
        if 'x' not in row:
            if not (all(row[j] < row[j+1] for j in range(2)) or all(row[j] > row[j+1] for j in range(2))):
                return False
        if 'x' not in col:
            if not (all(col[j] < col[j+1] for j in range(2)) or all(col[j] > col[j+1] for j in range(2))):
                return False
    return True

def calculate_sum(grid):
    diagonal_sum = grid[0, 0] + grid[1, 1] + grid[2, 2]
    top_row_sum = np.sum(grid[0])
    right_col_sum = np.sum(grid[:, 2])
    return diagonal_sum + top_row_sum + right_col_sum

def solve(grid):
    x_positions = np.argwhere(grid == 'x')
    numbers = [str(i) for i in range(41, 79)]
    perms = permutations(numbers, len(x_positions))
    
    min_sum = float('inf')
    min_grid = None
    
    for perm in perms:
        temp_grid = np.copy(grid)
        for i in range(len(x_positions)):
            temp_grid[x_positions[i][0], x_positions[i][1]] = perm[i]
        
        if is_valid(temp_grid):
            temp_sum = calculate_sum(temp_grid)
            if temp_sum < min_sum:
                min_sum = temp_sum
                min_grid = temp_grid
    
    replacements = []
    for i in range(3):
        for j in range(3):
            if grid[i, j] == 'x':
                replacements.append((i, j, int(min_grid[i, j])))
    
    return replacements

initial_grid = np.array([['x', '59', 'x'],
                          ['47', 'x', '62'],
                          ['x', '50', '63']])

solution = solve(initial_grid)
print(solution)
