
from itertools import permutations

# Define the grid
grid = [['x', 'x'],
        ['x', 'x']]

# Define the sums of the rows and columns
row_sums = [None, 7]
col_sums = [None, 7]

# Generate all possible permutations of the numbers 1 to 4
perms = list(permutations(range(1, 5)))

# Iterate over all permutations
for perm in perms:
    # Fill the grid with the current permutation
    for i in range(2):
        for j in range(2):
            grid[i][j] = perm[i*2 + j]
    # Check if the sums of the rows and columns match the given sums
    if all(sum(row) == row_sums[i] for i, row in enumerate(grid)) and all(sum(col) == col_sums[i] for i, col in enumerate(zip(*grid))):
        # If they match, print the solution and break the loop
        print(grid)
        break
