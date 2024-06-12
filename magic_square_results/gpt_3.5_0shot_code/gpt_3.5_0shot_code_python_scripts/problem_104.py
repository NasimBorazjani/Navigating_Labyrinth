
import numpy as np
from itertools import permutations

def check_sums(grid):
    row_sums = [None, 234, 271, None]
    col_sums = [None, 295, 200, None]
    diag_sum = 248

    for i in range(4):
        if row_sums[i] is not None and sum(grid[i]) != row_sums[i]:
            return False
        if col_sums[i] is not None and sum(grid[:, i]) != col_sums[i]:
            return False

    if np.trace(grid) != diag_sum:
        return False

    if sum(grid.flatten()) != sum(range(36, 93)):
        return False

    return True

def solve_magic_square():
    grid = np.array([[39, 47, 'x', 'x'],
                     ['x', 'x', 'x', 40],
                     [63, 82, 59, 'x'],
                     ['x', 78, 'x', 'x']])

    unknown_indices = [(i, j) for i in range(4) for j in range(4) if grid[i, j] == 'x']

    possible_values = [x for x in range(36, 93) if x not in grid]

    for perm in permutations(possible_values, len(unknown_indices)):
        temp_grid = grid.copy()
        for idx, val in zip(unknown_indices, perm):
            temp_grid[idx] = val

        if check_sums(temp_grid):
            solution = [(idx[0], idx[1], val) for idx, val in zip(unknown_indices, perm)]
            return solution

    return None

solution = solve_magic_square()
print(solution)
