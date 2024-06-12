
import numpy as np

# Initialize the grid
grid = np.array([['x', 'x', 'x'], ['x', '51', 'x'], ['x', '61', '64']])
# Initialize the list of used numbers
used_numbers = [51, 61, 64]
# Initialize the list of replacements
replacements = []

# Define a function to check if a number can be placed in a certain position
def can_place(grid, row, col, num):
    # Check the row
    for i in range(3):
        if grid[row][i] != 'x' and int(grid[row][i]) == num:
            return False
    # Check the column
    for i in range(3):
        if grid[i][col] != 'x' and int(grid[i][col]) == num:
            return False
    # Check the order
    if row > 0 and grid[row-1][col] != 'x' and int(grid[row-1][col]) >= num:
        return False
    if col > 0 and grid[row][col-1] != 'x' and int(grid[row][col-1]) >= num:
        return False
    return True

# Define a function to solve the grid
def solve(grid):
    for row in range(3):
        for col in range(3):
            if grid[row][col] == 'x':
                for num in range(34, 68):
                    if num not in used_numbers and can_place(grid, row, col, num):
                        grid[row][col] = str(num)
                        used_numbers.append(num)
                        replacements.append((row, col, num))
                        if solve(grid):
                            return True
                        grid[row][col] = 'x'
                        used_numbers.remove(num)
                        replacements.remove((row, col, num))
                return False
    return True

# Solve the grid
solve(grid)

# Print the replacements
print(replacements)
