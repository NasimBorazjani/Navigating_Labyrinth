
import numpy as np
from itertools import permutations

def check_valid(grid):
    for i in range(4):
        row = grid[i]
        col = grid[:, i]
        if not (all(row[:-1] < row[1:]) or all(row[:-1] > row[1:])) or not (all(col[:-1] < col[1:]) or all(col[:-1] > col[1:])):
            return False
    return True

def calculate_sum(grid):
    diagonal_sum = np.trace(grid)
    top_row_sum = np.sum(grid[0])
    right_col_sum = np.sum(grid[:, -1])
    return diagonal_sum + top_row_sum + right_col_sum

def solve(grid):
    x_positions = np.argwhere(grid == 'x')
    numbers = [str(i) for i in range(17, 67)]
    min_sum = float('inf')
    min_grid = None

    for perm in permutations(numbers, len(x_positions)):
        temp_grid = grid.copy()
        for i, (x, y) in enumerate(x_positions):
            temp_grid[x, y] = perm[i]

        if check_valid(temp_grid):
            current_sum = calculate_sum(temp_grid)
            if current_sum < min_sum:
                min_sum = current_sum
                min_grid = temp_grid.copy()

    result = []
    for i, (x, y) in enumerate(x_positions):
        result.append((x, y, int(min_grid[x, y])))

    return result

initial_grid = np.array([['42', '56', '64', 'x'],
                          ['x', 'x', '55', 'x'],
                          ['30', 'x', 'x', 'x'],
                          ['24', 'x', '45', 'x']])

solution = solve(initial_grid)
print(solution)
