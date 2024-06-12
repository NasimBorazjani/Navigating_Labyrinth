
import numpy as np
from itertools import permutations

# Define the initial grid
grid = np.array([[41, 'x', 21],
                 ['x', 'x', 'x'],
                 [12, 'x', 42]])

# Define the range of numbers
numbers = list(range(11, 49))

# Generate all possible permutations of the numbers
perms = permutations(numbers, 6)

# Define a function to check if a grid is valid
def is_valid(grid):
    for i in range(3):
        row = grid[i]
        col = grid[:, i]
        if 'x' in row:
            continue
        if row[0] >= row[1] or row[1] >= row[2]:
            return False
        if col[0] >= col[1] or col[1] >= col[2]:
            return False
    return True

# Define a function to calculate the sum of the specified elements
def calculate_sum(grid):
    return grid[0, :].sum() + grid[:, 2].sum() + grid.diagonal().sum()

# Initialize variables to keep track of the best grid and its sum
best_grid = grid.copy()
best_sum = calculate_sum(grid)

# Iterate through all permutations and update the best grid and sum if a valid solution is found
for perm in perms:
    new_grid = grid.copy()
    new_grid[new_grid == 'x'] = perm
    if is_valid(new_grid):
        new_sum = calculate_sum(new_grid)
        if new_sum < best_sum:
            best_grid = new_grid
            best_sum = new_sum

# Generate the list of tuples representing the replacements
replacements = []
for i in range(3):
    for j in range(3):
        if grid[i, j] == 'x':
            replacements.append((i, j, best_grid[i, j]))

print(replacements)
