
import numpy as np
from itertools import permutations

# Define the initial grid
grid = np.array([['x', 'x', '85'],
                 ['58', 'x', '84'],
                 ['x', '74', '59']])

# Define the range of numbers
numbers = list(range(48, 91))

# Generate all possible permutations of the numbers
perms = permutations(numbers, 3)

# Function to check if a row or column is strictly increasing or decreasing
def check_order(arr):
    return all(arr[i] < arr[i+1] for i in range(len(arr)-1)) or all(arr[i] > arr[i+1] for i in range(len(arr)-1))

# Function to calculate the sum of the diagonal
def diagonal_sum(arr):
    return sum(arr[i][i] for i in range(3))

# Initialize variables to store the minimum sum and the corresponding replacements
min_sum = float('inf')
min_replacements = []

# Iterate through all permutations of numbers
for perm in perms:
    temp_grid = np.copy(grid)
    replacements = []
    for i in range(3):
        for j in range(3):
            if temp_grid[i][j] == 'x':
                temp_grid[i][j] = str(perm.pop(0))
                replacements.append((i, j, int(temp_grid[i][j])))
    
    # Check if rows and columns are strictly increasing or decreasing
    rows_valid = all(check_order(temp_grid[i]) for i in range(3))
    cols_valid = all(check_order(temp_grid[:,j]) for j in range(3))
    
    # Calculate the sum of the top row, rightmost column, and diagonal
    if rows_valid and cols_valid:
        current_sum = sum(int(temp_grid[0][j]) for j in range(3)) + sum(int(temp_grid[i][2]) for i in range(3)) + diagonal_sum(temp_grid)
        if current_sum < min_sum:
            min_sum = current_sum
            min_replacements = replacements

print(min_replacements)
