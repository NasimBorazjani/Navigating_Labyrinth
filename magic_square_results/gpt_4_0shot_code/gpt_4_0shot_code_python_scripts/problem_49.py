
from itertools import permutations

# Define the grid
grid = [[37, 'x', 'x', 56],
        [52, 'x', 'x', 'x'],
        ['x', 50, 'x', 'x'],
        ['x', 'x', 'x', 46]]

# Define the sums
col_sums = [None, 165, 155, None]
row_sums = [None, 169, 190, None]
diag_sum = 201

# Define the range of possible values
values = list(range(34, 61))

# Remove the known values from the possible values
for row in grid:
    for value in row:
        if value != 'x' and value in values:
            values.remove(value)

# Generate all permutations of the possible values
perms = permutations(values)

# Try each permutation
for perm in perms:
    # Copy the grid and the permutation
    grid_copy = [row.copy() for row in grid]
    perm_copy = list(perm)

    # Fill in the 'x's with the permutation
    for i in range(4):
        for j in range(4):
            if grid_copy[i][j] == 'x':
                grid_copy[i][j] = perm_copy.pop(0)

    # Check the column sums
    for j in range(4):
        if col_sums[j] is not None and sum(grid_copy[i][j] for i in range(4)) != col_sums[j]:
            break
    else:
        # Check the row sums
        for i in range(4):
            if row_sums[i] is not None and sum(grid_copy[i]) != row_sums[i]:
                break
        else:
            # Check the diagonal sum
            if sum(grid_copy[i][3-i] for i in range(4)) == diag_sum:
                # If all constraints are satisfied, print the solution
                solution = [(i, j, grid_copy[i][j]) for i in range(4) for j in range(4) if grid[i][j] == 'x']
                print(solution)
                break
