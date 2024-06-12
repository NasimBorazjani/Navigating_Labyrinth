
import numpy as np
from itertools import permutations

# Define the grid
grid = np.array([[52, 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']])

# Define the range of numbers
numbers = list(range(35, 60))

# Remove the already known number from the list
numbers.remove(52)

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

    # Check the conditions
    if np.sum(temp_grid[:, 0]) == 130 and np.sum(temp_grid[1, :]) == 144 and np.sum(np.diag(np.fliplr(temp_grid))) == 123:
        # If the conditions are satisfied, add the permutation to the solution list
        solution.append(perm)

# Print the solution
for i, sol in enumerate(solution[0]):
    print((np.where(grid == 'x')[0][i], np.where(grid == 'x')[1][i], sol))
