
import numpy as np

# Define the grid
grid = np.array([[32, 75, 36, 'x'],
                 ['x', 83, 'x', 'x'],
                 ['x', 77, 58, 44],
                 ['x', 60, 'x', 'x']])

# Define the constraints
column_sums = [None, 295, 204, None]
row_sums = [None, 244, 251, None]
diagonal_sum = 237

# Define the range of possible values
possible_values = list(range(30, 87))

# Remove the known values from the possible values
for row in grid:
    for value in row:
        if value != 'x' and value in possible_values:
            possible_values.remove(value)

# Define a function to check if a value can be placed in a specific position
def is_valid(value, row, column):
    # Check the row
    if row_sums[row] is not None and (sum(grid[row]) + value > row_sums[row]):
        return False
    # Check the column
    if column_sums[column] is not None and (sum(grid[:, column]) + value > column_sums[column]):
        return False
    # Check the diagonal
    if row == column and (sum(np.diagonal(grid)) + value > diagonal_sum):
        return False
    return True

# Define a function to solve the problem
def solve():
    for row in range(4):
        for column in range(4):
            if grid[row][column] == 'x':
                for value in possible_values:
                    if is_valid(value, row, column):
                        grid[row][column] = value
                        possible_values.remove(value)
                        if solve():
                            return True
                        grid[row][column] = 'x'
                        possible_values.append(value)
                return False
    return True

# Solve the problem
if solve():
    print(grid)
else:
    print("No solution found")
