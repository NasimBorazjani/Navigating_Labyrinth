
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
    numbers = [str(i) for i in range(33, 78)]
    for perm in permutations(numbers, len(x_positions)):
        new_grid = grid.copy()
        for i, (x, y) in enumerate(x_positions):
            new_grid[x, y] = perm[i]
        if is_valid(new_grid):
            return new_grid

initial_grid = np.array([
    ['x', '58', 'x', 'x'],
    ['x', 'x', 'x', '70'],
    ['x', '48', '52', 'x'],
    ['x', '43', 'x', '67']
])

solution_grid = solve(initial_grid)
print(solution_grid)

solution = []
for i in range(4):
    for j in range(4):
        if initial_grid[i, j] == 'x':
            solution.append((i, j, int(solution_grid[i, j])))

print(solution)
