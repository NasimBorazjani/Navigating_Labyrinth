
import numpy as np
from itertools import permutations

# Define the initial grid
grid = np.array([['x', 'x', '57'],
                 ['x', 'x', 'x'],
                 ['33', '43', '47']])

# Define the range of numbers
numbers = list(range(23, 66))

# Generate all possible permutations of the numbers
perms = permutations(numbers, 6)

# Define a function to check if a grid is valid
def is_valid(grid):
    for i in range(3):
        row = grid[i]
        col = grid[:, i]
        if 'x' in row:
            continue
        if not (all(row[i] < row[i+1] for i in range(2)) or all(row[i] > row[i+1] for i in range(2))):
            return False
        if not (all(col[i] < col[i+1] for i in range(2)) or all(col[i] > col[i+1] for i in range(2))):
            return False
    return True

# Define a function to calculate the sum of the top row, right column, and diagonal
def calculate_sum(grid):
    top_row_sum = sum([int(grid[0, i]) for i in range(3) if grid[0, i] != 'x'])
    right_col_sum = sum([int(grid[i, 2]) for i in range(3) if grid[i, 2] != 'x'])
    diagonal_sum = sum([int(grid[i, i]) for i in range(3) if grid[i, i] != 'x'])
    return top_row_sum + right_col_sum + diagonal_sum

# Iterate through all permutations and find the one that minimizes the sum
min_sum = float('inf')
min_grid = None
for perm in perms:
    temp_grid = grid.copy()
    temp_grid[temp_grid == 'x'] = perm
    if is_valid(temp_grid):
        temp_sum = calculate_sum(temp_grid)
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
