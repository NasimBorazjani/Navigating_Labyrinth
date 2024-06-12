
from itertools import permutations

# Define the grid
grid = [['x', 2], [3, 'x']]

# Define the sums of columns and rows
col_sums = [4, 3]
row_sums = [3, 4]

# Generate all possible permutations of the numbers 1 to 4
perms = list(permutations(range(1, 5)))

# Iterate over all permutations
for perm in perms:
    # Fill the grid with the current permutation
    filled_grid = [[perm[0], grid[0][1]], [grid[1][0], perm[1]]]
    # Check if the sums of columns and rows match the given sums
    if all(sum(row) == row_sum for row, row_sum in zip(filled_grid, row_sums)) and all(sum(col) == col_sum for col, col_sum in zip(zip(*filled_grid), col_sums)):
        # If they match, print the solution
        print(filled_grid)
