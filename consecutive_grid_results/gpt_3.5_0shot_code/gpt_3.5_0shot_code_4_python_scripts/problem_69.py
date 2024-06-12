
import numpy as np
from itertools import permutations

# Define the initial grid
grid = np.array([[48, 52, 56, 'x'],
                 [55, 'x', 'x', 71],
                 [59, 'x', 74, 82],
                 ['x', 'x', 'x', 'x']])

# Define the range of numbers
numbers = list(range(48, 93))

# Generate all possible permutations of the numbers
perms = permutations(numbers, 10)

# Define a function to check if a grid is valid
def is_valid(grid):
    for i in range(4):
        row = grid[i]
        col = grid[:, i]
        if 'x' in row:
            continue
        if not all(row[j] < row[j+1] for j in range(3)) and not all(row[j] > row[j+1] for j in range(3)):
            return False
        if not all(col[j] < col[j+1] for j in range(3)) and not all(col[j] > col[j+1] for j in range(3)):
            return False
    return True

# Define a function to calculate the sum of the diagonal
def diagonal_sum(grid):
    return sum([grid[i][i] for i in range(4)])

# Initialize variables to keep track of the best solution
min_sum = float('inf')
best_solution = None

# Iterate through all permutations of numbers
for perm in perms:
    temp_grid = grid.copy()
    idx = 0
    for i in range(4):
        for j in range(4):
            if temp_grid[i][j] == 'x':
                temp_grid[i][j] = perm[idx]
                idx += 1
    if is_valid(temp_grid):
        current_sum = sum(temp_grid[0]) + sum(temp_grid[:, 3]) + diagonal_sum(temp_grid)
        if current_sum < min_sum:
            min_sum = current_sum
            best_solution = temp_grid

# Generate the list of tuples representing the replacements
replacements = []
for i in range(4):
    for j in range(4):
        if grid[i][j] == 'x':
            replacements.append((i, j, best_solution[i][j]))

print(replacements)
