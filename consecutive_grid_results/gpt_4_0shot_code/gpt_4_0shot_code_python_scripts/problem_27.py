
import numpy as np

# Initialize the grid
grid = np.array([[52, 'x', 'x'], [50, 'x', 'x'], ['x', 'x', 69]], dtype=object)

# Initialize the list of used numbers
used_numbers = [50, 52, 69]

# Initialize the list of replacements
replacements = []

# Define the range of possible numbers
number_range = list(range(46, 90))

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
    # Find the next empty position
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'x':
                # Try to place a number in the position
                for num in number_range:
                    if num not in used_numbers and can_place(grid, i, j, num):
                        grid[i][j] = num
                        used_numbers.append(num)
                        replacements.append((i, j, num))
                        # Recursively solve the rest of the grid
                        if solve(grid):
                            return True
                        # If the number cannot be placed, remove it and backtrack
                        grid[i][j] = 'x'
                        used_numbers.remove(num)
                        replacements.remove((i, j, num))
                return False
    return True

# Solve the grid
solve(grid)

# Print the replacements
print(replacements)
