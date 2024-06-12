
import numpy as np

def solve_grid():
    grid = np.array([['x', 'x', '58', 'x'],
                     ['44', '54', '59', 'x'],
                     ['43', 'x', '63', '75'],
                     ['x', 'x', 'x', '84']])
    replacements = []
    available_numbers = set(range(36, 87)) - set(map(int, grid[grid != 'x']))

    for i in range(4):
        for j in range(4):
            if grid[i, j] == 'x':
                if i > 0 and grid[i - 1, j] != 'x':
                    available_numbers -= set(range(int(grid[i - 1, j]), 87))
                if j > 0 and grid[i, j - 1] != 'x':
                    available_numbers -= set(range(int(grid[i, j - 1]), 87))
                if i < 3 and grid[i + 1, j] != 'x':
                    available_numbers -= set(range(36, int(grid[i + 1, j]) + 1))
                if j < 3 and grid[i, j + 1] != 'x':
                    available_numbers -= set(range(36, int(grid[i, j + 1]) + 1))

                replacement = min(available_numbers)
                available_numbers.remove(replacement)
                grid[i, j] = str(replacement)
                replacements.append((i, j, replacement))

    return replacements

print(solve_grid())
