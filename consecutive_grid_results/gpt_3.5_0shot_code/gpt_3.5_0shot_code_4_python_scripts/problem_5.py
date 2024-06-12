
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
    possible_values = [str(i) for i in range(44, 77) if str(i) not in grid]
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

    return min_solution

initial_grid = np.array([['66', 'x', '74'],
                         ['x', '60', '62'],
                         ['x', 'x', 'x']])

solution_grid = solve(initial_grid)

solution = []
for i in range(3):
    for j in range(3):
        if initial_grid[i, j] == 'x':
            solution.append((i, j, int(solution_grid[i, j])))

print(solution)
