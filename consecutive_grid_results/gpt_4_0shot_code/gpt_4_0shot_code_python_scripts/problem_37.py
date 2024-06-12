
import numpy as np

# Initialize the grid
grid = np.array([[57, 'x', 86], ['x', 75, 'x'], ['x', 76, 90]])

# Initialize the list of used numbers
used_numbers = [57, 86, 75, 76, 90]

# Initialize the list of replacements
replacements = []

# Define the range of possible numbers
number_range = list(range(48, 102))

# Remove the used numbers from the range
for number in used_numbers:
    number_range.remove(number)

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
    return True

# Define a function to solve the grid
def solve(grid):
    # Find the first empty position
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'x':
                # Try to place a number in the position
                for num in number_range:
                    if can_place(grid, i, j, num):
                        grid[i][j] = num
                        used_numbers.append(num)
                        number_range.remove(num)
                        replacements.append((i, j, num))
                        if solve(grid):
                            return True
                        # If the number cannot be placed, backtrack
                        grid[i][j] = 'x'
                        used_numbers.remove(num)
                        number_range.append(num)
                        replacements.remove((i, j, num))
                return False
    return True

# Solve the grid
solve(grid)

# Print the replacements
print(replacements)
