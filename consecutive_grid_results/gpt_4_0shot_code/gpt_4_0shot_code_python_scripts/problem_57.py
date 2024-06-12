
import numpy as np

def solve_grid():
    grid = np.array([[11, 14, 'x', 'x'],
                     [12, 'x', 'x', 38],
                     ['x', 'x', 'x', 36],
                     [25, 'x', 'x', 34]])

    replacements = []
    available_numbers = set(range(7, 48)) - set(map(int, grid[grid != 'x']))

    for i in range(4):
        for j in range(4):
            if grid[i, j] == 'x':
                if i > 0 and grid[i - 1, j] != 'x':
                    lower_bound = int(grid[i - 1, j])
                else:
                    lower_bound = 7

                if j < 3 and grid[i, j + 1] != 'x':
                    upper_bound = int(grid[i, j + 1])
                else:
                    upper_bound = 47

                possible_values = list(available_numbers.intersection(set(range(lower_bound + 1, upper_bound))))
                possible_values.sort()

                if len(possible_values) > 0:
                    value = possible_values[0]
                    grid[i, j] = value
                    available_numbers.remove(value)
                    replacements.append((i, j, value))

    return replacements

print(solve_grid())
