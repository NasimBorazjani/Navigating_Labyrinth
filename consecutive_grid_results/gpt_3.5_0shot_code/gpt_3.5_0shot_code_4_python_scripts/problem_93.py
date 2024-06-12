
import numpy as np
from itertools import permutations

# Define the initial grid
grid = np.array([[38, 'x', 50, 'x'],
                 ['x', 'x', 64, 67],
                 [54, 'x', 71, 79],
                 ['x', 59, 89, 90]])

# Define the range of numbers
numbers = list(range(36, 91))

# Generate all possible permutations of the numbers
perms = permutations(numbers, 10)

# Function to check if a row or column is strictly increasing or decreasing
def check_order(arr):
    return all(arr[i] < arr[i+1] for i in range(len(arr)-1)) or all(arr[i] > arr[i+1] for i in range(len(arr)-1))

# Function to calculate the sum of the diagonal
def diagonal_sum(arr):
    return sum(arr[i][i] for i in range(len(arr)))

# Initialize variables to store the minimum sum and the corresponding grid
min_sum = float('inf')
min_grid = None

# Iterate through all permutations
for perm in perms:
    temp_grid = grid.copy()
    idx = 0
    for i in range(4):
        for j in range(4):
            if temp_grid[i][j] == 'x':
                temp_grid[i][j] = perm[idx]
                idx += 1
    
    # Check if the grid satisfies the conditions
    if all(check_order(row) for row in temp_grid) and all(check_order(col) for col in temp_grid.T):
        diag_sum = diagonal_sum(temp_grid)
        if diag_sum < min_sum:
            min_sum = diag_sum
            min_grid = temp_grid

# Generate the list of tuples representing the replacements
replacements = []
for i in range(4):
    for j in range(4):
        if grid[i][j] == 'x':
            replacements.append((i, j, min_grid[i][j]))

print(replacements)
