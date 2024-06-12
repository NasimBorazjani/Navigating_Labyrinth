
import numpy as np
from itertools import permutations

def is_valid(grid):
    for row in grid:
        if 'x' in row:
            continue
        if not (row[0] > row[1] > row[2] or row[0] < row[1] < row[2]):
            return False
    for col in grid.T:
        if 'x' in col:
            continue
        if not (col[0] > col[1] > col[2] or col[0] < col[1] < col[2]):
            return False
    return True

def calculate_sum(grid):
    diagonal_sum = sum([grid[i][i] for i in range(3)])
    top_row_sum = sum(grid[0])
    right_col_sum = sum(grid[:, 2])
    return diagonal_sum + top_row_sum + right_col_sum

def solve(grid):
    x_positions = [(i, j) for i in range(3) for j in range(3) if grid[i][j] == 'x']
    possible_values = [x for x in range(26, 74) if x not in grid]
    min_sum = float('inf')
    min_permutation = None

    for perm in permutations(possible_values):
        new_grid = grid.copy()
        for pos, val in zip(x_positions, perm):
            new_grid[pos[0]][pos[1]] = val
        if is_valid(new_grid):
            current_sum = calculate_sum(new_grid)
            if current_sum < min_sum:
                min_sum = current_sum
                min_permutation = new_grid

    result = []
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'x' and min_permutation[i][j] != 'x':
                result.append((i, j, min_permutation[i][j]))

    return result

initial_grid = np.array([[41, 'x', 'x'], [42, 57, 'x'], ['x', 'x', 'x']])
solution = solve(initial_grid)
print(solution)
