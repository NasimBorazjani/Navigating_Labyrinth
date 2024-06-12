
import numpy as np

# Initialize the grid
grid = np.array([[66, 'x', 74], ['x', 60, 62], ['x', 'x', 'x']])

# Initialize the list of available numbers
available_numbers = list(range(44, 78))

# Remove the numbers that are already in the grid from the list of available numbers
for row in grid:
    for number in row:
        if number != 'x' and number in available_numbers:
            available_numbers.remove(number)

# Sort the available numbers in ascending order
available_numbers.sort()

# Initialize the list of replacements
replacements = []

# Define a function to check if a number can be placed in a certain position in the grid
def is_valid(number, row, col):
    # Check the row
    for i in range(3):
        if grid[row][i] != 'x' and grid[row][i] >= number:
            return False
    # Check the column
    for i in range(3):
        if grid[i][col] != 'x' and grid[i][col] >= number:
            return False
    return True

# Define a function to fill the grid
def fill_grid():
    for row in range(3):
        for col in range(3):
            if grid[row][col] == 'x':
                for number in available_numbers:
                    if is_valid(number, row, col):
                        grid[row][col] = number
                        available_numbers.remove(number)
                        replacements.append((row, col, number))
                        if fill_grid():
                            return True
                        grid[row][col] = 'x'
                        available_numbers.append(number)
                        replacements.remove((row, col, number))
                return False
    return True

# Fill the grid
fill_grid()

# Print the replacements
print(replacements)
