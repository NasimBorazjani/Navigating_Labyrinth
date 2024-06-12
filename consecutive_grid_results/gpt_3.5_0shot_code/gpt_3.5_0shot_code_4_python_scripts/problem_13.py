
import numpy as np
from itertools import permutations

# Define the initial grid
grid = np.array([[29, 45, 'x'],
                 ['x', 'x', 'x'],
                 ['x', 43, 34]])

# Define the range of numbers
numbers = list(range(21, 59))

# Generate all possible permutations of the numbers
perms = permutations(numbers, 6)

# Function to check if a grid is valid
def is_valid(grid):
    for i in range(3):
        row = grid[i]
        col = grid[:, i]
        if 'x' in row:
            continue
        if row[0] >= row[1] >= row[2] or row[0] <= row[1] <= row[2]:
            continue
        else:
            return False
        if col[0] >= col[1] >= col[2] or col[0] <= col[1] <= col[2]:
            continue
        else:
            return False
    return True

# Initialize variables for minimum sum and corresponding grid
min_sum = float('inf')
min_grid = None

# Iterate through all permutations
for perm in perms:
    temp_grid = grid.copy()
    temp_grid[temp_grid == 'x'] = perm
    if is_valid(temp_grid):
        temp_sum = temp_grid[0, :].sum() + temp_grid[:, 2].sum() + np.diag(temp_grid).sum()
        if temp_sum < min_sum:
            min_sum = temp_sum
            min_grid = temp_grid

# Generate the list of tuples representing the replacements
replacements = []
for i in range(3):
    for j in range(3):
        if grid[i, j] == 'x':
            replacements.append((i, j, min_grid[i, j]))

print(replacements)
