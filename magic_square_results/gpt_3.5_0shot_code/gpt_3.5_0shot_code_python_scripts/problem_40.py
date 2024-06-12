
import numpy as np
from itertools import permutations

# Given grid
grid = np.array([[38, 'x', 'x', 'x'],
                 ['x', 'x', 'x', 'x'],
                 ['x', 39, 40, 27],
                 [32, 46, 'x', 25]])

# Define the constraints
row_sums = [None, 135, 130, None]
col_sums = [None, 149, 178, None]
diag_sum = 151

# Generate all permutations of unique integers from 24 to 50
unique_integers = list(permutations(range(24, 51), 16))

# Function to check if a grid satisfies the constraints
def check_constraints(grid):
    # Check row sums
    for i in range(4):
        if row_sums[i] is not None and sum(grid[i]) != row_sums[i]:
            return False
    # Check column sums
    for j in range(4):
        if col_sums[j] is not None and sum(grid[:, j]) != col_sums[j]:
            return False
    # Check diagonal sum
    if grid[0, 3] + grid[1, 2] + grid[2, 1] + grid[3, 0] != diag_sum:
        return False
    return True

# Function to calculate the total sum of a grid
def total_sum(grid):
    return sum(sum(grid, []))

# Initialize variables to keep track of the best solution
best_sum = float('inf')
best_solution = None

# Iterate through all permutations of unique integers
for integers in unique_integers:
    temp_grid = grid.copy()
    idx = 0
    for i in range(4):
        for j in range(4):
            if temp_grid[i, j] == 'x':
                temp_grid[i, j] = integers[idx]
                idx += 1
    if check_constraints(temp_grid):
        temp_sum = total_sum(temp_grid)
        if temp_sum < best_sum:
            best_sum = temp_sum
            best_solution = temp_grid

# Convert the solution to a list of tuples
solution = []
for i in range(4):
    for j in range(4):
        if grid[i, j] == 'x':
            solution.append((i, j, best_solution[i, j]))

print(solution)
