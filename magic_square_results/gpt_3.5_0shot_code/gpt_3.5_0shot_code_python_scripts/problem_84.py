
import numpy as np
from itertools import permutations

def check_sums(grid):
    row_sums = [np.sum(row) if 'x' not in row else None for row in grid]
    col_sums = [np.sum(col) if 'x' not in col else None for col in grid.T]
    diag_sum = np.trace(grid)
    anti_diag_sum = np.trace(np.fliplr(grid))
    
    return row_sums == [None, 253, 221, None] and col_sums == [None, 277, 204, None] and diag_sum == 252 and anti_diag_sum == 252

def solve_magic_square():
    grid = np.array([[42, 53, 43, 72],
                      ['x', 82, 54, 'x'],
                      ['x', 62, 44, 'x'],
                      ['x', 'x', 'x', 'x']])
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i, j] == 'x']
    possible_values = [val for val in range(37, 84)]
    
    min_sum = float('inf')
    min_solution = None
    
    for perm in permutations(possible_values, len(unknown_positions)):
        for i, (row, col) in enumerate(unknown_positions):
            grid[row, col] = perm[i]
        
        if check_sums(grid):
            total_sum = np.sum(grid)
            if total_sum < min_sum:
                min_sum = total_sum
                min_solution = [(row, col, val) for (row, col), val in zip(unknown_positions, perm)]
    
    return min_solution

solution = solve_magic_square()
print(solution)
