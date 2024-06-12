
import numpy as np

def solve_grid():
    grid = np.array([['x', 47, 'x', 55],
                     [29, 34, 'x', 'x'],
                     [16, 'x', 'x', 35],
                     ['x', 26, 'x', 'x']])

    replacements = []
    available_numbers = set(range(12, 58))

    # Remove already used numbers from the available numbers
    for row in grid:
        for cell in row:
            if cell != 'x':
                available_numbers.remove(cell)

    # Sort the available numbers in ascending order
    available_numbers = sorted(list(available_numbers))

    # Replace 'x' with the smallest available number that maintains the order
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 'x':
                # Find the smallest available number that is larger than the number to its left and smaller than the number to its right
                for number in available_numbers:
                    if (j == 0 or number > grid[i][j-1]) and (j == 3 or number < grid[i][j+1]):
                        grid[i][j] = number
                        replacements.append((i, j, number))
                        available_numbers.remove(number)
                        break

    return replacements

print(solve_grid())
