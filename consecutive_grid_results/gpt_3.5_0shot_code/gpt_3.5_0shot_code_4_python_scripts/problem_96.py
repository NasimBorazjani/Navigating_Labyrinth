
import numpy as np
from itertools import permutations

# Define the initial grid
grid = np.array([[81, 52, 'x', 'x'],
                  ['x', 50, 53, 'x'],
                  [42, 'x', 54, 74],
                  ['x', 'x', 56, 77]])

# Define the range of numbers
numbers = list(range(28, 83))

# Generate all possible permutations of the numbers
perms = permutations(numbers, 4)

# Initialize variables to keep track of the minimum sum and corresponding solution
min_sum = float('inf')
min_solution = []

# Iterate through all permutations
for perm in perms:
    # Replace 'x's in the grid with the numbers from the permutation
    temp_grid = grid.copy()
    idx = 0
    for i in range(4):
        for j in range(4):
            if temp_grid[i, j] == 'x':
                temp_grid[i, j] = perm[idx]
                idx += 1
    
    # Calculate the sum of the top row, rightmost column, and diagonal
    temp_sum = temp_grid[0, :].sum() + temp_grid[:, 3].sum() + np.trace(temp_grid)
    
    # Update the minimum sum and solution if a new minimum is found
    if temp_sum < min_sum:
        min_sum = temp_sum
        min_solution = [(i, j, temp_grid[i, j]) for i in range(4) for j in range(4)]
        
# Print the minimum sum and corresponding solution
print("Minimum sum:", min_sum)
print("Solution:")
for sol in min_solution:
    print(sol)
