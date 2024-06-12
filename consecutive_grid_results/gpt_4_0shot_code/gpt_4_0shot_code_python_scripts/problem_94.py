
import numpy as np

def solve_grid():
    grid = np.array([['x', 36, 71, 79],
                     ['x', 'x', 69, 'x'],
                     ['x', 50, 63, 70],
                     [21, 53, 'x', 62]])

    replacements = []
    available_numbers = set(range(20, 81)) - set(grid[grid != 'x'].astype(int))

    for i in range(4):
        for j in range(4):
            if grid[i, j] == 'x':
                if i > 0 and grid[i - 1, j] != 'x':
                    lower_bound = int(grid[i - 1, j])
                else:
                    lower_bound = 20

                if i < 3 and grid[i + 1, j] != 'x':
                    upper_bound = int(grid[i + 1, j])
                else:
                    upper_bound = 80

                possible_values = [num for num in available_numbers if lower_bound < num < upper_bound]
                value = min(possible_values)
                available_numbers.remove(value)
                grid[i, j] = value
                replacements.append((i, j, value))

    return replacements

print(solve_grid())
