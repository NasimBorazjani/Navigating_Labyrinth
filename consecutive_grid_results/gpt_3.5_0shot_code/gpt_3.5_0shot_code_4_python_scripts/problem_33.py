
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

def solve_grid():
    grid = np.array([[79, 63, 43], [0, 68, 0], [0, 0, 0]])
    min_sum = float('inf')
    min_grid = None

    for perm in permutations(range(41, 89), 6):
        grid[1, 0] = perm[0]
        grid[1, 2] = perm[1]
        grid[2, 0] = perm[2]
        grid[2, 1] = perm[3]
        grid[2, 2] = perm[4]

        if is_valid(grid):
            current_sum = calculate_sum(grid)
            if current_sum < min_sum:
                min_sum = current_sum
                min_grid = np.copy(grid)

    replacements = []
    for i in range(3):
        for j in range(3):
            if min_grid[i, j] == 0:
                replacements.append((i, j, min_grid[i-1, j]))

    return replacements

solution = solve_grid()
print(solution)
