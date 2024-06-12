
import numpy as np
from itertools import permutations

# Define the grid
grid = np.array([['x', 46, 'x'],
                 [39, 'x', 'x'],
                 ['x', 'x', 'x']])

# Define the range of possible numbers
numbers = list(range(28, 58))

# Remove the numbers already in the grid from the list of possible numbers
numbers.remove(46)
numbers.remove(39)

# Generate all permutations of the remaining numbers
perms = permutations(numbers)

# Iterate over all permutations
for perm in perms:
    # Create a copy of the grid
    grid_copy = np.copy(grid)
    
    # Fill in the 'x's with the current permutation
    grid_copy[grid_copy == 'x'] = perm[:7]
    
    # Check if the sums of the rows, columns, and diagonal match the given sums
    if np.sum(grid_copy[:, 0]) == 126 and np.sum(grid_copy[1, :]) == 124 and np.sum(np.diag(np.fliplr(grid_copy))) == 136:
        # If they do, print the solution and break the loop
        solution = [(i, j, grid_copy[i, j]) for i in range(3) for j in range(3) if grid[i, j] == 'x']
        print(solution)
        break
