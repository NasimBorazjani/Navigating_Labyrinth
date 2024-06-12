
from itertools import permutations

# Define the grid
grid = [['x', 65, 49, 35],
        [40, 'x', 52, 'x'],
        ['x', 'x', 34, 'x'],
        ['x', 'x', 55, 61]]

# Define the sums
col_sums = [None, 191, 190, None]
row_sums = [None, 192, 173, None]
diag_sum = 180

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

    # Check the column sums
    if all(sum(grid[i][j] for i in range(4)) == col_sums[j] or col_sums[j] is None for j in range(4)):
        # Check the row sums
        if all(sum(grid[i]) == row_sums[i] or row_sums[i] is None for i in range(4)):
            # Check the diagonal sum
            if sum(grid[i][3 - i] for i in range(4)) == diag_sum:
                # If all constraints are satisfied, print the solution
                print([(i, j, grid[i][j]) for (i, j) in x_positions])
                break
