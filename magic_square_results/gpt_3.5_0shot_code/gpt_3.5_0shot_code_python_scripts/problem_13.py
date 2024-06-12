
import numpy as np
from itertools import permutations

# Given grid
grid = np.array([[41, 'x', 'x'],
                 [34, 'x', 'x'],
                 ['x', 'x', 'x']])

# Given sums
row_sum = 133
col_sum = 129
diag_sum = 136

# Generate all permutations of unique integers from 28 to 57
unique_integers = list(permutations(range(28, 58), 6))

# Function to check if a grid satisfies the given conditions
def is_valid(grid):
    if grid[0].sum() != col_sum:
        return False
    if grid[:, 0].sum() != row_sum:
        return False
    if grid[0, 2] + grid[1, 1] + grid[2, 0] != diag_sum:
        return False
    return True

# Function to calculate the sum of all numbers in the grid
def total_sum(grid):
    return np.sum(grid[grid != 'x'])

# Iterate through all permutations and find the one that satisfies the conditions with the lowest total sum
min_sum = float('inf')
solution = None
for integers in unique_integers:
    temp_grid = grid.copy()
    temp_grid[temp_grid == 'x'] = integers
    if is_valid(temp_grid):
        temp_sum = total_sum(temp_grid)
        if temp_sum < min_sum:
            min_sum = temp_sum
            solution = temp_grid

# Find the positions and values of the unique integers replaced with 'x'
result = []
for i in range(3):
    for j in range(3):
        if solution[i, j] == 'x':
            result.append((i, j, integers[i*3 + j]))

print(result)
