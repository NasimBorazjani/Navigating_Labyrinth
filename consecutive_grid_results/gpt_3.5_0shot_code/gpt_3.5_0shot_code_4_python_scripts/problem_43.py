
import numpy as np
from itertools import permutations

def is_valid(grid):
    for i in range(3):
        row = grid[i]
        col = grid[:, i]
        if not (np.all(np.diff(row) > 0) or np.all(np.diff(row) < 0) or np.all(np.isnan(row))):
            return False
        if not (np.all(np.diff(col) > 0) or np.all(np.diff(col) < 0) or np.all(np.isnan(col))):
            return False
    return True

def calculate_sum(grid):
    diagonal_sum = np.sum(np.diag(grid))
    top_row_sum = np.sum(grid[0, :])
    right_col_sum = np.sum(grid[:, 2])
    return diagonal_sum + top_row_sum + right_col_sum

def solve(grid):
    x_positions = np.argwhere(grid == 'x')
    numbers = [str(i) for i in range(7, 60)]
    min_sum = float('inf')
    min_perm = None

    for perm in permutations(numbers, len(x_positions)):
        temp_grid = grid.copy()
        for i, (x, y) in enumerate(x_positions):
            temp_grid[x, y] = perm[i]
        
        if is_valid(temp_grid):
            current_sum = calculate_sum(temp_grid)
            if current_sum < min_sum:
                min_sum = current_sum
                min_perm = temp_grid.copy()

    result = []
    for i, (x, y) in enumerate(x_positions):
        result.append((x, y, int(min_perm[x, y])))

    return result

initial_grid = np.array([['13', 'x', 'x'],
                          ['x', 'x', '27'],
                          ['x', '26', 'x']])

solution = solve(initial_grid)
print(solution)
