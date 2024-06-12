
import numpy as np

# Define the initial grid
grid = np.array([['69', '70', 'x', 'x'],
                 ['64', '66', 'x', '75'],
                 ['62', '64', 'x', 'x'],
                 ['60', 'x', '48', '46']])

# Define the range of numbers
numbers = set(map(str, range(41, 87)))

# Remove the numbers already in the grid from the set of numbers
for row in grid:
    for number in row:
        if number in numbers:
            numbers.remove(number)

# Convert the numbers to a list and sort it
numbers = sorted(list(numbers), key=int)

# Define the replacements list
replacements = []

# Replace the 'x's in the grid
for i in range(4):
    for j in range(4):
        if grid[i, j] == 'x':
            # Find the next number in the sorted list that maintains the order in the row and column
            for number in numbers:
                if (i == 0 or int(grid[i - 1, j]) < int(number)) and \
                   (j == 0 or int(grid[i, j - 1]) < int(number)) and \
                   (i == 3 or int(grid[i + 1, j]) > int(number)) and \
                   (j == 3 or int(grid[i, j + 1]) > int(number)):
                    # Replace the 'x' with the number
                    grid[i, j] = number
                    # Add the replacement to the replacements list
                    replacements.append((i, j, number))
                    # Remove the number from the list
                    numbers.remove(number)
                    break

# Print the replacements
print(replacements)
