
import numpy as np
from itertools import permutations

# Define the initial grid
grid = np.array([['x', '29', '41', 'x'],
                 ['x', 'x', '32', '43'],
                 ['23', '25', '29', '44'],
                 ['12', 'x', '20', 'x']])

# Define the range of numbers
numbers = list(range(9, 49))

# Generate all possible permutations of the numbers
perms = permutations(numbers, 4)

# Function to check if a row or column is strictly increasing or decreasing
def check_order(arr):
    return all(arr[i] < arr[i+1] for i in range(len(arr)-1)) or all(arr[i] > arr[i+1] for i in range(len(arr)-1))

# Function to calculate the sum of the diagonal
def diagonal_sum(arr):
    return sum(arr[i][i] for i in range(len(arr)))

# Initialize variables to store the best solution
best_solution = None
min_sum = float('inf')

# Iterate through all permutations
for perm in perms:
    new_grid = grid.copy()
    idx = 0
    for i in range(4):
        for j in range(4):
            if new_grid[i][j] == 'x':
                new_grid[i][j] = str(perm[idx])
                idx += 1
    
    # Check if the rows and columns are in order
    rows_in_order = all(check_order([int(num) for num in row if num != 'x']) for row in new_grid)
    cols_in_order = all(check_order([int(num) for num in new_grid[:,j] if num != 'x']) for j in range(4)
    
    # Calculate the sum of the diagonal
    diag_sum = diagonal_sum(new_grid)
    
    # Update the best solution if the conditions are met
    if rows_in_order and cols_in_order and diag_sum < min_sum:
        min_sum = diag_sum
        best_solution = new_grid

# Generate the list of tuples representing the replacements
replacements = []
for i in range(4):
    for j in range(4):
        if grid[i][j] == 'x':
            replacements.append((i, j, int(best_solution[i][j])))

print(replacements)
