
import numpy as np

# Define the initial grid
grid = np.array([['x', 'x', 'x'], ['65', 'x', 'x'], ['79', '73', '50']])

# Define the range of possible numbers
numbers = list(map(str, range(34, 88)))

# Remove the numbers already in the grid from the list of possible numbers
for row in grid:
    for num in row:
        if num in numbers:
            numbers.remove(num)

# Sort the numbers in ascending order
numbers.sort()

# Define a function to check if a number can be placed in a certain position
def can_place(grid, row, col, num):
    # Check the row
    for i in range(3):
        if grid[row][i] == num:
            return False
    # Check the column
    for i in range(3):
        if grid[i][col] == num:
            return False
    # Check the diagonal
    if row == col:
        for i in range(3):
            if grid[i][i] == num:
                return False
    return True

# Define a function to solve the grid
def solve(grid):
    for row in range(3):
        for col in range(3):
            if grid[row][col] == 'x':
                for num in numbers:
                    if can_place(grid, row, col, num):
                        grid[row][col] = num
                        numbers.remove(num)
                        if solve(grid):
                            return True
                        grid[row][col] = 'x'
                        numbers.append(num)
                return False
    return True

# Solve the grid
solve(grid)

# Print the solution
print(grid)
