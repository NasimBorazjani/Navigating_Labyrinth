
import numpy as np
from itertools import permutations

# Define the initial grid
grid = np.array([['x', 'x', '38', 'x'],
                 ['x', '30', 'x', 'x'],
                 ['20', 'x', '44', 'x'],
                 ['x', '22', 'x', '57']])

# Define the range of numbers
numbers = list(range(19, 59))

# Generate all possible permutations of the numbers
perms = permutations(numbers, 4)

# Define a function to check if a row or column is strictly increasing or decreasing
def check_order(arr):
    return all(arr[i] < arr[i+1] for i in range(len(arr)-1)) or all(arr[i] > arr[i+1] for i in range(len(arr)-1))

# Define a function to calculate the sum of the diagonal
def diagonal_sum(arr):
    return sum(arr[i][i] for i in range(len(arr)))

# Initialize variables to keep track of the minimum sum and the corresponding grid
min_sum = float('inf')
min_grid = None

# Iterate through all permutations of numbers
for perm in perms:
    new_grid = grid.copy()
    idx = 0
    for i in range(4):
        for j in range(4):
            if new_grid[i][j] == 'x':
                new_grid[i][j] = str(perm[idx])
                idx += 1
    
    # Check if the rows and columns are in increasing or decreasing order
    rows_valid = all(check_order([int(num) for num in row if num != 'x']) for row in new_grid)
    cols_valid = all(check_order([int(num) for num in new_grid[:,j] if num != 'x']) for j in range(4)
    
    # Calculate the sum of the top row, rightmost column, and diagonal
    if rows_valid and cols_valid:
        current_sum = sum(int(new_grid[0][j]) for j in range(4)) + sum(int(new_grid[i][3]) for i in range(4)) + diagonal_sum(new_grid)
        if current_sum < min_sum:
            min_sum = current_sum
            min_grid = new_grid

# Generate the list of tuples representing the replacements
replacements = [(i, j, int(min_grid[i][j])) for i in range(4) for j in range(4) if min_grid[i][j] != grid[i][j]]

print(replacements)
