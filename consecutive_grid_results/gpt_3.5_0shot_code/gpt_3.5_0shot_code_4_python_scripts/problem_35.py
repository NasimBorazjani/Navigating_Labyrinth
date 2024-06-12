
import numpy as np
from itertools import permutations

def is_valid(grid):
    for i in range(3):
        row = grid[i]
        col = grid[:, i]
        if not (all(row[0] < row[1] < row[2]) or all(row[0] > row[1] > row[2])):
            return False
        if not (all(col[0] < col[1] < col[2]) or all(col[0] > col[1] > col[2])):
            return False
    return True

def calculate_sum(grid):
    diagonal_sum = grid[0, 0] + grid[1, 1] + grid[2, 2]
    top_row_sum = np.sum(grid[0, :])
    right_col_sum = np.sum(grid[:, 2])
    return diagonal_sum + top_row_sum + right_col_sum

def solve(grid):
    x_positions = np.argwhere(grid == 'x')
    numbers = [i for i in range(40, 88)]
    min_sum = float('inf')
    min_grid = None

    for perm in permutations(numbers, len(x_positions)):
        new_grid = grid.copy()
        for i, (x, y) in enumerate(x_positions):
            new_grid[x, y] = perm[i]
        
        if is_valid(new_grid):
            current_sum = calculate_sum(new_grid)
            if current_sum < min_sum:
                min_sum = current_sum
                min_grid = new_grid.copy()
    
    result = []
    for i, (x, y) in enumerate(x_positions):
        result.append((x, y, min_grid[x, y]))
    
    return result

initial_grid = np.array([['x', 'x', 'x'],
                          ['x', '61', '62'],
                          ['x', 'x', '63']])

solution = solve(initial_grid)
print(solution)
