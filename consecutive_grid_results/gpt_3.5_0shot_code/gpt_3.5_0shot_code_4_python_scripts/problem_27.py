
import numpy as np
from itertools import permutations

# Define the initial grid
grid = np.array([[52, 'x', 'x'],
                 [50, 'x', 'x'],
                 ['x', 'x', 69]])

# Define the range of numbers
numbers = list(range(46, 89))

# Generate all possible permutations of the numbers
perms = permutations(numbers, 6)

# Define a function to check if a grid is valid
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

# Initialize variables to keep track of the minimum sum and the corresponding grid
min_sum = float('inf')
min_grid = None

# Iterate through all permutations of numbers
for perm in perms:
    temp_grid = grid.copy()
    idx = 0
    for i in range(3):
        for j in range(3):
            if temp_grid[i, j] == 'x':
                temp_grid[i, j] = perm[idx]
                idx += 1
    if is_valid(temp_grid):
        diagonal_sum = temp_grid[0, 0] + temp_grid[1, 1] + temp_grid[2, 2]
        rightmost_col_sum = sum(temp_grid[:, 2])
        topmost_row_sum = sum(temp_grid[0, :])
        total_sum = diagonal_sum + rightmost_col_sum + topmost_row_sum
        if total_sum < min_sum:
            min_sum = total_sum
            min_grid = temp_grid

# Generate the list of tuples representing the replacements
replacements = []
for i in range(3):
    for j in range(3):
        if grid[i, j] == 'x':
            replacements.append((i, j, min_grid[i, j]))

print(replacements)
