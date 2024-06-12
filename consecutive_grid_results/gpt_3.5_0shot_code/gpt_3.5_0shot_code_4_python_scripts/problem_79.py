
import numpy as np
from itertools import permutations

def check_valid(grid):
    for i in range(4):
        row = grid[i]
        col = grid[:, i]
        if not (all(row[1:] > row[:-1]) or all(row[1:] < row[:-1])):
            return False
        if not (all(col[1:] > col[:-1]) or all(col[1:] < col[:-1])):
            return False
    return True

def calculate_sum(grid):
    diagonal_sum = np.sum(np.diag(grid))
    top_row_sum = np.sum(grid[0])
    right_col_sum = np.sum(grid[:, -1])
    return diagonal_sum + top_row_sum + right_col_sum

def solve(grid):
    x_positions = np.argwhere(grid == 'x')
    numbers = [str(i) for i in range(14, 64)]
    perms = permutations(numbers, len(x_positions))

    min_sum = float('inf')
    min_grid = None

    for perm in perms:
        temp_grid = grid.copy()
        for i, (x, num) in enumerate(zip(x_positions, perm)):
            temp_grid[tuple(x)] = num
        if check_valid(temp_grid):
            temp_sum = calculate_sum(temp_grid)
            if temp_sum < min_sum:
                min_sum = temp_sum
                min_grid = temp_grid

    replacements = []
    for i in range(4):
        for j in range(4):
            if grid[i, j] == 'x':
                replacements.append((i, j, int(min_grid[i, j])))

    return replacements

initial_grid = np.array([['x', 'x', '53', '62'],
                          ['x', '27', 'x', 'x'],
                          ['21', '22', 'x', '50'],
                          ['x', '20', '25', '44']])

solution = solve(initial_grid)
print(solution)
