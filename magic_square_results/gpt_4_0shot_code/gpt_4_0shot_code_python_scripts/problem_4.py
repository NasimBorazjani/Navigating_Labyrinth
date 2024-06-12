
import numpy as np
from itertools import permutations

# Define the grid
grid = np.array([[21, 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']])

# Define the range of numbers
numbers = list(range(20, 40))

# Remove the known numbers from the list
numbers.remove(21)

# Generate all possible permutations of the remaining numbers
perms = permutations(numbers, 8)

# Define the solution list
solution = []

# Iterate over all permutations
for perm in perms:
    # Fill the grid with the current permutation
    temp_grid = grid.copy()
    temp_grid[temp_grid == 'x'] = perm

    # Convert the grid to integers
    temp_grid = temp_grid.astype(int)

    # Check if the conditions are satisfied
    if np.sum(temp_grid[:, 0]) == 72 and np.sum(temp_grid[1, :]) == 95 and np.sum(np.diag(np.fliplr(temp_grid))) == 71:
        # If the conditions are satisfied, add the permutation to the solution list
        solution.append(perm)

# Convert the solution to the required format
solution = [(i//3, i%3, solution[0][i]) for i in range(8) if grid[i//3, i%3] == 'x']

print(solution)
