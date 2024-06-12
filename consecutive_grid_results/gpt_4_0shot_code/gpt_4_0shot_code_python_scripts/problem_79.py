
import numpy as np

# Define the initial grid
grid = np.array([['x', 35, 'x', 'x'],
                 [34, 36, 38, 'x'],
                 [29, 'x', 43, 'x'],
                 ['x', 'x', 49, 53]])

# Define the range of possible numbers
numbers = set(range(23, 74))

# Remove the numbers already in the grid from the set of possible numbers
for row in grid:
    for num in row:
        if num != 'x':
            numbers.remove(num)

# Define a function to find the 'x' in the grid
def find_x(grid):
    for i in range(4):
        for j in range(4):
            if grid[i, j] == 'x':
                return (i, j)
    return None

# Define a function to check if a number can be placed at a certain position
def can_place(grid, row, col, num):
    # Check the row
    for i in range(4):
        if grid[row, i] == num:
            return False
    # Check the column
    for i in range(4):
        if grid[i, col] == num:
            return False
    # Check the diagonal
    if row == col:
        for i in range(4):
            if grid[i, i] == num:
                return False
    return True

# Define a function to solve the grid
def solve(grid):
    # Find the next 'x' in the grid
    pos = find_x(grid)
    # If there is no 'x', the grid is solved
    if not pos:
        return True
    row, col = pos
    # Try to place each number in the 'x'
    for num in numbers:
        if can_place(grid, row, col, num):
            grid[row, col] = num
            numbers.remove(num)
            # Recursively try to solve the rest of the grid
            if solve(grid):
                return True
            # If the rest of the grid can't be solved, remove the number and try the next one
            grid[row, col] = 'x'
            numbers.add(num)
    return False

# Solve the grid
solve(grid)

# Print the solved grid
print(grid)
