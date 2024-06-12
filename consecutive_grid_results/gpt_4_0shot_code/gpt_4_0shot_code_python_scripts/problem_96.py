
import numpy as np

# Define the initial grid
grid = np.array([['x', 58, 'x', 77],
                 ['x', 49, 63, 70],
                 ['x', 'x', 'x', 69],
                 [22, 43, 'x', 68]])

# Define the range of numbers
numbers = set(range(22, 83))

# Remove the numbers already in the grid from the set of numbers
for row in grid:
    for num in row:
        if num != 'x':
            numbers.remove(num)

# Define a function to check if a number can be placed at a certain position
def can_place(grid, row, col, num):
    # Check the row
    for i in range(4):
        if grid[row][i] == num:
            return False
    # Check the column
    for i in range(4):
        if grid[i][col] == num:
            return False
    # Check the diagonal
    if row == col:
        for i in range(4):
            if grid[i][i] == num:
                return False
    return True

# Define a function to solve the grid
def solve(grid, numbers):
    # Find the next 'x'
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 'x':
                # Try each number
                for num in numbers:
                    if can_place(grid, i, j, num):
                        # Place the number
                        grid[i][j] = num
                        numbers.remove(num)
                        # Recursively solve the rest of the grid
                        if solve(grid, numbers):
                            return True
                        # If the solution is not valid, backtrack
                        grid[i][j] = 'x'
                        numbers.add(num)
                return False
    return True

# Solve the grid
solve(grid, numbers)

# Print the solution
for i in range(4):
    for j in range(4):
        if grid[i][j] != 'x':
            print((i, j, grid[i][j]))
