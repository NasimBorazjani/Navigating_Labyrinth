
import numpy as np

# Initialize the grid
grid = np.array([['x', 'x', 74, 'x'],
                 [61, 'x', 80, 88],
                 ['x', 'x', 82, 89],
                 [51, 75, 83, 90]])

# Initialize the set of available numbers
available_numbers = set(range(50, 111)) - set(grid[grid != 'x'])

# Initialize the list of replacements
replacements = []

def solve(i, j):
    # If we have reached the end of the grid, return True
    if i == 4 and j == 0:
        return True

    # If the current cell is not 'x', move to the next cell
    if grid[i, j] != 'x':
        return solve(i + (j + 1) // 4, (j + 1) % 4)

    # Try each available number
    for number in sorted(available_numbers):
        # Check if the number can be placed in the current cell
        if ((i == 0 or grid[i - 1, j] < number) and
            (j == 0 or grid[i, j - 1] < number) and
            (i == 3 or grid[i + 1, j] > number) and
            (j == 3 or grid[i, j + 1] > number)):
            # Place the number in the current cell
            grid[i, j] = number
            replacements.append((i, j, number))
            available_numbers.remove(number)

            # Move to the next cell
            if solve(i + (j + 1) // 4, (j + 1) % 4):
                return True

            # If the number cannot be placed in the current cell, remove it and backtrack
            grid[i, j] = 'x'
            replacements.remove((i, j, number))
            available_numbers.add(number)

    # If no number can be placed in the current cell, return False
    return False

# Solve the problem
solve(0, 0)

# Print the replacements
print(replacements)
