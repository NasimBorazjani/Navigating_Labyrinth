
import numpy as np
from itertools import permutations

# Define the initial grid
grid = np.array([['x', 'x', '46', 'x'],
                 ['x', '57', '59', '70'],
                 ['56', 'x', '69', '73'],
                 ['57', '75', 'x', '80']])

# Define the range of numbers
numbers = list(range(36, 81))

# Generate all possible permutations of the numbers
perms = permutations(numbers, 4)

# Initialize variables to store the minimum sum and the corresponding grid
min_sum = float('inf')
min_grid = None

# Iterate through all permutations
for perm in perms:
    # Replace 'x's with numbers from the permutation
    temp_grid = grid.copy()
    idx = 0
    for i in range(4):
        for j in range(4):
            if temp_grid[i, j] == 'x':
                temp_grid[i, j] = str(perm[idx])
                idx += 1
    
    # Calculate the sum of the top row, rightmost column, and diagonal
    row_sum = sum([int(temp_grid[0, j]) for j in range(4)])
    col_sum = sum([int(temp_grid[i, 3]) for i in range(4)])
    diag_sum = sum([int(temp_grid[i, i]) for i in range(4)])
    total_sum = row_sum + col_sum + diag_sum
    
    # Update the minimum sum and corresponding grid
    if total_sum < min_sum:
        min_sum = total_sum
        min_grid = temp_grid

# Generate the list of tuples representing the replacements
replacements = []
for i in range(4):
    for j in range(4):
        if grid[i, j] == 'x':
            replacements.append((i, j, int(min_grid[i, j])))

# Print the list of replacements
print(replacements)
