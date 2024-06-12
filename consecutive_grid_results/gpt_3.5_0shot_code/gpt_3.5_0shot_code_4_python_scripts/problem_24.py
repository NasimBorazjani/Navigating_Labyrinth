
import numpy as np
from itertools import permutations

# Initial grid
grid = np.array([[66, 'x', 'x'],
                 [65, 68, 'x'],
                 ['x', 'x', 79]])

# Possible numbers to fill in 'x'
numbers = list(range(50, 93))

# Function to check if a row or column is strictly increasing or decreasing
def check_order(arr):
    return all(arr[i] < arr[i+1] for i in range(len(arr)-1)) or all(arr[i] > arr[i+1] for i in range(len(arr)-1))

# Function to calculate the sum of the diagonal, top row, and rightmost column
def calculate_sum(grid):
    diagonal_sum = sum(grid[i][i] for i in range(3))
    top_row_sum = sum(grid[0])
    rightmost_column_sum = sum(grid[i][2] for i in range(3))
    return diagonal_sum + top_row_sum + rightmost_column_sum

# Generate all permutations of numbers to fill in 'x'
perms = permutations(numbers, 3)

min_sum = float('inf')
solution = []

# Iterate through all permutations and check if they satisfy the conditions
for perm in perms:
    new_grid = grid.copy()
    new_grid[0][1] = perm[0]
    new_grid[0][2] = perm[1]
    new_grid[1][2] = perm[2]
    
    if check_order(new_grid[0]) and check_order(new_grid[:, 0]):
        if calculate_sum(new_grid) < min_sum:
            min_sum = calculate_sum(new_grid)
            solution = [(0, 1, perm[0]), (0, 2, perm[1]), (1, 2, perm[2])]

print(solution)
