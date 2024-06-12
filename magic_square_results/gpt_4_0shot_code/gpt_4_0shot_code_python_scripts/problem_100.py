
import numpy as np

# Define the grid
grid = np.array([['x', 'x', 'x', 67],
                 [62, 'x', 32, 77],
                 [66, 'x', 34, 'x'],
                 ['x', 'x', 73, 35]])

# Define the constraints
row_sums = [None, 220, 184, None]
col_sums = [None, 239, 192, None]
diag_sum = 199

# Define the range of possible values
values = list(range(30, 87))

# Remove the known values from the list of possible values
for row in grid:
    for value in row:
        if value != 'x' and value in values:
            values.remove(value)

# Define a function to check if a value can be placed at a position
def is_valid(grid, row, col, value):
    # Check the row
    if row_sums[row] is not None and np.sum([value if x=='x' else x for x in grid[row]]) > row_sums[row]:
        return False
    # Check the column
    if col_sums[col] is not None and np.sum([value if x=='x' else x for x in grid[:,col]]) > col_sums[col]:
        return False
    # Check the diagonal
    if row == col and np.sum([value if grid[i,i]=='x' else grid[i,i] for i in range(4)]) > diag_sum:
        return False
    return True

# Define a function to solve the grid
def solve(grid):
    for row in range(4):
        for col in range(4):
            if grid[row, col] == 'x':
                for value in values:
                    if is_valid(grid, row, col, value):
                        grid[row, col] = value
                        values.remove(value)
                        if solve(grid):
                            return True
                        grid[row, col] = 'x'
                        values.append(value)
                return False
    return True

# Solve the grid
solve(grid)

# Print the solution
solution = [(row, col, grid[row, col]) for row in range(4) for col in range(4) if type(grid[row, col]) is int]
print(solution)
