
from itertools import permutations

# Define the grid
grid = [['x', 'x', 60, 63],
        [35, 'x', 'x', 'x'],
        ['x', 'x', 'x', 50],
        [34, 'x', 37, 'x']]

# Define the sums
col_sums = [None, 157, 200, None]
row_sums = [None, 193, 158, None]
diag_sum = 183

# Find the 'x' positions and the numbers already in the grid
x_positions = []
numbers = set(range(28, 65))
for i in range(4):
    for j in range(4):
        if grid[i][j] == 'x':
            x_positions.append((i, j))
        else:
            numbers.remove(grid[i][j])

# Try all permutations of the remaining numbers
for perm in permutations(numbers):
    # Fill the 'x' positions with the permutation
    for (i, j), num in zip(x_positions, perm):
        grid[i][j] = num
    # Check the sums
    if all(sum(grid[i][j] for j in range(4)) == row_sums[i] or row_sums[i] is None for i in range(4)) and \
       all(sum(grid[i][j] for i in range(4)) == col_sums[j] or col_sums[j] is None for j in range(4)) and \
       sum(grid[i][3-i] for i in range(4)) == diag_sum:
        # If the sums are correct, print the solution
        print([(i, j, grid[i][j]) for (i, j) in x_positions])
        break
