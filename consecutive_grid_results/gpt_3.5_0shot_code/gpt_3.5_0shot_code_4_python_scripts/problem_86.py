
import numpy as np
from itertools import permutations

def check_valid(grid):
    for i in range(4):
        row = grid[i]
        col = grid[:, i]
        if not (all(row[0] > row[1] > row[2] > row[3]) or all(row[0] < row[1] < row[2] < row[3])):
            return False
        if not (all(col[0] > col[1] > col[2] > col[3]) or all(col[0] < col[1] < col[2] < col[3])):
            return False
    return True

def calculate_sum(grid):
    diagonal_sum = sum([grid[i][i] for i in range(4)])
    top_row_sum = sum(grid[0])
    right_col_sum = sum(grid[:, 3])
    return diagonal_sum + top_row_sum + right_col_sum

def solve(grid):
    x_positions = np.argwhere(grid == 'x')
    numbers = list(range(6, 56))
    min_sum = float('inf')
    min_permutation = None

    for perm in permutations(numbers, len(x_positions)):
        temp_grid = grid.copy()
        for i, (x_row, x_col) in enumerate(x_positions):
            temp_grid[x_row][x_col] = perm[i]
        
        if check_valid(temp_grid):
            temp_sum = calculate_sum(temp_grid)
            if temp_sum < min_sum:
                min_sum = temp_sum
                min_permutation = temp_grid.copy()

    result = []
    for i, (x_row, x_col) in enumerate(x_positions):
        result.append((x_row, x_col, min_permutation[x_row][x_col]))

    return result

initial_grid = np.array([['x', 'x', 'x', '54'],
                          ['x', 'x', '44', '53'],
                          ['x', '17', 'x', 'x'],
                          ['18', '22', '36', 'x']])

solution = solve(initial_grid)
print(solution)
