
import numpy as np
from itertools import permutations

def is_magic_square(square):
    row_sums = [sum(row) for row in square]
    col_sums = [sum(col) for col in square.T]
    diag_sum1 = np.trace(square)
    diag_sum2 = np.trace(np.fliplr(square))
    
    return all(x == 72 for x in col_sums) and all(x == 95 for x in row_sums) and diag_sum1 == 71 and diag_sum2 == 71

def find_minimal_magic_square():
    grid = np.array([[21, 'x', 'x'],
                     ['x', 'x', 'x'],
                     ['x', 'x', 'x']])
    
    unknown_positions = [(i, j) for i in range(3) for j in range(3) if grid[i, j] == 'x']
    possible_values = [x for x in range(20, 40)]
    
    min_sum = float('inf')
    min_square = None
    
    for perm in permutations(possible_values, len(unknown_positions)):
        temp_grid = grid.copy()
        for pos, val in zip(unknown_positions, perm):
            temp_grid[pos] = val
        
        if is_magic_square(temp_grid):
            if sum(temp_grid[temp_grid != 'x']) < min_sum:
                min_sum = sum(temp_grid[temp_grid != 'x'])
                min_square = temp_grid
    
    result = [(i, j, min_square[i, j]) for i, j in unknown_positions]
    
    return result

solution = find_minimal_magic_square()
print(solution)
