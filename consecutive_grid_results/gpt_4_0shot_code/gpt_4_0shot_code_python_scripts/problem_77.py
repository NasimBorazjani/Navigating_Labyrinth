
import numpy as np

# Define the grid
grid = np.array([[20, 21, 33, 60],
                 [None, None, None, 49],
                 [None, 38, None, None],
                 [36, None, 46, None]])

# Define the range of possible numbers
numbers = set(range(14, 65))

# Remove the numbers that are already in the grid
for row in grid:
    for number in row:
        if number in numbers:
            numbers.remove(number)

# Convert the set to a list and sort it
numbers = sorted(list(numbers))

# Define a function to check if a number can be placed at a certain position
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
    if row > 0 and grid[row-1][col] is not None and grid[row-1][col] > num:
        return False
    if col > 0 and grid[row][col-1] is not None and grid[row][col-1] > num:
        return False

    return True

# Define a function to solve the grid
def solve(grid, numbers):
    for x in range(4):
        for y in range(4):
            if grid[x][y] is None:
                for number in numbers:
                    if is_valid(grid, x, y, number):
                        grid[x][y] = number
                        numbers.remove(number)

                        if solve(grid, numbers):
                            return True

                        grid[x][y] = None
                        numbers.append(number)
                        numbers.sort()

                return False

    return True

# Solve the grid
solve(grid, numbers)

# Print the solution
for row in grid:
    print(row)
