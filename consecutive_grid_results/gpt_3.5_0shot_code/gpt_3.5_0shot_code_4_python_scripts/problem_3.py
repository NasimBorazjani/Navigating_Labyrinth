
import numpy as np
from itertools import permutations

# Define the initial grid
grid = np.array([[22, 'x', 48],
                 [27, 'x', 'x'],
                 ['x', 42, 52]])

# Define the range of numbers
numbers = list(range(20, 53))

# Generate all possible permutations of the numbers
perms = permutations(numbers, 3)

# Function to check if a row or column is strictly increasing or decreasing
def check_order(arr):
    return all(arr[i] < arr[i+1] for i in range(len(arr)-1)) or all(arr[i] > arr[i+1] for i in range(len(arr)-1))

# Function to calculate the sum of the diagonal
def diagonal_sum(arr):
    return sum(arr[i][i] for i in range(3))

min_sum = float('inf')
solution = []

# Iterate through all permutations
for perm in perms:
    new_grid = grid.copy()
    idx = 0
    for i in range(3):
        for j in range(3):
            if new_grid[i][j] == 'x':
                new_grid[i][j] = perm[idx]
                idx += 1
    if check_order(new_grid[:,0]) and check_order(new_grid[0,:]) and diagonal_sum(new_grid) < min_sum:
        min_sum = diagonal_sum(new_grid)
        solution = [(i, j, new_grid[i][j]) for i in range(3) for j in range(3) if grid[i][j] == 'x']

print(solution)
