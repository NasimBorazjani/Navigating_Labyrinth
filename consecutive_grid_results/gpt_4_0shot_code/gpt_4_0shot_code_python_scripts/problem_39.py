
import numpy as np

# Define the initial grid
grid = np.array([['x', 60, 'x'], ['x', 'x', 53], [52, 39, 20]])

# Define the range of possible numbers
numbers = set(range(18, 72))

# Remove the numbers that are already in the grid from the set of possible numbers
for row in grid:
    for number in row:
        if number != 'x':
            numbers.remove(number)

# Define a function to check if a number can be placed in a certain position
def can_place(grid, row, col, number):
    # Check the row
    for i in range(3):
        if grid[row][i] == number:
            return False
    # Check the column
    for i in range(3):
        if grid[i][col] == number:
            return False
    # Check the diagonal
    if row == col:
        for i in range(3):
            if grid[i][i] == number:
                return False
    return True

# Define a function to solve the grid
def solve(grid):
    for row in range(3):
        for col in range(3):
            if grid[row][col] == 'x':
                for number in sorted(numbers):
                    if can_place(grid, row, col, number):
                        grid[row][col] = number
                        numbers.remove(number)
                        if solve(grid):
                            return True
                        grid[row][col] = 'x'
                        numbers.add(number)
                return False
    return True

# Solve the grid
solve(grid)

# Print the solution
print(grid)
