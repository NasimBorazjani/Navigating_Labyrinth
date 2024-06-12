
import numpy as np

def solve_grid():
    grid = np.array([[62, 58, 'x', 'x'],
                     [56, 57, 'x', 'x'],
                     [50, 'x', 'x', 74],
                     [48, 'x', 'x', 78]])

    # Create a list of all possible numbers
    numbers = list(range(30, 86))

    # Remove the numbers already in the grid from the list
    for row in grid:
        for num in row:
            if num != 'x' and num in numbers:
                numbers.remove(num)

    # Sort the remaining numbers in ascending order
    numbers.sort()

    # Replace the 'x's in the grid with the smallest possible numbers
    replacements = []
    for i in range(4):
        for j in range(4):
            if grid[i, j] == 'x':
                grid[i, j] = numbers.pop(0)
                replacements.append((i, j, grid[i, j]))

    return replacements

print(solve_grid())
