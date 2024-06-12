
import numpy as np
from itertools import permutations

def check_sums(grid):
    row_sums = [np.sum(row) if None not in row else None for row in grid]
    col_sums = [np.sum(col) if None not in col else None for col in grid.T]
    diag_sum1 = np.trace(grid)
    diag_sum2 = np.trace(np.fliplr(grid))
    
    return row_sums == [None, 185, 162, None] and col_sums == [None, 134, 166, None] and diag_sum1 == 173 and diag_sum2 == 173

def solve_magic_square():
    grid = np.array([[50, 'x', 'x', 42],
                     ['x', 'x', 44, 'x'],
                     [47, 'x', 49, 'x'],
                     [53, 'x', 'x', 30]])
    
    unknown_indices = [(i, j) for i in range(4) for j in range(4) if grid[i, j] == 'x']
    possible_values = [val for val in range(28, 60) if val not in grid]
    
    min_sum = float('inf')
    min_solution = None
    
    for perm in permutations(possible_values, len(unknown_indices)):
        temp_grid = grid.copy()
        for idx, (i, j) in enumerate(unknown_indices):
            temp_grid[i, j] = perm[idx]
        
        if check_sums(temp_grid):
            total_sum = np.sum(temp_grid)
            if total_sum < min_sum:
                min_sum = total_sum
                min_solution = temp_grid
    
    solution = [(i, j, min_solution[i, j]) for i, j in unknown_indices]
    
    return solution

print(solve_magic_square())
