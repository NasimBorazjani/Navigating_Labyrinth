
import numpy as np
from itertools import permutations

def check_magic_square(grid):
    row_sum = [sum(row) for row in grid]
    col_sum = [sum(col) for col in grid.T]
    diag_sum1 = np.trace(grid)
    diag_sum2 = np.trace(np.fliplr(grid))
    
    if len(set(row_sum)) == 1 and len(set(col_sum)) == 1 and diag_sum1 == 106 and diag_sum2 == 106:
        return True
    else:
        return False

def solve_magic_square():
    grid = np.array([[47, 'x', 'x'],
                     ['x', 'x', 'x'],
                     ['x', 'x', 'x']])
    
    unknown_positions = [(i, j) for i in range(3) for j in range(3) if grid[i, j] == 'x']
    possible_values = [x for x in range(26, 66)]
    
    min_sum = float('inf')
    min_solution = None
    
    for perm in permutations(possible_values, len(unknown_positions)):
        temp_grid = grid.copy()
        for i, (row, col) in enumerate(unknown_positions):
            temp_grid[row, col] = perm[i]
        
        if check_magic_square(temp_grid):
            if sum(sum(temp_grid, [])) < min_sum:
                min_sum = sum(sum(temp_grid, []))
                min_solution = [(row, col, val) for (row, col), val in zip(unknown_positions, perm)]
    
    return min_solution

solution = solve_magic_square()
print(solution)
