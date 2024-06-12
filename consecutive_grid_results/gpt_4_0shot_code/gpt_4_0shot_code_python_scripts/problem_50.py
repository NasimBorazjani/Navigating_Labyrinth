
import numpy as np

# Initialize the grid
grid = np.array([['x', 'x', 'x', 60],
                 [47, 'x', 62, 65],
                 ['x', 58, 67, 68],
                 [54, 'x', 74, 'x']])

# Create a list to store the replacements
replacements = []

# Define the range of possible numbers
numbers = set(range(36, 77))

# Remove the known numbers from the set of possible numbers
for row in grid:
    for cell in row:
        if cell != 'x':
            numbers.remove(cell)

# Define a function to check if a number can be placed in a certain position
def is_valid(grid, row, col, num):
    # Check the row
    for i in range(4):
        if grid[row][i] == num:
            return False
    # Check the column
    for i in range(4):
        if grid[i][col] == num:
            return False
    # Check the order
    if row > 0 and grid[row-1][col] != 'x' and grid[row-1][col] >= num:
        return False
    if col > 0 and grid[row][col-1] != 'x' and grid[row][col-1] >= num:
        return False
    return True

# Define a function to solve the grid
def solve(grid):
    for row in range(4):
        for col in range(4):
            if grid[row][col] == 'x':
                for num in numbers:
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        numbers.remove(num)
                        replacements.append((row, col, num))
                        if solve(grid):
                            return True
                        grid[row][col] = 'x'
                        numbers.add(num)
                        replacements.remove((row, col, num))
                return False
    return True

# Solve the grid
solve(grid)

# Print the replacements
print(replacements)
