
import numpy as np

# Initialize the grid
grid = np.array([[79, 63, 43], [None, 68, None], [None, None, None]])

# Initialize the list of used numbers
used_numbers = [79, 63, 43, 68]

# Define the range of possible numbers
possible_numbers = list(range(41, 90))

# Define the function to check if a number can be placed in a specific position
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
    if row > 0 and grid[row-1][col] is not None and grid[row-1][col] >= num:
        return False
    if col > 0 and grid[row][col-1] is not None and grid[row][col-1] >= num:
        return False
    return True

# Define the function to solve the grid
def solve(grid):
    for row in range(3):
        for col in range(3):
            if grid[row][col] is None:
                for num in possible_numbers:
                    if num not in used_numbers and can_place(grid, row, col, num):
                        grid[row][col] = num
                        used_numbers.append(num)
                        if solve(grid):
                            return True
                        grid[row][col] = None
                        used_numbers.remove(num)
                return False
    return True

# Solve the grid
solve(grid)

# Print the solution
print(grid)
