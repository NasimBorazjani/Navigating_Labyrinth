
from itertools import permutations

# Define the grid
grid = [[46, 30, 'x', 49],
        [43, 'x', 'x', 53],
        ['x', 'x', 37, 'x'],
        ['x', 34, 33, 'x']]

# Define the sums
col_sums = [None, 154, 157, None]
row_sums = [None, 173, 194, None]
diag_sum = 208

# Get the 'x' positions and the available numbers
x_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
available_numbers = [n for n in range(30, 67) if n not in [grid[i][j] for i in range(4) for j in range(4) if grid[i][j] != 'x']]

# Try all permutations of the available numbers
for perm in permutations(available_numbers):
    # Fill the 'x' positions with the current permutation
    for (i, j), n in zip(x_positions, perm):
        grid[i][j] = n
    # Check the column sums
    if all(sum(grid[i][j] for i in range(4)) == col_sums[j] for j in range(4) if col_sums[j] is not None):
        # Check the row sums
        if all(sum(grid[i][j] for j in range(4)) == row_sums[i] for i in range(4) if row_sums[i] is not None):
            # Check the diagonal sum
            if sum(grid[i][3-i] for i in range(4)) == diag_sum:
                # If all constraints are satisfied, print the solution and break
                print([(i, j, grid[i][j]) for i, j in x_positions])
                break
