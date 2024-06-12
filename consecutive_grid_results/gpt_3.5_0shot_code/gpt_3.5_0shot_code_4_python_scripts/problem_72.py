
import numpy as np
from itertools import permutations

def is_valid(grid):
    for row in grid:
        if 'x' in row:
            continue
        if not all(row[i] < row[i+1] for i in range(len(row)-1)) and not all(row[i] > row[i+1] for i in range(len(row)-1)):
            return False
    for col in grid.T:
        if 'x' in col:
            continue
        if not all(col[i] < col[i+1] for i in range(len(col)-1)) and not all(col[i] > col[i+1] for i in range(len(col)-1)):
            return False
    return True

def calculate_sum(grid):
    diagonal_sum = np.trace(grid)
    top_row_sum = np.sum(grid[0])
    right_col_sum = np.sum(grid[:,-1])
    return diagonal_sum + top_row_sum + right_col_sum

def solve(grid):
    x_positions = np.argwhere(grid == 'x')
    numbers = [str(i) for i in range(9, 54) if str(i) not in grid]
    min_sum = float('inf')
    min_permutation = None

    for perm in permutations(numbers):
        temp_grid = grid.copy()
        for i, (x_row, x_col) in enumerate(x_positions):
            temp_grid[x_row, x_col] = perm[i]
        
        if is_valid(temp_grid):
            temp_sum = calculate_sum(temp_grid)
            if temp_sum < min_sum:
                min_sum = temp_sum
                min_permutation = temp_grid.copy()

    result = []
    for i, (x_row, x_col) in enumerate(x_positions):
        result.append((x_row, x_col, int(min_permutation[x_row, x_col])))

    return result

initial_grid = np.array([['24', 'x', 'x', '53'],
                          ['25', '31', 'x', 'x'],
                          ['26', '29', '31', 'x'],
                          ['x', 'x', 'x', 'x']])

solution = solve(initial_grid)
print(solution)
