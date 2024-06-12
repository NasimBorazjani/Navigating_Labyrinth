
import numpy as np

# Define the grid
grid = np.array([[15, 20, 'x', 'x'],
                 [6, 'x', 'x', 40],
                 ['x', 'x', 29, 'x'],
                 [46, 42, 34, 'x']])

# Define the constraints
column_sums = [None, 99, 126, None]
row_sums = [None, 97, 107, None]
diagonal_sum = 124

# Define the range of possible values
possible_values = list(range(6, 48))

# Remove the known values from the possible values
for row in grid:
    for value in row:
        if value != 'x' and value in possible_values:
            possible_values.remove(value)

# Find the position of the 'x' in the grid
x_position = np.where(grid == 'x')

# Try each possible value at the 'x' position
for value in possible_values:
    # Replace the 'x' with the current value
    grid[x_position] = value

    # Check if the constraints are satisfied
    if (np.sum(grid, axis=0) == column_sums).all() and \
       (np.sum(grid, axis=1) == row_sums).all() and \
       np.trace(grid[::-1]) == diagonal_sum:
        # If the constraints are satisfied, print the solution
        print(f"The solution is: {(x_position[0][0], x_position[1][0], value)}")
        break
