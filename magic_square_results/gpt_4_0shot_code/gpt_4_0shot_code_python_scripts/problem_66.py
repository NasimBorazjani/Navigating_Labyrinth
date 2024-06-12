
from itertools import permutations

# Define the grid
grid = [['x', 'x', '64', 'x'],
        ['34', '54', 'x', 'x'],
        ['x', '56', '53', 'x'],
        ['36', 'x', 'x', '49']]

# Define the constraints
col_sums = [None, 217, 193, None]
row_sums = [None, 156, 208, None]
diag_sum = 166

# Find the 'x' positions and the numbers already in the grid
x_positions = []
numbers_in_grid = []
for i in range(4):
    for j in range(4):
        if grid[i][j] == 'x':
            x_positions.append((i, j))
        else:
            numbers_in_grid.append(int(grid[i][j]))

# Generate all possible numbers that can be in the grid
possible_numbers = [i for i in range(31, 68) if i not in numbers_in_grid]

# Generate all permutations of the possible numbers
perms = permutations(possible_numbers, len(x_positions))

# Check each permutation
for perm in perms:
    # Fill the grid with the permutation
    for (i, j), num in zip(x_positions, perm):
        grid[i][j] = num

    # Check the column sums
    if all(sum(grid[i][j] for i in range(4)) == col_sums[j] or col_sums[j] is None for j in range(4)):
        # Check the row sums
        if all(sum(grid[i][j] for j in range(4)) == row_sums[i] or row_sums[i] is None for i in range(4)):
            # Check the diagonal sum
            if sum(grid[i][3-i] for i in range(4)) == diag_sum:
                # If all constraints are satisfied, print the solution
                print([(i, j, grid[i][j]) for (i, j) in x_positions])
                break
