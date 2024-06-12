
import numpy as np

# Define the grid
grid = np.array([['x', 'x', 53, 62],
                 ['x', 27, 'x', 'x'],
                 [21, 22, 'x', 50],
                 ['x', 20, 25, 44]])

# Define the range of possible numbers
numbers = set(range(14, 65))

# Remove the known numbers from the set of possible numbers
for row in grid:
    for cell in row:
        if cell != 'x':
            numbers.remove(cell)

# Define a function to check if a number can be placed in a certain position
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
    if (row == 3 and col == 4):
        return True
    # If the current column is beyond the last, move to the next row
    if col == 4:
        row += 1
        col = 0
    # If the current cell is already filled, move to the next cell
    if grid[row][col] != 'x':
        return solve(grid, row, col + 1)
    # Try all possible numbers
    for num in numbers:
        if can_place(grid, row, col, num):
            # Place the number
            grid[row][col] = num
            # Remove the number from the set of possible numbers
            numbers.remove(num)
            # Move to the next cell
            if solve(grid, row, col + 1):
                return True
            # If it's not possible to solve, remove the number and backtrack
            grid[row][col] = 'x'
            numbers.add(num)
    return False

# Solve the grid
solve(grid)

# Print the solution
print(grid)
