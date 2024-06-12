
import numpy as np
from itertools import permutations

def is_valid(grid):
    for row in grid:
        if 'x' in row:
            continue
        if any(row[i] >= row[i+1] for i in range(len(row)-1)) and any(row[i] <= row[i+1] for i in range(len(row)-1)):
            return False
    for col in grid.T:
        if 'x' in col:
            continue
        if any(col[i] >= col[i+1] for i in range(len(col)-1)) and any(col[i] <= col[i+1] for i in range(len(col)-1)):
            return False
    return True

def calculate_sum(grid):
    diagonal_sum = sum([grid[i][i] for i in range(4)])
    top_row_sum = sum(grid[0])
    right_col_sum = sum(grid[:,3])
    return diagonal_sum + top_row_sum + right_col_sum

def solve(grid):
    x_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    min_sum = float('inf')
    best_solution = None

    for perm in permutations(range(25, 70)):
        new_grid = grid.copy()
        for pos, num in zip(x_positions, perm):
            new_grid[pos] = num
        if is_valid(new_grid):
            current_sum = calculate_sum(new_grid)
            if current_sum < min_sum:
                min_sum = current_sum
                best_solution = [(pos[0], pos[1], num) for pos, num in zip(x_positions, perm)]

    return best_solution

grid = np.array([['x', '40', 'x', '65'],
                 ['34', 'x', '53', 'x'],
                 ['x', 'x', 'x', '63'],
                 ['x', '56', 'x', '62']])

solution = solve(grid)
print(solution)
