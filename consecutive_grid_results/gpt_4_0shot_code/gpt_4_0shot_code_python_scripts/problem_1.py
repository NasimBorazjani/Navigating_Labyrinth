
import numpy as np

# Define the initial grid
grid = np.array([[16, 'x', 41], ['x', 30, 'x'], ['x', 29, 30]], dtype=object)

# Define the range of numbers
numbers = set(range(13, 47))

# Remove the numbers already in the grid from the set of numbers
for row in grid:
    for num in row:
        if num != 'x':
            numbers.remove(num)

# Define the positions of the 'x's
positions = [(i, j) for i in range(3) for j in range(3) if grid[i, j] == 'x']

# Sort the positions by row and column
positions.sort(key=lambda x: (x[0], x[1]))

# Replace the 'x's with the smallest available numbers
replacements = []
for pos in positions:
    num = min(numbers)
    numbers.remove(num)
    grid[pos[0], pos[1]] = num
    replacements.append((pos[0], pos[1], num))

# Print the replacements
print(replacements)
