
import numpy as np

# Define the initial grid
grid = np.array([['45', '60', '89', 'x'],
                 ['x', '65', 'x', '84'],
                 ['55', 'x', 'x', 'x'],
                 ['x', '85', 'x', 'x']])

# Define the range of possible numbers
numbers = set(str(i) for i in range(42, 98))

# Remove the numbers already in the grid from the set of possible numbers
for row in grid:
    for num in row:
        if num in numbers:
            numbers.remove(num)

# Convert the numbers to a sorted list
numbers = sorted(list(numbers), key=int)

# Initialize the list of replacements
replacements = []

# Iterate over the grid to find the 'x's
for i in range(4):
    for j in range(4):
        if grid[i, j] == 'x':
            # Find the next number that maintains the order in the row and column
            for num in numbers:
                if (i > 0 and int(num) <= int(grid[i-1, j])) or (j > 0 and int(num) <= int(grid[i, j-1])):
                    continue
                if (i < 3 and grid[i+1, j] != 'x' and int(num) >= int(grid[i+1, j])) or (j < 3 and grid[i, j+1] != 'x' and int(num) >= int(grid[i, j+1])):
                    continue
                # If the number is valid, add it to the grid and the list of replacements
                grid[i, j] = num
                replacements.append((i, j, num))
                numbers.remove(num)
                break

print(replacements)
