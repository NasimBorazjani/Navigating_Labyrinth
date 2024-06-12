
import numpy as np
from itertools import permutations

# Define the grid
grid = np.array([[35, 'x', 46], ['x', 'x', 'x'], ['x', 'x', 'x']])

# Define the range of possible numbers
numbers = list(range(29, 49))

# Remove the numbers already in the grid from the list of possible numbers
for num in grid.flatten():
    if num != 'x':
        numbers.remove(num)

# Generate all permutations of the remaining numbers
perms = permutations(numbers)

# Try each permutation until a valid solution is found
for perm in perms:
    # Create a copy of the grid
    grid_copy = np.copy(grid)

    # Replace 'x' with numbers from the permutation
    i = 0
    for row in range(3):
        for col in range(3):
            if grid_copy[row, col] == 'x':
                grid_copy[row, col] = perm[i]
                i += 1

    # Check if the sums of the specified rows, columns, and diagonal are correct
    if np.sum(grid_copy[:, 0]) == 107 and np.sum(grid_copy[1, :]) == 103 and np.trace(grid_copy[::-1]) == 124:
        # If the solution is valid, print it and break the loop
        solution = []
        i = 0
        for row in range(3):
            for col in range(3):
                if grid[row, col] == 'x':
                    solution.append((row, col, perm[i]))
                    i += 1
        print(solution)
        break
