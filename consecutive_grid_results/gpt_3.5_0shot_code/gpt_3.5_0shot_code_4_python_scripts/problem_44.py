
import numpy as np
from itertools import permutations

def is_valid(grid):
    for row in grid:
        if 'x' in row:
            continue
        if not (all(row[i] < row[i+1] for i in range(len(row)-1)) or all(row[i] > row[i+1] for i in range(len(row)-1))):
            return False
    for col in grid.T:
        if 'x' in col:
            continue
        if not (all(col[i] < col[i+1] for i in range(len(col)-1)) or all(col[i] > col[i+1] for i in range(len(col)-1))):
            return False
    return True

def calculate_sum(grid):
    diagonal_sum = sum([grid[i][i] for i in range(3)])
    top_row_sum = sum(grid[0])
    right_col_sum = sum(grid[:,2])
    return diagonal_sum + top_row_sum + right_col_sum

def solve(grid):
    x_positions = np.argwhere(grid == 'x')
    numbers = [i for i in range(31, 84)]
    min_sum = float('inf')
    min_perm = None
    for perm in permutations(numbers, len(x_positions)):
        temp_grid = grid.copy()
        for i, (x, y) in enumerate(x_positions):
            temp_grid[x][y] = perm[i]
        if is_valid(temp_grid):
            current_sum = calculate_sum(temp_grid)
            if current_sum < min_sum:
                min_sum = current_sum
                min_perm = temp_grid
    result = []
    for i, (x, y) in enumerate(x_positions):
        result.append((x, y, min_perm[x][y]))
    return result

initial_grid = np.array([['x', '58', 'x'],
                          ['42', 'x', '70'],
                          ['x', 'x', 'x']])

solution = solve(initial_grid)
print(solution)
