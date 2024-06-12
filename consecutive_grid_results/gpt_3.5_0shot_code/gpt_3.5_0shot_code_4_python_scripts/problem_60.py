
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
    diagonal_sum = sum([grid[i][i] for i in range(4)])
    top_row_sum = sum([int(grid[0][i]) for i in range(4) if grid[0][i] != 'x'])
    right_col_sum = sum([int(grid[i][3]) for i in range(4) if grid[i][3] != 'x'])
    return diagonal_sum + top_row_sum + right_col_sum

def solve(grid):
    x_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    numbers = [str(num) for num in range(24, 64) if str(num) not in grid]
    min_sum = float('inf')
    min_permutation = None

    for perm in permutations(numbers):
        new_grid = np.copy(grid)
        for (i, j), num in zip(x_positions, perm):
            new_grid[i][j] = num
        if is_valid(new_grid):
            current_sum = calculate_sum(new_grid)
            if current_sum < min_sum:
                min_sum = current_sum
                min_permutation = new_grid

    result = []
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 'x' and min_permutation[i][j] != 'x':
                result.append((i, j, int(min_permutation[i][j])))

    return result

initial_grid = np.array([['x', 'x', 'x', 'x'],
                         ['37', 'x', '49', 'x'],
                         ['x', '44', 'x', 'x'],
                         ['42', 'x', '51', '61']])

solution = solve(initial_grid)
print(solution)
