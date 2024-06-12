
import numpy as np
from itertools import permutations

# Define the initial grid
grid = np.array([[45, 55, 59, 'x'],
                 ['x', 67, 'x', 'x'],
                 [60, 'x', 79, 80],
                 ['x', 'x', 'x', 83]])

# Define the range of numbers
numbers = list(range(44, 84))

# Generate all possible permutations of the numbers
perms = permutations(numbers, 12)

# Define a function to check if a grid is valid
def is_valid(grid):
    for i in range(4):
        row = grid[i]
        col = grid[:, i]
        if 'x' in row:
            continue
        if not all(row[i] < row[i+1] for i in range(3)) and not all(row[i] > row[i+1] for i in range(3)):
            return False
        if not all(col[i] < col[i+1] for i in range(3)) and not all(col[i] > col[i+1] for i in range(3)):
            return False
    return True

# Define a function to calculate the sum of the top row, right column, and diagonal
def calculate_sum(grid):
    top_row_sum = sum(grid[0])
    right_col_sum = sum(grid[:, 3])
    diagonal_sum = sum([grid[i][i] for i in range(4)])
    return top_row_sum + right_col_sum + diagonal_sum

# Iterate through all permutations and find the valid grid with the minimum sum
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
for i in range(4):
    for j in range(4):
        if grid[i][j] == 'x':
            replacements.append((i, j, min_grid[i][j]))

print(replacements)
