
import numpy as np

# Define the initial grid
grid = np.array([['x', 42, 38], ['x', 'x', 'x'], ['x', 63, 'x']])

# Define the range of possible numbers
numbers = set(range(38, 77))

# Remove the numbers that are already in the grid from the set of possible numbers
for row in grid:
    for num in row:
        if num != 'x':
            numbers.remove(num)

# Define a function to check if a number can be placed in a certain position in the grid
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
    # Find the next empty position
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'x':
                # Try to place a number in the empty position
                for num in sorted(numbers):
                    if can_place(grid, i, j, num):
                        grid[i][j] = num
                        numbers.remove(num)
                        # Recursively solve the rest of the grid
                        if solve(grid):
                            return True
                        # If the grid can't be solved, backtrack and try the next number
                        grid[i][j] = 'x'
                        numbers.add(num)
                return False
    return True

# Solve the grid
solve(grid)

# Print the solution
print(grid)
