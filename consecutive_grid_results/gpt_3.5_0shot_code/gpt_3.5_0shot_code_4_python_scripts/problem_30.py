
import numpy as np
from itertools import permutations

# Define the initial grid
grid = np.array([['x', '57', 'x'],
                 ['42', 'x', '72'],
                 ['39', 'x', '73']])

# Define the range of numbers
numbers = list(range(39, 87))

# Generate all possible permutations of the numbers
perms = permutations(numbers, 6)

# Function to check if a row or column is strictly increasing or decreasing
def check_order(arr):
    return all(arr[i] < arr[i+1] for i in range(len(arr)-1)) or all(arr[i] > arr[i+1] for i in range(len(arr)-1))

# Function to calculate the sum of the diagonal
def diagonal_sum(arr):
    return sum(arr[i][i] for i in range(3))

# Initialize variables to store the minimum sum and the corresponding grid
min_sum = float('inf')
min_grid = None

# Iterate through all permutations
for perm in perms:
    temp_grid = grid.copy()
    temp_grid[temp_grid == 'x'] = perm
    
    # Check if each row and column is in increasing or decreasing order
    if all(check_order(temp_grid[i]) for i in range(3)) and all(check_order(temp_grid[:,j]) for j in range(3)):
        # Calculate the sum of the top row, rightmost column, and diagonal
        temp_sum = sum(temp_grid[0]) + sum(temp_grid[:,2]) + diagonal_sum(temp_grid)
        
        # Update the minimum sum and corresponding grid
        if temp_sum < min_sum:
            min_sum = temp_sum
            min_grid = temp_grid

# Generate the list of tuples representing the replacements
replacements = [(i, j, min_grid[i][j]) for i in range(3) for j in range(3) if grid[i][j] == 'x']

print(replacements)
