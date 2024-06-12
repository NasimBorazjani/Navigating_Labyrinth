
import numpy as np
from itertools import permutations

# Given grid
grid = np.array([[42, 'x', 41, 'x'],
                 ['x', 48, 'x', 'x'],
                 ['x', 39, 30, 52],
                 ['x', 'x', 40, 'x']])

# Define the constraints
row_sums = [None, 191, 157, None]
col_sums = [None, 170, 162, None]
diagonal_sum = 171

# Generate all possible permutations of unique integers from 28 to 59
possible_values = [i for i in range(28, 60)]
perms = permutations(possible_values, 4)

# Initialize variables to keep track of the best solution
min_sum = float('inf')
best_solution = []

# Iterate through all permutations
for perm in perms:
    grid_copy = grid.copy()
    for i in range(4):
        for j in range(4):
            if grid_copy[i][j] == 'x':
                grid_copy[i][j] = perm.pop(0)
    
    # Check if the constraints are satisfied
    if (all(row is None or sum(row) == row_sums[i] for i, row in enumerate(grid_copy)) and
        all(col is None or sum(col) == col_sums[j] for j, col in enumerate(grid_copy.T)) and
        sum(grid_copy.diagonal()) == diagonal_sum and
        sum(grid_copy.flatten()) < min_sum):
        
        min_sum = sum(grid_copy.flatten())
        best_solution = [(i, j, grid_copy[i][j]) for i in range(4) for j in range(4) if grid_copy[i][j] != grid[i][j]]

print(best_solution)
