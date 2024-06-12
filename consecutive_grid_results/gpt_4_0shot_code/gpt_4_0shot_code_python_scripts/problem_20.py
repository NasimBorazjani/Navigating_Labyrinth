
import numpy as np

# Initialize the grid
grid = np.array([[80, 'x', 'x'], [56, 'x', 64], [51, 'x', 76]])

# Initialize the list of available numbers
available_numbers = list(range(48, 92))
for row in grid:
    for cell in row:
        if cell != 'x':
            available_numbers.remove(cell)

# Initialize the list of replacements
replacements = []

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
                for num in available_numbers:
                    if can_place(grid, row, col, num):
                        grid[row][col] = num
                        available_numbers.remove(num)
                        replacements.append((row, col, num))
                        if solve(grid):
                            return True
                        grid[row][col] = 'x'
                        available_numbers.append(num)
                        replacements.remove((row, col, num))
                return False
    return True

# Solve the grid
solve(grid)

# Print the replacements
print(replacements)
