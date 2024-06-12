
import numpy as np
from itertools import permutations

# Given grid
grid = np.array([[15, 20, 'x', 'x'],
                 [6, 'x', 'x', 40],
                 ['x', 'x', 29, 'x'],
                 [46, 42, 34, 'x']])

# Define the constraints
row_sums = [None, 97, 107, None]
col_sums = [None, 99, 126, None]
diagonal_sum = 124

# Generate all possible unique integers in the given range
possible_integers = [i for i in range(6, 48)]

# Generate all possible permutations of the integers to fill in the 'x' positions
permutations_x = permutations(possible_integers, np.sum(grid == 'x'))

# Function to check if a grid satisfies the constraints
def check_constraints(grid):
    if not all(np.sum(row) == sum_ if sum_ is not None else True for row, sum_ in zip(grid, row_sums)):
        return False
    if not all(np.sum(col) == sum_ if sum_ is not None else True for col, sum_ in zip(grid.T, col_sums)):
        return False
    if np.trace(grid) != diagonal_sum:
        return False
    return True

# Iterate through all permutations and check if they satisfy the constraints
solutions = []
for perm in permutations_x:
    new_grid = grid.copy()
    new_grid[new_grid == 'x'] = perm
    if check_constraints(new_grid):
        solution = [(i, j, perm[idx]) for idx, (i, j) in enumerate(zip(*np.where(grid == 'x')))]
        solutions.append(solution)

# Print the solution with the lowest sum of all numbers in the grid
min_sum = float('inf')
best_solution = None
for solution in solutions:
    sum_grid = sum([val for _, _, val in solution])
    if sum_grid < min_sum:
        min_sum = sum_grid
        best_solution = solution

print(best_solution)
