
import numpy as np

# Define the initial grid
grid = np.array([['x', 59, 'x'], [47, 'x', 62], ['x', 50, 63]])

# Define the range of possible numbers
numbers = set(range(41, 80))

# Remove the numbers that are already in the grid from the set of possible numbers
for row in grid:
    for num in row:
        if num != 'x':
            numbers.remove(num)

# Define a function to check if a number can be placed in a certain position
def can_place(grid, row, col, num):
    # Check the row
    for i in range(3):
        if grid[row][i] != 'x' and grid[row][i] == num:
            return False
    # Check the column
    for i in range(3):
        if grid[i][col] != 'x' and grid[i][col] == num:
            return False
    # Check the diagonal
    if row == col:
        for i in range(3):
            if grid[i][i] != 'x' and grid[i][i] == num:
                return False
    return True

# Define a function to solve the grid
def solve(grid):
    for row in range(3):
        for col in range(3):
            if grid[row][col] == 'x':
                for num in sorted(numbers):
                    if can_place(grid, row, col, num):
                        grid[row][col] = num
                        numbers.remove(num)
                        if solve(grid):
                            return True
                        grid[row][col] = 'x'
                        numbers.add(num)
                return False
    return True

# Solve the grid
solve(grid)

# Print the solution
print(grid)
