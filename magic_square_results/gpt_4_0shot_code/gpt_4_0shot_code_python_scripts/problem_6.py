
import numpy as np

# Define the grid
grid = np.array([['x', 20, 'x'],
                 ['x', 'x', 'x'],
                 ['x', 'x', 33]])

# Define the range of possible numbers
numbers = list(range(19, 44))

# Remove the numbers already in the grid from the list of possible numbers
for row in grid:
    for num in row:
        if num != 'x' and num in numbers:
            numbers.remove(num)

# Define the target sums
target_sum_col = 82
target_sum_row = 82
target_sum_diag = 96

# Find the missing numbers
missing_col = target_sum_col - np.sum(grid[grid[:, 0] != 'x', 0])
missing_row = target_sum_row - np.sum(grid[grid[1, :] != 'x', 1])
missing_diag = target_sum_diag - np.sum(grid[np.diag(grid[::-1, :]) != 'x'])

# Assign the missing numbers to the grid
grid[0, 0] = missing_col
grid[1, 0] = missing_row
grid[2, 0] = missing_diag

# Find the remaining missing numbers
missing_numbers = [num for num in numbers if num not in grid.flatten()]

# Assign the remaining missing numbers to the grid
grid[grid == 'x'] = missing_numbers

# Convert the grid to a list of tuples
solution = [(i, j, grid[i, j]) for i in range(3) for j in range(3) if grid[i, j] != 'x']

print(solution)
