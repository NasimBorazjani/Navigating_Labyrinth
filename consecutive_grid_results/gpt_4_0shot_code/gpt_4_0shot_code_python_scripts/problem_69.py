
import numpy as np

# Initialize the grid
grid = np.array([[24, 'x', 'x', 53],
                 [25, 31, 'x', 'x'],
                 [26, 29, 31, 'x'],
                 ['x', 'x', 'x', 'x']])

# Create a list to store the replacements
replacements = []

# Create a set of all possible numbers
numbers = set(range(9, 55))

# Remove the numbers that are already in the grid
for row in grid:
    for num in row:
        if num != 'x':
            numbers.remove(num)

# Define a function to check if a number can be placed in a cell
def can_place(grid, row, col, num):
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
def solve(grid, row=0, col=0):
    # If the last cell is reached, return True
    if row == 3 and col == 4:
        return True
    # If the current column is beyond the last, move to the next row
    if col == 4:
        row += 1
        col = 0
    # If the current cell is already filled, move to the next cell
    if grid[row][col] != 'x':
        return solve(grid, row, col + 1)
    # Try all possible numbers for the current cell
    for num in numbers:
        if can_place(grid, row, col, num):
            # Place the number in the current cell
            grid[row][col] = num
            replacements.append((row, col, num))
            numbers.remove(num)
            # Move to the next cell
            if solve(grid, row, col + 1):
                return True
            # If the placement does not lead to a solution, remove the number
            grid[row][col] = 'x'
            replacements.remove((row, col, num))
            numbers.add(num)
    return False

# Solve the grid
solve(grid)

# Print the replacements
print(replacements)
