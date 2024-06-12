
from itertools import permutations

# Define the grid
grid = [['x', 46, 'x', 22],
        ['x', 'x', 36, 15],
        [47, 'x', 'x', 25],
        ['x', 'x', 53, 'x']]

# Define the sums
col_sums = [None, 146, 168, None]
row_sums = [None, 118, 120, None]
diag_sum = 91

# Find the 'x' positions and the numbers already in the grid
x_positions = []
numbers_in_grid = []
for i in range(4):
    for j in range(4):
        if grid[i][j] == 'x':
            x_positions.append((i, j))
        else:
            numbers_in_grid.append(grid[i][j])

# Generate the possible numbers to fill the grid
possible_numbers = [i for i in range(13, 55) if i not in numbers_in_grid]

# Generate all permutations of the possible numbers
perms = permutations(possible_numbers, len(x_positions))

# Check each permutation
for perm in perms:
    # Fill the grid with the current permutation
    for (i, j), num in zip(x_positions, perm):
        grid[i][j] = num

    # Check the column sums
    if all(sum(grid[i][j] for i in range(4)) == col_sums[j] or col_sums[j] is None for j in range(4)):
        # Check the row sums
        if all(sum(grid[i][j] for j in range(4)) == row_sums[i] or row_sums[i] is None for i in range(4)):
            # Check the diagonal sum
            if sum(grid[i][3-i] for i in range(4)) == diag_sum:
                # If all conditions are met, print the solution
                print([(i, j, grid[i][j]) for (i, j) in x_positions])
                break
