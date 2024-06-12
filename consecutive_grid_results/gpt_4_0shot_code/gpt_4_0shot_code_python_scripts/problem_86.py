
import numpy as np

# Initialize the grid
grid = np.array([[81, 52, 'x', 'x'],
                 ['x', 50, 53, 'x'],
                 [42, 'x', 54, 74],
                 ['x', 'x', 56, 77]])

# Find the positions of the 'x's
x_positions = np.where(grid == 'x')

# Initialize the list of tuples
tuples = []

# Initialize the list of available numbers
available_numbers = list(range(28, 84))

# Remove the numbers that are already in the grid
for row in grid:
    for number in row:
        if number != 'x' and number in available_numbers:
            available_numbers.remove(number)

# Sort the available numbers in ascending order
available_numbers.sort()

# Replace the 'x's with the smallest available numbers
for i in range(len(x_positions[0])):
    row = x_positions[0][i]
    col = x_positions[1][i]
    number = available_numbers.pop(0)
    tuples.append((row, col, number))

# Print the solution
print(tuples)
