
import numpy as np

# Define the grid
grid = np.array([['x', 68, 71, 'x'],
                 ['x', 'x', 62, 'x'],
                 [43, 'x', 55, 'x'],
                 [44, 45, 52, 58]])

# Define the range of possible numbers
numbers = set(range(31, 77))

# Remove the numbers already in the grid from the set of possible numbers
for row in grid:
    for cell in row:
        if cell != 'x':
            numbers.remove(cell)

# Define a function to check if a number can be placed in a given cell
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
def solve(grid, row=0, col=0):
    # If the last cell is reached, return the grid
    if row == 3 and col == 3:
        return grid
    # If the current row is finished, move to the next row
    if col == 4:
        return solve(grid, row+1, 0)
    # If the current cell is not empty, move to the next cell
    if grid[row][col] != 'x':
        return solve(grid, row, col+1)
    # Try all possible numbers for the current cell
    for num in numbers:
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            numbers.remove(num)
            if solve(grid, row, col+1) is not None:
                return grid
            grid[row][col] = 'x'
            numbers.add(num)
    return None

# Solve the grid
solution = solve(grid)

# Print the solution
if solution is not None:
    for row in solution:
        print(row)
else:
    print("No solution exists")
