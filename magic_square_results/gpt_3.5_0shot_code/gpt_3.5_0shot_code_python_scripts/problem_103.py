
import numpy as np
from itertools import permutations

def check_sums(grid):
    row_sums = [None, 315, 234, None]
    col_sums = [None, 279, 306, None]
    diag_sum = 264
    
    # Check row sums
    for i in range(4):
        if row_sums[i] is not None:
            if sum(grid[i]) != row_sums[i]:
                return False
    
    # Check column sums
    for j in range(4):
        if col_sums[j] is not None:
            if sum(grid[:, j]) != col_sums[j]:
                return False
    
    # Check diagonal sum
    if np.trace(grid) != diag_sum:
        return False
    
    return True

def solve_magic_square():
    grid = np.array([[44, None, None, None],
                     [90, 52, None, 91],
                     [None, 58, None, 62],
                     [None, 80, None, None]])
    
    unknown_indices = [(i, j) for i in range(4) for j in range(4) if grid[i, j] is None]
    possible_values = [x for x in range(36, 93)]
    
    min_sum = float('inf')
    min_solution = None
    
    for perm in permutations(possible_values, len(unknown_indices)):
        temp_grid = grid.copy()
        for idx, val in zip(unknown_indices, perm):
            temp_grid[idx] = val
        
        if check_sums(temp_grid):
            if sum(temp_grid.flatten()) < min_sum:
                min_sum = sum(temp_grid.flatten())
                min_solution = [(idx[0], idx[1], val) for idx, val in zip(unknown_indices, perm)]
    
    return min_solution

solution = solve_magic_square()
print(solution)
