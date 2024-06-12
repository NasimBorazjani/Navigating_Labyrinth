
import numpy as np
from itertools import permutations

# Define the grid
grid = np.array([['x', 'x', 'x'], ['30', 'x', 'x'], ['x', 'x', 'x']])

# Define the range of possible numbers
numbers = list(range(20, 40))

# Remove the known number from the list of possible numbers
numbers.remove(30)

# Generate all permutations of the remaining numbers
perms = permutations(numbers, 8)

# Initialize the solution as an empty list
solution = []

# Iterate over all permutations
for perm in perms:
    # Create a copy of the grid
    grid_copy = np.copy(grid)
    
    # Fill the grid with the current permutation
    for i in range(3):
        for j in range(3):
            if grid_copy[i, j] == 'x':
                grid_copy[i, j] = perm.pop(0)
    
    # Check if the sums of the specified rows, columns, and diagonal are correct
    if np.sum(grid_copy[:, 0]) == 82 and np.sum(grid_copy[1, :]) == 87 and np.trace(grid_copy[::-1, :]) == 94:
        # If the sums are correct, add the permutation to the solution
        solution.append(grid_copy)

# Print the solution
for sol in solution:
    print(sol)
