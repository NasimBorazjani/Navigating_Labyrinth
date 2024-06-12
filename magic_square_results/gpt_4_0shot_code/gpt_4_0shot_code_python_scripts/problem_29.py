
import numpy as np
from itertools import permutations

# Define the grid
grid = np.array([['x', 77, 'x'],
                 [49, 'x', 'x'],
                 ['x', 'x', 'x']])

# Define the possible numbers
numbers = list(range(34, 79))

# Remove the numbers already in the grid
numbers.remove(77)
numbers.remove(49)

# Generate all possible permutations of the remaining numbers
perms = permutations(numbers, 7)

# Define the target sums
target_sums = [180, 156, 127]

# Iterate over all permutations
for perm in perms:
    # Fill in the grid with the current permutation
    temp_grid = np.copy(grid)
    temp_grid[temp_grid == 'x'] = perm

    # Calculate the sums
    col_sum = np.sum(temp_grid[:, 0].astype(int))
    row_sum = np.sum(temp_grid[1, :].astype(int))
    diag_sum = np.sum(np.diag(np.fliplr(temp_grid)).astype(int))

    # Check if the sums match the target sums
    if col_sum == target_sums[0] and row_sum == target_sums[1] and diag_sum == target_sums[2]:
        # If they do, print the solution
        print(temp_grid)
        break
