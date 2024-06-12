
import numpy as np

# Define the initial grid
grid = np.array([['x', 'x', '38', 'x'],
                 ['x', 'x', '33', 'x'],
                 ['16', 'x', '28', '47'],
                 ['14', 'x', 'x', '52']])

# Define the range of numbers
numbers = set(str(i) for i in range(14, 70))

# Remove the numbers already in the grid from the set of numbers
for row in grid:
    for num in row:
        if num in numbers:
            numbers.remove(num)

# Sort the remaining numbers in increasing order
numbers = sorted(numbers, key=int)

# Define the positions of the 'x's
positions = [(i, j) for i in range(4) for j in range(4) if grid[i, j] == 'x']

# Fill in the 'x's with the smallest numbers from the set
for i, j in positions:
    grid[i, j] = numbers.pop(0)

# Convert the grid to integers
grid = grid.astype(int)

# Calculate the sum of the top row, right column, and diagonal
sum_top_row = np.sum(grid[0, :])
sum_right_col = np.sum(grid[:, -1])
sum_diag = np.sum(grid.diagonal())

# Print the sum
print('Sum:', sum_top_row + sum_right_col + sum_diag)

# Print the filled grid
print('Grid:', grid)

# Print the replacements
replacements = [(i, j, grid[i, j]) for i, j in positions]
print('Replacements:', replacements)
