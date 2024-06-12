
import numpy as np

def solve_grid():
    grid = np.array([['x', 21, 'x', 'x'],
                     [18, 27, 'x', 51],
                     [24, 29, 'x', 'x'],
                     [54, 33, 25, 12]])

    # Create a list of all possible numbers
    numbers = list(range(10, 66))

    # Remove the numbers already in the grid from the list
    for row in grid:
        for num in row:
            if num != 'x' and num in numbers:
                numbers.remove(num)

    # Sort the remaining numbers in ascending order
    numbers.sort()

    # Create a list to store the replacements
    replacements = []

    # Iterate over the grid to find the 'x's
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 'x':
                # Replace the 'x' with the smallest possible number
                grid[i][j] = numbers[0]
                replacements.append((i, j, numbers[0]))
                # Remove the used number from the list
                numbers.pop(0)

    # Return the replacements
    return replacements

print(solve_grid())
