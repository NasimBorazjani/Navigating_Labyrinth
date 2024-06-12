
import numpy as np
from itertools import permutations

# Define the initial grid
grid = np.array([[33, 37, 'x', 58],
                 [44, 51, 'x', 63],
                 ['x', 52, 62, 64],
                 ['x', 'x', 65, 'x']])

# Define the range of numbers
numbers = list(range(33, 78))

# Generate all possible permutations of the numbers
perms = permutations(numbers, 4)

# Function to check if a row or column is strictly increasing or decreasing
def check_order(arr):
    return all(arr[i] < arr[i+1] for i in range(len(arr)-1)) or all(arr[i] > arr[i+1] for i in range(len(arr)-1))

# Function to calculate the sum of the diagonal
def diagonal_sum(arr):
    return sum(arr[i][i] for i in range(len(arr)))

min_sum = float('inf')
solution = []

# Iterate through all permutations
for perm in perms:
    new_grid = grid.copy()
    idx = 0
    for i in range(4):
        for j in range(4):
            if new_grid[i][j] == 'x':
                new_grid[i][j] = perm[idx]
                idx += 1
    if all(check_order(row) for row in new_grid) and all(check_order(col) for col in new_grid.T):
        diag_sum = diagonal_sum(new_grid)
        if diag_sum < min_sum:
            min_sum = diag_sum
            solution = [(i, j, new_grid[i][j]) for i in range(4) for j in range(4) if grid[i][j] == 'x']

print(solution)
