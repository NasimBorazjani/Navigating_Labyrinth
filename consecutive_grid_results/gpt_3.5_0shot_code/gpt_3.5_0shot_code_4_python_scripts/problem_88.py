
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

def solve_grid():
    grid = np.array([
        ['x', 'x', 'x', '68'],
        ['x', '58', 'x', 'x'],
        ['41', 'x', 'x', 'x'],
        ['x', '66', '67', '79']
    ])

    possible_values = [i for i in range(30, 80) if i != 68 and i != 58 and i != 41 and i != 66 and i != 67 and i != 79]

    min_sum = float('inf')
    min_permutation = None

    for perm in permutations(possible_values):
        temp_grid = grid.copy()
        temp_grid[temp_grid == 'x'] = perm

        if check_valid(temp_grid):
            temp_sum = calculate_sum(temp_grid)
            if temp_sum < min_sum:
                min_sum = temp_sum
                min_permutation = temp_grid

    result = []
    for i in range(4):
        for j in range(4):
            if grid[i, j] == 'x':
                result.append((i, j, min_permutation[i, j]))

    return result

solution = solve_grid()
print(solution)
