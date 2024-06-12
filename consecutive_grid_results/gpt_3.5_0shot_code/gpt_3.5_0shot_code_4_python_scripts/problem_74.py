
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
    numbers = [str(i) for i in range(44, 89)]
    for perm in permutations(numbers, len(x_positions)):
        new_grid = grid.copy()
        for i, (x, y) in enumerate(x_positions):
            new_grid[x, y] = perm[i]
        if is_valid(new_grid):
            return new_grid

initial_grid = np.array([
    ['49', 'x', 'x', 'x'],
    ['x', '51', 'x', '84'],
    ['47', 'x', 'x', '79'],
    ['x', 'x', 'x', '77']
])

solution_grid = solve(initial_grid)

result = []
for i in range(4):
    for j in range(4):
        if initial_grid[i, j] == 'x':
            result.append((i, j, int(solution_grid[i, j])))

print(result)
