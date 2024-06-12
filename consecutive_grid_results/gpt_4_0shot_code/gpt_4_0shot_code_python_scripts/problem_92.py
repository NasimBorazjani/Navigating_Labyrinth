
import numpy as np

def solve_grid():
    grid = np.array([['x', 28, 11, 'x'],
                     ['x', 27, 'x', 'x'],
                     [15, 'x', 'x', 46],
                     ['x', 'x', 'x', 50]])

    replacements = []
    available_numbers = set(range(6, 62)) - set(grid[grid != 'x'])

    for i in range(4):
        for j in range(4):
            if grid[i, j] == 'x':
                if i == 0 or j == 0:
                    min_val = min(available_numbers)
                elif i == 3 or j == 3:
                    min_val = min(available_numbers - set([grid[i-1, j], grid[i, j-1]]))
                else:
                    min_val = min(available_numbers - set([grid[i-1, j], grid[i, j-1], grid[i+1, j], grid[i, j+1]]))
                grid[i, j] = min_val
                available_numbers.remove(min_val)
                replacements.append((i, j, min_val))

    return replacements

print(solve_grid())
