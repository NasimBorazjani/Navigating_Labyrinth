
import numpy as np

# Define the initial grid
grid = np.array([['x', 73, 74, 'x'],
                 [46, 'x', 63, 72],
                 ['x', 47, 'x', 'x'],
                 [41, 45, 'x', 54]])

# Define the range of possible numbers
numbers = set(range(35, 81))

# Remove the numbers that are already in the grid from the set of possible numbers
for row in grid:
    for number in row:
        if number != 'x':
            numbers.remove(number)

# Define a function to check if a number can be placed in a certain position
def is_valid(grid, row, col, num):
    # Check the row
    for x in range(4):
        if grid[row][x] == num:
            return False

    # Check the column
    for x in range(4):
        if grid[x][col] == num:
            return False

    # Check the order
    if row > 0 and grid[row - 1][col] != 'x' and grid[row - 1][col] > num:
        return False
    if col > 0 and grid[row][col - 1] != 'x' and grid[row][col - 1] > num:
        return False

    return True

# Define a function to solve the grid
def solve(grid):
    for x in range(4):
        for y in range(4):
            if grid[x][y] == 'x':
                for num in numbers:
                    if is_valid(grid, x, y, num):
                        grid[x][y] = num
                        numbers.remove(num)

                        if solve(grid):
                            return True

                        grid[x][y] = 'x'
                        numbers.add(num)

                return False

    return True

# Solve the grid
solve(grid)

# Print the solution
print(grid)
