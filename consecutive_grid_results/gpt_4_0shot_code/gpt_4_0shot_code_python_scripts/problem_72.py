
import numpy as np

# Initialize the grid
grid = np.array([[25, 'x', 'x', 57],
                 [39, 45, 56, 'x'],
                 [43, 'x', 58, 'x'],
                 [46, 'x', 65, 69]])

# Find the positions of the 'x's
x_positions = np.where(grid == 'x')

# Initialize the list of replacements
replacements = []

# Try all possible numbers for each 'x'
for i in range(len(x_positions[0])):
    for num in range(21, 72):
        # Check if the number is already in the grid
        if num not in grid:
            # Check if the number maintains the order in the row and column
            row = x_positions[0][i]
            col = x_positions[1][i]
            if (grid[row, :col].tolist() + [num] + grid[row, col+1:].tolist() == sorted(grid[row, :col].tolist() + [num] + grid[row, col+1:].tolist()) and
                grid[:row, col].tolist() + [num] + grid[row+1:, col].tolist() == sorted(grid[:row, col].tolist() + [num] + grid[row+1:, col].tolist())):
                # Add the number to the grid and the list of replacements
                grid[row, col] = num
                replacements.append((row, col, num))
                break

# Print the list of replacements
print(replacements)
