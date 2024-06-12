
import numpy as np

# Define the initial grid
grid = np.array([['x', 'x', 65],
                 ['x', 47, 56],
                 [48, 44, 'x']])

# Define the range of possible numbers
numbers = list(range(40, 89))

# Define a list to store the replacements
replacements = []

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
    # Check the order
    if row > 0 and grid[row-1][col] != 'x' and grid[row-1][col] >= num:
        return False
    if col > 0 and grid[row][col-1] != 'x' and grid[row][col-1] >= num:
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
                        replacements.append((row, col, num))
                        if solve(grid):
                            return True
                        grid[row][col] = 'x'
                        numbers.append(num)
                        replacements.remove((row, col, num))
                return False
    return True

# Solve the grid
solve(grid)

# Print the replacements
print(replacements)
