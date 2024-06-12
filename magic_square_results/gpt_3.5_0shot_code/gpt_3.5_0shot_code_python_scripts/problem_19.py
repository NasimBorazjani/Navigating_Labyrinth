
import numpy as np
from itertools import permutations

# Given grid
grid = np.array([[64, 78, 'x'],
                 ['x', 'x', 'x'],
                 ['x', 'x', 'x']])

# Given sums
col_sum = 234
row_sum = 201
diag_sum = 213

# Generate all permutations of unique integers from 50 to 84
unique_integers = list(permutations(range(50, 85), 9))

# Function to check if a grid satisfies the given conditions
def is_valid(grid):
    if grid[0, 0] + grid[1, 1] + grid[2, 2] != diag_sum:
        return False
    if sum(grid[:, 0]) != col_sum:
        return False
    if sum(grid[0, :]) != row_sum:
        return False
    return True

# Function to calculate the sum of all numbers in the grid
def total_sum(grid):
    return sum(sum(grid))

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

# Find the positions of 'x' in the solution
x_positions = [(i, j, solution[i, j]) for i in range(3) for j in range(3) if solution[i, j] == 'x']

print(x_positions)
