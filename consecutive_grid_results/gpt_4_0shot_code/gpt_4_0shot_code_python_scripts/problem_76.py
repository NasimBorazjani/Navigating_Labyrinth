
import numpy as np

# Define the initial grid
grid = np.array([['47', '51', 'x', '64'],
                 ['50', '53', 'x', 'x'],
                 ['x', '55', '68', '74'],
                 ['x', 'x', '72', 'x']])

# Define the range of numbers
numbers = set(map(str, range(37, 88)))

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
            # Find the smallest number that maintains the order in the row and column
            for number in numbers:
                if (i == 0 or number > grid[i - 1, j]) and (j == 0 or number > grid[i, j - 1]):
                    grid[i, j] = number
                    numbers.remove(number)
                    replacements.append((i, j, int(number)))
                    break

# Print the replacements
print(replacements)
