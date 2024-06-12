
import numpy as np

# Define the initial grid
grid = np.array([['x', 'x', 46, 'x'],
                 ['x', 57, 59, 70],
                 [56, 'x', 69, 73],
                 [57, 75, 'x', 80]])

# Define the range of possible numbers
numbers = set(range(36, 82))

# Remove the numbers already in the grid from the set of possible numbers
for row in grid:
    for number in row:
        if number != 'x':
            numbers.remove(number)

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
def solve(grid, numbers):
    for row in range(4):
        for col in range(4):
            if grid[row][col] == 'x':
                for num in numbers:
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        numbers.remove(num)
                        if solve(grid, numbers):
                            return True
                        grid[row][col] = 'x'
                        numbers.add(num)
                return False
    return True

# Solve the grid
solve(grid, numbers)

# Print the solution
for row in range(4):
    for col in range(4):
        if type(grid[row][col]) == int:
            print((row, col, grid[row][col]))
