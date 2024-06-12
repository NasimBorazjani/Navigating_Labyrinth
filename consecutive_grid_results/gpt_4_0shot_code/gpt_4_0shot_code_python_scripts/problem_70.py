
import numpy as np

# Define the initial grid
grid = np.array([['49', 'x', 'x', 'x'],
                 ['x', '51', 'x', '84'],
                 ['47', 'x', 'x', '79'],
                 ['x', 'x', 'x', '77']])

# Define the range of possible numbers
numbers = set(map(str, range(44, 90)))

# Remove the numbers already in the grid from the set of possible numbers
for row in grid:
    for number in row:
        if number != 'x':
            numbers.remove(number)

# Convert the numbers back to integers and sort them
numbers = sorted(map(int, numbers))

# Define the replacements list
replacements = []

# Replace the 'x's in the grid
for i in range(4):
    for j in range(4):
        if grid[i, j] == 'x':
            # Find the smallest number that maintains the order in the row and column
            for number in numbers:
                if (i == 0 or number > int(grid[i-1, j])) and (j == 0 or number > int(grid[i, j-1])):
                    # Add the replacement to the list
                    replacements.append((i, j, number))
                    # Remove the number from the set of possible numbers
                    numbers.remove(number)
                    # Replace the 'x' in the grid
                    grid[i, j] = str(number)
                    break

# Print the replacements
print(replacements)
