
import numpy as np
from itertools import permutations

def check_magic_square(grid):
    row_sum = [sum(row) for row in grid]
    col_sum = [sum(col) for col in grid.T]
    diag_sum1 = np.trace(grid)
    diag_sum2 = np.trace(np.fliplr(grid))
    
    if all(x == 107 for x in col_sum) and all(x == 124 for x in row_sum) and diag_sum1 == 108 and diag_sum2 == 108:
        return True
    else:
        return False

def solve_magic_square(grid):
    unknown_positions = [(i, j) for i in range(3) for j in range(3) if grid[i][j] == 'x']
    possible_values = [x for x in range(26, 66)]
    min_sum = float('inf')
    min_solution = None
    
    for perm in permutations(possible_values, len(unknown_positions)):
        temp_grid = np.copy(grid)
        for i, (x, y) in enumerate(unknown_positions):
            temp_grid[x][y] = perm[i]
        
        if check_magic_square(temp_grid):
            temp_sum = sum(sum(row) for row in temp_grid)
            if temp_sum < min_sum:
                min_sum = temp_sum
                min_solution = [(x, y, perm[i]) for i, (x, y) in enumerate(unknown_positions)]
    
    return min_solution

grid = np.array([['51', 'x', 'x'],
                 ['x', 'x', 'x'],
                 ['x', 'x', 'x']])

solution = solve_magic_square(grid)
print(solution)
