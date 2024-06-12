
import numpy as np

# Define the initial grid
grid = np.array([[66, 'x', 'x'], [65, 68, 'x'], ['x', 'x', 79]], dtype='object')

# Define the range of possible numbers
numbers = list(range(50, 94))

# Remove the numbers that are already in the grid from the list of possible numbers
for row in grid:
    for cell in row:
        if cell != 'x':
            numbers.remove(cell)

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
