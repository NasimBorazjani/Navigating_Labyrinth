
from itertools import permutations

# Define the grid
grid = [['x', 'x', 32, 'x'],
        [37, 61, 'x', 54],
        ['x', 'x', 'x', 62],
        ['x', 30, 'x', 44]]

# Define the sums
col_sums = [None, 143, 170, None]
row_sums = [None, 211, 161, None]
diag_sum = 146

# Find the 'x' positions and the numbers already in the grid
x_positions = []
numbers_in_grid = []
for i in range(4):
    for j in range(4):
        if grid[i][j] == 'x':
            x_positions.append((i, j))
        else:
            numbers_in_grid.append(grid[i][j])

# Generate all possible numbers that can be in the grid
possible_numbers = [i for i in range(22, 69) if i not in numbers_in_grid]

# Generate all permutations of the possible numbers
perms = permutations(possible_numbers, len(x_positions))

# Check each permutation
for perm in perms:
    # Create a copy of the grid
    new_grid = [row[:] for row in grid]
    # Fill in the 'x' positions with the numbers in the permutation
    for (i, j), num in zip(x_positions, perm):
        new_grid[i][j] = num
    # Check the column sums
    if all(sum(new_grid[i][j] for i in range(4)) == col_sums[j] or col_sums[j] is None for j in range(4)):
        # Check the row sums
        if all(sum(new_grid[i]) == row_sums[i] or row_sums[i] is None for i in range(4)):
            # Check the diagonal sum
            if sum(new_grid[i][3-i] for i in range(4)) == diag_sum:
                # If all conditions are met, print the solution
                print([(i, j, new_grid[i][j]) for (i, j) in x_positions])
                break
