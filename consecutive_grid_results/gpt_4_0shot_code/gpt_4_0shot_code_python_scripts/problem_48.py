
import numpy as np

# Define the initial grid
grid = np.array([['x', 53, 'x', 79],
                 [46, 51, 'x', 78],
                 [45, 'x', 73, 77],
                 [42, 47, 'x', 'x']])

# Define the range of numbers
numbers = set(range(40, 81))

# Remove the numbers already in the grid from the set of numbers
for row in grid:
    for num in row:
        if num != 'x':
            numbers.remove(num)

# Define a function to check if a number can be placed in a certain position
def can_place(grid, row, col, num):
    # Check the row
    for i in range(4):
        if grid[row][i] == num:
            return False
    # Check the column
    for i in range(4):
        if grid[i][col] == num:
            return False
    # Check the order
    if row > 0 and grid[row-1][col] != 'x' and grid[row-1][col] >= num:
        return False
    if col > 0 and grid[row][col-1] != 'x' and grid[row][col-1] >= num:
        return False
    return True

# Define a function to solve the grid
def solve(grid, numbers):
    # Find the next empty position
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 'x':
                # Try to place a number in the position
                for num in sorted(numbers):
                    if can_place(grid, i, j, num):
                        grid[i][j] = num
                        numbers.remove(num)
                        if solve(grid, numbers):
                            return True
                        # Backtrack
                        grid[i][j] = 'x'
                        numbers.add(num)
                return False
    return True

# Solve the grid
solve(grid, numbers)

# Print the solution
print(grid)
