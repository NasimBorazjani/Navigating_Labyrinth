
import numpy as np

# Initialize the grid
grid = np.array([['85', '73', '59', 'x'],
                 ['x', 'x', '66', '70'],
                 ['x', '59', 'x', 'x'],
                 ['40', '41', '79', '82']])

# Convert the grid to integers, with -1 representing 'x'
grid = np.where(grid=='x', -1, grid).astype(int)

# Get the list of all possible numbers
numbers = set(range(31, 87))

# Remove the numbers that are already in the grid
numbers -= set(grid[grid!=-1])

# Initialize the list of replacements
replacements = []

def solve():
    # Find the first 'x' in the grid
    for i in range(4):
        for j in range(4):
            if grid[i, j] == -1:
                # Try to fill the 'x' with each possible number
                for number in sorted(numbers):
                    # Check if the number can be placed at the current position
                    if ((i == 0 or grid[i-1, j] < number) and
                        (j == 0 or grid[i, j-1] < number) and
                        (i == 3 or grid[i+1, j] > number) and
                        (j == 3 or grid[i, j+1] > number)):
                        # Place the number
                        grid[i, j] = number
                        numbers.remove(number)
                        replacements.append((i, j, number))
                        # Recursively solve the rest of the grid
                        if solve():
                            return True
                        # If the solution is not found, undo the current move
                        grid[i, j] = -1
                        numbers.add(number)
                        replacements.remove((i, j, number))
                return False
    # If there are no 'x's left, the grid is solved
    return True

# Solve the grid
solve()

# Print the replacements
print(replacements)
