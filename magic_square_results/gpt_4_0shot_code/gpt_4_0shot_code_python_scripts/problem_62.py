
from itertools import permutations

# Define the grid
grid = [['x', 'x', 'x', 'x'],
        [40, 39, 32, 53],
        [46, 'x', 58, 'x'],
        ['x', 'x', 43, 51]]

# Define the sums of columns and rows
col_sums = [None, 199, 194, None]
row_sums = [None, 164, 210, None]
diag_sum = 197

# Find the 'x' positions and the numbers already in the grid
x_positions = []
numbers = set(range(30, 67))
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
    # Check the sums of columns, rows and diagonal
    if all(sum(grid[i][j] for i in range(4)) in (col_sums[j], None) for j in range(4)) and \
       all(sum(grid[i][j] for j in range(4)) in (row_sums[i], None) for i in range(4)) and \
       sum(grid[i][3-i] for i in range(4)) == diag_sum:
        # If all conditions are met, print the solution
        print([(i, j, grid[i][j]) for i, j in x_positions])
        break
