
import numpy as np
from itertools import permutations

# Define the initial grid
grid = np.array([[27, 37, 'x', 'x'],
                 [30, 'x', 'x', 'x'],
                 [32, 44, 53, 61],
                 [33, 54, 'x', 64]])

# Define the range of numbers
numbers = list(range(27, 67))

# Generate all possible permutations of the numbers
perms = permutations(numbers, 4)

# Function to check if a row or column is strictly increasing or decreasing
def check_order(arr):
    return all(arr[i] < arr[i+1] for i in range(len(arr)-1)) or all(arr[i] > arr[i+1] for i in range(len(arr)-1))

# Function to calculate the sum of the diagonal
def diagonal_sum(arr):
    return sum(arr[i][i] for i in range(len(arr)))

# Initialize variables to store the minimum sum and corresponding replacements
min_sum = float('inf')
min_replacements = []

# Iterate through all permutations
for perm in perms:
    temp_grid = grid.copy()
    replacements = []
    for i in range(4):
        for j in range(4):
            if temp_grid[i][j] == 'x':
                temp_grid[i][j] = perm.pop(0)
                replacements.append((i, j, temp_grid[i][j]))
    
    # Check if the replacements maintain the order in each row and column
    if all(check_order(row) for row in temp_grid) and all(check_order(col) for col in temp_grid.T):
        # Calculate the sum of the top row, rightmost column, and diagonal
        temp_sum = sum(temp_grid[0]) + sum(temp_grid[:, -1]) + diagonal_sum(temp_grid)
        if temp_sum < min_sum:
            min_sum = temp_sum
            min_replacements = replacements

print(min_replacements)
