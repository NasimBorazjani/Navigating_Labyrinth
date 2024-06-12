
from itertools import permutations

# Define the grid
grid = [[61, 'x', 50, 'x'],
        ['x', 'x', 'x', 'x'],
        [68, 40, 57, 'x'],
        ['x', 42, 'x', 'x']]

# Define the sums
col_sums = [None, 188, 234, None]
row_sums = [None, 247, 238, None]
diag_sum = 215

# Find the 'x's in the grid
xs = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']

# Generate all possible values for the 'x's
values = list(range(35, 77))
for row in grid:
    for value in row:
        if value != 'x' and value in values:
            values.remove(value)
value_perms = permutations(values, len(xs))

# Try all permutations of values
for perm in value_perms:
    # Fill in the 'x's with the current permutation
    for (i, j), value in zip(xs, perm):
        grid[i][j] = value

    # Check if the sums are correct
    if all(sum(grid[i][j] if grid[i][j] != 'x' else 0 for j in range(4)) == row_sums[i] or row_sums[i] is None for i in range(4)) and \
       all(sum(grid[i][j] if grid[i][j] != 'x' else 0 for i in range(4)) == col_sums[j] or col_sums[j] is None for j in range(4)) and \
       sum(grid[i][3-i] if grid[i][3-i] != 'x' else 0 for i in range(4)) == diag_sum:
        # If the sums are correct, print the solution
        print([(i, j, grid[i][j]) for i, j in xs])
        break
