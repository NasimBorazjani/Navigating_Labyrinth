
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
    numbers = [str(num) for num in range(23, 73) if str(num) not in grid]
    perms = permutations(numbers, len(x_positions))

    min_sum = float('inf')
    min_grid = None

    for perm in perms:
        temp_grid = np.copy(grid)
        for i, (x_pos, num) in enumerate(zip(x_positions, perm)):
            temp_grid[x_pos[0], x_pos[1]] = num
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

initial_grid = np.array([['x', '35', 'x', 'x'],
                          ['34', '36', '38', 'x'],
                          ['29', 'x', '43', 'x'],
                          ['x', 'x', '49', '53']])

solution = solve(initial_grid)
print(solution)
