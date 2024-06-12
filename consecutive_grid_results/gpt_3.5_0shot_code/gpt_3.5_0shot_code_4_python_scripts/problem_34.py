
import numpy as np
from itertools import permutations

def is_valid(grid):
    for row in grid:
        if 'x' in row:
            continue
        if not (row[0] < row[1] < row[2] or row[0] > row[1] > row[2]):
            return False
    for col in grid.T:
        if 'x' in col:
            continue
        if not (col[0] < col[1] < col[2] or col[0] > col[1] > col[2]):
            return False
    return True

def calculate_sum(grid):
    diagonal_sum = np.trace(grid)
    top_row_sum = np.sum(grid[0])
    right_col_sum = np.sum(grid[:, 2])
    return diagonal_sum + top_row_sum + right_col_sum

def solve(grid):
    x_positions = np.argwhere(grid == 'x')
    possible_values = [str(i) for i in range(38, 86) if str(i) not in grid]
    min_sum = float('inf')
    min_solution = None

    for perm in permutations(possible_values):
        new_grid = grid.copy()
        for i, (x, y) in enumerate(x_positions):
            new_grid[x, y] = perm[i]
        
        if is_valid(new_grid):
            current_sum = calculate_sum(new_grid)
            if current_sum < min_sum:
                min_sum = current_sum
                min_solution = new_grid

    solution = []
    for i, (x, y) in enumerate(x_positions):
        solution.append((x, y, int(min_solution[x, y])))

    return solution

initial_grid = np.array([['38', 'x', '77'],
                          ['x', 'x', 'x'],
                          ['x', '52', 'x']])

solution = solve(initial_grid)
print(solution)
