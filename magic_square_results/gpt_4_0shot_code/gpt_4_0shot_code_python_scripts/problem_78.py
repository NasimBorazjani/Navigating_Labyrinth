
import numpy as np

# Define the grid
grid = np.array([['x', 22, 'x', 'x'],
                 [28, 47, 42, 'x'],
                 [16, 'x', 30, 24],
                 ['x', 'x', 'x', 'x']])

# Define the constraints
row_sums = [None, 158, 87, None]
col_sums = [None, 135, 153, None]
diag_sum = 140

# Define the range of possible values
values = list(range(13, 55))

# Remove the known values from the list of possible values
for row in grid:
    for value in row:
        if value != 'x' and value in values:
            values.remove(value)

# Define a function to check if a value can be placed in a specific position
def is_valid(grid, row, col, value):
    # Check the row
    if row_sums[row] is not None and sum(grid[row]) + value > row_sums[row]:
        return False

    # Check the column
    if col_sums[col] is not None and sum(grid[:, col]) + value > col_sums[col]:
        return False

    # Check the diagonal
    if row == col and sum(np.diag(grid)) + value > diag_sum:
        return False

    return True

# Define a function to solve the problem
def solve(grid):
    # Find the next empty position
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 'x':
                # Try each possible value
                for value in values:
                    if is_valid(grid, i, j, value):
                        # Place the value
                        grid[i][j] = value

                        # Recurse
                        if solve(grid):
                            return True

                        # Undo the placement
                        grid[i][j] = 'x'

                # No valid placement
                return False

    # All positions are filled
    return True

# Solve the problem
if solve(grid):
    print(grid)
else:
    print("No solution found")
