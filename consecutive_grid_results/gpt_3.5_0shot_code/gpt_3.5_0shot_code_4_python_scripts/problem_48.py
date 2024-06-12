
import numpy as np
from itertools import permutations

# Initial grid
grid = np.array([['x', '53', 'x', '79'],
                 ['46', '51', 'x', '78'],
                 ['45', 'x', '73', '77'],
                 ['42', '47', 'x', 'x']])

# Range of numbers
numbers = list(range(40, 80))

# Generate all possible permutations of the numbers
perms = permutations(numbers, 4)

# Function to check if a row or column is strictly increasing or decreasing
def check_order(arr):
    return all(arr[i] < arr[i+1] for i in range(len(arr)-1)) or all(arr[i] > arr[i+1] for i in range(len(arr)-1))

# Function to calculate the sum of the diagonal
def diagonal_sum(arr):
    return sum(arr[i][i] for i in range(len(arr)))

# Initialize variables
min_sum = float('inf')
min_perm = None

# Iterate through all permutations
for perm in perms:
    temp_grid = grid.copy()
    temp_grid[temp_grid == 'x'] = perm
    
    # Check if each row and column is in increasing or decreasing order
    if all(check_order(temp_grid[i]) for i in range(4)) and all(check_order(temp_grid[:,j]) for j in range(4)):
        # Calculate the sum of the top row, rightmost column, and diagonal
        temp_sum = sum(temp_grid[0]) + sum(temp_grid[:,3]) + diagonal_sum(temp_grid)
        
        # Update minimum sum and permutation
        if temp_sum < min_sum:
            min_sum = temp_sum
            min_perm = temp_grid

# Generate the list of tuples representing the replacements
replacements = [(i, j, int(min_perm[i][j])) for i in range(4) for j in range(4) if min_perm[i][j] != grid[i][j]]

print(replacements)
