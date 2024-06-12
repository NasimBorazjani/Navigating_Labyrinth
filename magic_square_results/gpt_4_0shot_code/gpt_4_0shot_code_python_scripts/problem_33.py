
import numpy as np
from itertools import combinations

# Define the grid
grid = np.array([['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 55]])

# Define the range of numbers
numbers = list(range(31, 76))

# Remove the numbers already in the grid
numbers = [n for n in numbers if n not in grid]

# Generate all possible combinations of numbers
combs = list(combinations(numbers, 8))

# Define the target sums
target_sums = [138, 171, 145]

# Iterate over all combinations
for comb in combs:
    # Create a copy of the grid
    grid_copy = np.copy(grid)
    
    # Replace the 'x's with the numbers in the combination
    for i in range(3):
        for j in range(3):
            if grid_copy[i, j] == 'x':
                grid_copy[i, j] = comb.pop(0)
    
    # Check if the sums match the target sums
    if np.sum(grid_copy[:, 0]) == target_sums[0] and np.sum(grid_copy[1, :]) == target_sums[1] and np.sum(grid_copy.diagonal()[::-1]) == target_sums[2]:
        # If they do, print the solution
        print([(i, j, grid_copy[i, j]) for i in range(3) for j in range(3) if grid[i, j] == 'x'])
        break
