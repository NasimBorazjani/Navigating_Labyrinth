
import numpy as np
from itertools import permutations

def check_magic_square(grid):
    col_sum = np.sum(grid, axis=0)
    row_sum = np.sum(grid, axis=1)
    diag_sum1 = np.trace(grid)
    diag_sum2 = np.trace(np.fliplr(grid))
    
    if col_sum[0] == 233 and row_sum[0] == 207 and diag_sum1 == 185 and diag_sum2 == 185:
        return True
    return False

def solve_magic_square():
    grid = np.array([[62, 82, 'x'],
                     ['x', 'x', 'x'],
                     ['x', 'x', 'x']])
    
    unknown_positions = [(0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    possible_values = [i for i in range(50, 85)]
    
    min_sum = float('inf')
    min_solution = None
    
    for perm in permutations(possible_values, len(unknown_positions)):
        temp_grid = grid.copy()
        for i, pos in enumerate(unknown_positions):
            temp_grid[pos[0], pos[1]] = perm[i]
        
        if check_magic_square(temp_grid):
            temp_sum = np.sum(temp_grid)
            if temp_sum < min_sum:
                min_sum = temp_sum
                min_solution = [(pos[0], pos[1], perm[i]) for i, pos in enumerate(unknown_positions)]
    
    return min_solution

solution = solve_magic_square()
print(solution)
