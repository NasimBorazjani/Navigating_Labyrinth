
import numpy as np
from itertools import permutations

def check_sums(grid):
    row_sums = [None, 196, 162, None]
    col_sums = [None, 208, 157, None]
    diag_sum = 166
    
    for i in range(4):
        if row_sums[i] is not None and sum(grid[i]) != row_sums[i]:
            return False
        if col_sums[i] is not None and sum(grid[:, i]) != col_sums[i]:
            return False
    
    if np.trace(grid) != diag_sum:
        return False
    
    if sum(grid.flatten()) != 4 * 44 + 166:
        return False
    
    return True

def solve_magic_square():
    grid = np.array([[30, 'x', 'x', 37],
                     [41, 56, 'x', 'x'],
                     ['x', 'x', 29, 55],
                     ['x', 'x', 'x', 42]])
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i, j] == 'x']
    possible_values = [x for x in range(28, 60) if x not in grid]
    
    min_sum = float('inf')
    min_solution = None
    
    for perm in permutations(possible_values, len(unknown_positions)):
        temp_grid = grid.copy()
        for i, (row, col) in enumerate(unknown_positions):
            temp_grid[row, col] = perm[i]
        
        if check_sums(temp_grid):
            if sum(temp_grid.flatten()) < min_sum:
                min_sum = sum(temp_grid.flatten())
                min_solution = [(row, col, val) for (row, col), val in zip(unknown_positions, perm)]
    
    return min_solution

solution = solve_magic_square()
print(solution)
