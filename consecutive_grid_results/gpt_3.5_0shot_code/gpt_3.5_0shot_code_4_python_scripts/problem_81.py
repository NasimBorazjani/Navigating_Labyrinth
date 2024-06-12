
import numpy as np
from itertools import permutations

# Define the initial grid
grid = np.array([[47, 51, 'x', 64],
                 [50, 53, 'x', 'x'],
                 ['x', 55, 68, 74],
                 ['x', 'x', 72, 'x']])

# Define the range of numbers
numbers = list(range(37, 87))

# Generate all possible permutations of the numbers
perms = permutations(numbers, 4)

# Function to check if a row or column is strictly increasing or decreasing
def check_order(arr):
    return all(arr[i] < arr[i+1] for i in range(len(arr)-1)) or all(arr[i] > arr[i+1] for i in range(len(arr)-1))

# Function to calculate the sum of the diagonal
def diagonal_sum(arr):
    return sum(arr[i][i] for i in range(len(arr)))

# Initialize variables to store the minimum sum and the corresponding grid
min_sum = float('inf')
min_grid = None

# Iterate through all permutations of numbers
for perm in perms:
    new_grid = grid.copy()
    idx = 0
    for i in range(4):
        for j in range(4):
            if new_grid[i][j] == 'x':
                new_grid[i][j] = perm[idx]
                idx += 1
    
    # Check if the rows and columns are in increasing or decreasing order
    rows_valid = all(check_order(row) for row in new_grid)
    cols_valid = all(check_order(new_grid[:,j]) for j in range(4))
    
    # Calculate the sum of the diagonal
    diag_sum = diagonal_sum(new_grid)
    
    # Update the minimum sum and corresponding grid if conditions are met
    if rows_valid and cols_valid and diag_sum < min_sum:
        min_sum = diag_sum
        min_grid = new_grid

# Generate the list of tuples representing the replacements
replacements = []
for i in range(4):
    for j in range(4):
        if grid[i][j] == 'x':
            replacements.append((i, j, min_grid[i][j]))

print(replacements)
