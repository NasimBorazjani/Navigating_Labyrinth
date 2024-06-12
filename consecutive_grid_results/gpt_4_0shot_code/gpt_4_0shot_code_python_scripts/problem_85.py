
import numpy as np

# Initialize the grid
grid = np.array([[71, 'x', 57, 'x'],
                 [67, 68, 'x', 73],
                 [51, 'x', 72, 'x'],
                 [50, 'x', 75, 'x']])

# Find the positions of the 'x's
x_positions = np.where(grid == 'x')

# Initialize the list of tuples
tuples = []

# Initialize the list of available numbers
available_numbers = list(range(39, 95))

# Remove the numbers that are already in the grid
for row in grid:
    for number in row:
        if number != 'x' and number in available_numbers:
            available_numbers.remove(number)

# Sort the available numbers in ascending order
available_numbers.sort()

# Try to fill the 'x's with the available numbers
for i in range(len(x_positions[0])):
    row = x_positions[0][i]
    col = x_positions[1][i]
    for number in available_numbers:
        # Check if the number can be placed in the current position
        if (row > 0 and number <= grid[row-1][col]) or \
           (row < 3 and number >= grid[row+1][col]) or \
           (col > 0 and number <= grid[row][col-1]) or \
           (col < 3 and number >= grid[row][col+1]):
            continue
        # If the number can be placed, add it to the grid and the list of tuples
        grid[row][col] = number
        tuples.append((row, col, number))
        available_numbers.remove(number)
        break

print(tuples)
