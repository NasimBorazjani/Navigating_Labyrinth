
import numpy as np
from itertools import permutations

def check_valid(grid):
    for i in range(3):
        row = grid[i]
        col = grid[:, i]
        if not (all(row[:-1] < row[1:]) or all(row[:-1] > row[1:])) or not (all(col[:-1] < col[1:]) or all(col[:-1] > col[1:])):
            return False
    return True

def calculate_sum(grid):
    diagonal_sum = np.trace(grid)
    top_row_sum = np.sum(grid[0])
    right_col_sum = np.sum(grid[:, 2])
    return diagonal_sum + top_row_sum + right_col_sum

def solve(grid):
    x_positions = np.argwhere(grid == 'x')
    possible_values = [str(i) for i in range(8, 41) if str(i) not in grid]
    min_sum = float('inf')
    min_permutation = None

    for perm in permutations(possible_values):
        new_grid = grid.copy()
        for i, (x, y) in enumerate(x_positions):
            new_grid[x, y] = perm[i]

        if check_valid(new_grid):
            current_sum = calculate_sum(new_grid)
            if current_sum < min_sum:
                min_sum = current_sum
                min_permutation = new_grid

    result = []
    for i, (x, y) in enumerate(x_positions):
        result.append((x, y, int(min_permutation[x, y])))

    return result

initial_grid = np.array([['10', '15', '39'],
                         ['x', '27', '29'],
                         ['x', 'x', 'x']])

solution = solve(initial_grid)
print(solution)
