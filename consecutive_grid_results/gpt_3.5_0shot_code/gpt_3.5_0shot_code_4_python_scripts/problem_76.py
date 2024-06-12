
import numpy as np
from itertools import permutations

def is_valid(grid):
    for row in grid:
        if 'x' in row:
            continue
        if any(row[i] >= row[i+1] for i in range(len(row)-1)) and any(row[i] <= row[i+1] for i in range(len(row)-1)):
            return False
    for col in grid.T:
        if 'x' in col:
            continue
        if any(col[i] >= col[i+1] for i in range(len(col)-1)) and any(col[i] <= col[i+1] for i in range(len(col)-1)):
            return False
    return True

def calculate_sum(grid):
    diagonal_sum = sum([grid[i][i] for i in range(4)])
    top_row_sum = sum(grid[0])
    right_col_sum = sum(grid[:,3])
    return diagonal_sum + top_row_sum + right_col_sum

def solve(grid):
    x_positions = np.argwhere(grid == 'x')
    possible_values = [i for i in range(28, 78) if i not in grid]
    min_sum = float('inf')
    min_permutation = None

    for perm in permutations(possible_values):
        new_grid = grid.copy()
        for i, (x_row, x_col) in enumerate(x_positions):
            new_grid[x_row][x_col] = perm[i]
        
        if is_valid(new_grid):
            current_sum = calculate_sum(new_grid)
            if current_sum < min_sum:
                min_sum = current_sum
                min_permutation = new_grid

    result = []
    for i, (x_row, x_col) in enumerate(x_positions):
        result.append((x_row, x_col, min_permutation[x_row][x_col]))

    return result

initial_grid = np.array([['x', '53', '60', '67'],
                          ['x', 'x', '72', 'x'],
                          ['50', '56', '74', 'x'],
                          ['54', '65', '76', 'x']])

solution = solve(initial_grid)
print(solution)
