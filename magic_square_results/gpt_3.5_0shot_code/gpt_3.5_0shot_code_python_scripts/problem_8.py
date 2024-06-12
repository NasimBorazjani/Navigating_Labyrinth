
import numpy as np
from itertools import permutations

# Given grid
grid = np.array([['52', 'x', 'x'],
                 ['x', 'x', 'x'],
                 ['x', 'x', 'x']])

# Given sums
row_sum = 144
col_sum = 130
diag_sum = 123

# Generate all permutations of unique integers from 35 to 59
unique_integers = list(permutations(range(35, 60), 7))

# Function to check if a grid satisfies the given conditions
def is_valid(grid):
    # Check row sum
    if sum(int(grid[0][i]) for i in range(3)) != row_sum:
        return False
    # Check column sum
    if sum(int(grid[i][0]) for i in range(3)) != col_sum:
        return False
    # Check diagonal sum
    if int(grid[0][2]) + int(grid[1][1]) + int(grid[2][0]) != diag_sum:
        return False
    return True

# Function to calculate the total sum of the grid
def total_sum(grid):
    return sum(int(grid[i][j]) for i in range(3) for j in range(3) if grid[i][j] != 'x')

# Initialize variables to store the best solution
best_grid = grid.copy()
min_total_sum = total_sum(grid)

# Iterate through all permutations of unique integers
for integers in unique_integers:
    temp_grid = grid.copy()
    temp_grid[0][1] = str(integers[0])
    temp_grid[0][2] = str(integers[1])
    temp_grid[1][0] = str(integers[2])
    temp_grid[1][1] = str(integers[3])
    temp_grid[1][2] = str(integers[4])
    temp_grid[2][0] = str(integers[5])
    temp_grid[2][1] = str(integers[6])

    if is_valid(temp_grid):
        temp_total_sum = total_sum(temp_grid)
        if temp_total_sum < min_total_sum:
            min_total_sum = temp_total_sum
            best_grid = temp_grid.copy()

# Find the positions and values of 'x' in the best solution
solution = []
for i in range(3):
    for j in range(3):
        if best_grid[i][j] == 'x':
            solution.append((i, j, int(grid[i][j])))

print(solution)
