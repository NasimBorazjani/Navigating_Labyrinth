
import numpy as np
from itertools import permutations

# Given grid
grid = np.array([[48, 'x', 'x'],
                 ['x', 'x', 'x'],
                 ['x', 49, 'x']])

# Given sums
row_sum = 209
col_sum = 150
diag_sum = 169

# Generate all permutations of unique integers from 40 to 89
unique_integers = list(permutations(range(40, 90), 6))

# Function to check if a grid satisfies the given conditions
def is_valid(grid):
    if sum(grid[0]) == col_sum and sum(grid[:,0]) == row_sum and grid[0,2] + grid[1,1] + grid[2,0] == diag_sum:
        return True
    return False

# Function to calculate the sum of all numbers in the grid
def total_sum(grid):
    return sum(sum(grid, []))

# Initialize variables to keep track of the best solution found so far
best_solution = None
best_sum = float('inf')

# Iterate through all permutations of unique integers
for integers in unique_integers:
    new_grid = grid.copy()
    new_grid[0,1] = integers[0]
    new_grid[0,2] = integers[1]
    new_grid[1,0] = integers[2]
    new_grid[1,1] = integers[3]
    new_grid[1,2] = integers[4]
    new_grid[2,0] = integers[5]
    
    if is_valid(new_grid):
        current_sum = total_sum(new_grid)
        if current_sum < best_sum:
            best_sum = current_sum
            best_solution = [(0, 1, integers[0]), (0, 2, integers[1]), (1, 0, integers[2]), 
                             (1, 1, integers[3]), (1, 2, integers[4]), (2, 0, integers[5])]

print(best_solution)
