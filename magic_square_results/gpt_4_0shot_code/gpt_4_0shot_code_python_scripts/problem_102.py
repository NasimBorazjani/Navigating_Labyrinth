
from itertools import permutations

# Define the grid
grid = [[70, 'x', 50, 'x'],
        ['x', 39, 46, 'x'],
        [34, 60, 'x', 51],
        ['x', 'x', 'x', 68]]

# Define the sums
col_sums = [None, 260, 216, None]
row_sums = [None, 183, 217, None]
diag_sum = 214

# Find the 'x' positions and the remaining numbers
x_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
remaining_numbers = [n for n in range(30, 87) if n not in [num for row in grid for num in row if num != 'x']]

# Generate all possible permutations of the remaining numbers
perms = permutations(remaining_numbers)

# Try each permutation
for perm in perms:
    # Fill the 'x' positions with the current permutation
    for (i, j), num in zip(x_positions, perm):
        grid[i][j] = num
    # Check if the sums are correct
    if all(sum(grid[i][j] for j in range(4) if grid[i][j] != 'x') in [row_sums[i], sum(grid[i][j] for j in range(4))] for i in range(4)) and \
       all(sum(grid[i][j] for i in range(4) if grid[i][j] != 'x') in [col_sums[j], sum(grid[i][j] for i in range(4))] for j in range(4)) and \
       sum(grid[i][3-i] for i in range(4)) == diag_sum:
        # If the sums are correct, print the solution
        print([(i, j, grid[i][j]) for (i, j) in x_positions])
        break
