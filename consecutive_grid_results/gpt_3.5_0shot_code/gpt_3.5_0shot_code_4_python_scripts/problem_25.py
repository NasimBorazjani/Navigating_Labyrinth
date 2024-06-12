
import numpy as np
from itertools import permutations

def is_valid(grid):
    for i in range(3):
        row = grid[i]
        col = grid[:, i]
        if not (all(row[0] < row[1] < row[2]) or all(row[0] > row[1] > row[2])):
            return False
        if not (all(col[0] < col[1] < col[2]) or all(col[0] > col[1] > col[2])):
            return False
    return True

def calculate_sum(grid):
    diagonal_sum = grid[0, 0] + grid[1, 1] + grid[2, 2]
    top_row_sum = np.sum(grid[0, :])
    right_col_sum = np.sum(grid[:, 2])
    return diagonal_sum + top_row_sum + right_col_sum

def solve(grid):
    x_positions = np.argwhere(grid == 'x')
    numbers = [str(num) for num in range(29, 72)]
    perms = permutations(numbers, len(x_positions))

    min_sum = float('inf')
    min_grid = None

    for perm in perms:
        temp_grid = np.copy(grid)
        for i, (x, num) in enumerate(zip(x_positions, perm)):
            temp_grid[x[0], x[1]] = num
        if is_valid(temp_grid):
            temp_sum = calculate_sum(temp_grid)
            if temp_sum < min_sum:
                min_sum = temp_sum
                min_grid = temp_grid

    replacements = []
    for i in range(3):
        for j in range(3):
            if grid[i, j] == 'x':
                replacements.append((i, j, int(min_grid[i, j])))

    return replacements

initial_grid = np.array([['x', 'x', 'x'],
                          ['39', 'x', '52'],
                          ['60', 'x', 'x']])

solution = solve(initial_grid)
print(solution)
