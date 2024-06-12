
import numpy as np
from itertools import permutations

def check_magic_square(grid):
    row_sum = [86, 99, grid[0,0] + grid[1,1] + grid[2,2]]
    col_sum = [99, grid[0,0] + grid[1,0] + grid[2,0], grid[0,1] + grid[1,1] + grid[2,1]]
    diag_sum = [76, grid[0,2] + grid[1,1] + grid[2,0]]
    
    if all(x == y for x, y in zip(row_sum, col_sum)) and row_sum[0] == diag_sum[0]:
        return True
    return False

grid = np.array([[25, 'x', 'x'],
                 ['x', 'x', 'x'],
                 ['x', 'x', 'x']])

possible_values = [i for i in range(20, 40)]
positions = [(i, j) for i in range(3) for j in range(3) if grid[i, j] == 'x']

min_sum = float('inf')
min_solution = []

for perm in permutations(possible_values, len(positions)):
    temp_grid = grid.copy()
    for pos, val in zip(positions, perm):
        temp_grid[pos] = val
    if check_magic_square(temp_grid):
        temp_sum = sum(sum(temp_grid, []))
        if temp_sum < min_sum:
            min_sum = temp_sum
            min_solution = [(pos[0], pos[1], val) for pos, val in zip(positions, perm)]

print(min_solution)
