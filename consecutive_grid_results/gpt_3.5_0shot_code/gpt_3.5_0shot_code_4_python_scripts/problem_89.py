
import numpy as np
from itertools import permutations

def is_valid(grid):
    for i in range(4):
        row = grid[i]
        col = grid[:, i]
        if not (all(row[0] < row[i] for i in range(1, 4)) or all(row[0] > row[i] for i in range(1, 4)):
            return False
        if not (all(col[0] < col[i] for i in range(1, 4)) or all(col[0] > col[i] for i in range(1, 4)):
            return False
    return True

def calculate_sum(grid):
    diagonal_sum = sum([grid[i][i] for i in range(4)])
    top_row_sum = sum(grid[0])
    right_col_sum = sum(grid[:, 3])
    return diagonal_sum + top_row_sum + right_col_sum

def solve(grid):
    x_positions = np.argwhere(grid == 'x')
    numbers = [str(i) for i in range(10, 60)]
    min_sum = float('inf')
    min_permutation = None

    for perm in permutations(numbers, len(x_positions)):
        temp_grid = grid.copy()
        for i, (x, y) in enumerate(x_positions):
            temp_grid[x][y] = perm[i]

        if is_valid(temp_grid):
            current_sum = calculate_sum(temp_grid)
            if current_sum < min_sum:
                min_sum = current_sum
                min_permutation = temp_grid

    result = []
    for i, (x, y) in enumerate(x_positions):
        result.append((x, y, int(min_permutation[x][y])))

    return result

initial_grid = np.array([['x', '33', '34', '47'],
                         ['x', 'x', 'x', '50'],
                         ['x', 'x', 'x', '52'],
                         ['x', 'x', 'x', '53']])

solution = solve(initial_grid)
print(solution)
