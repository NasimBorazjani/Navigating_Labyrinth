
import numpy as np
from itertools import permutations

# Define the initial grid
grid = np.array([['x', 'x', '23'],
                 ['31', 'x', 'x'],
                 ['x', '42', '51']])

# Define the range of numbers
numbers = list(range(18, 56))

# Generate all possible permutations of the numbers
perms = permutations(numbers, 3)

# Initialize variables to store the minimum sum and corresponding solution
min_sum = float('inf')
solution = []

# Iterate through all permutations
for perm in perms:
    # Replace 'x's with numbers from the permutation
    new_grid = grid.copy()
    new_grid[new_grid == 'x'] = perm

    # Calculate the sum of the top row, rightmost column, and diagonal
    row_sum = np.sum(new_grid[0].astype(int))
    col_sum = np.sum(new_grid[:, 2].astype(int))
    diag_sum = np.sum(np.diag(new_grid))

    total_sum = row_sum + col_sum + diag_sum

    # Update the minimum sum and solution if a new minimum is found
    if total_sum < min_sum:
        min_sum = total_sum
        solution = [(i, j, new_grid[i, j]) for i in range(3) for j in range(3)]

# Print the solution
print(solution)
