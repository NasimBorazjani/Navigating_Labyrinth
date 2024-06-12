
import numpy as np
from itertools import permutations

# Define the initial grid
grid = np.array([[16, 'x', 41],
                 ['x', 30, 'x'],
                 ['x', 29, 30]])

# Define the range of numbers
numbers = list(range(13, 46))

# Generate all possible permutations of the numbers
perms = permutations(numbers, 3)

# Initialize variables to store the minimum sum and corresponding solution
min_sum = float('inf')
solution = []

# Iterate through all permutations
for perm in perms:
    # Replace 'x's with the numbers from the permutation
    new_grid = grid.copy()
    idx = 0
    for i in range(3):
        for j in range(3):
            if new_grid[i, j] == 'x':
                new_grid[i, j] = perm[idx]
                idx += 1
    
    # Calculate the sum of the top row, rightmost column, and diagonal
    row_sum = sum(new_grid[0])
    col_sum = sum(new_grid[:, 2])
    diag_sum = sum([new_grid[i, i] for i in range(3)])
    total_sum = row_sum + col_sum + diag_sum
    
    # Update the minimum sum and solution if a new minimum is found
    if total_sum < min_sum:
        min_sum = total_sum
        solution = [(i, j, new_grid[i, j]) for i in range(3) for j in range(3)]

# Print the solution
print(solution)
