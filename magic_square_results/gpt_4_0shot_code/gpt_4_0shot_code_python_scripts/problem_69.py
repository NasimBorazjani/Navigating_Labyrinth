
from itertools import permutations

# Define the grid
grid = [['43', '65', 'x', 'x'],
        ['42', 'x', '59', 'x'],
        ['54', '45', 'x', 'x'],
        ['x', 'x', 'x', '35']]

# Define the sums
col_sums = [None, 205, 218, None]
row_sums = [None, 219, 220, None]
diag_sum = 182

# Convert the grid to integers and 'None' for 'x'
for i in range(4):
    for j in range(4):
        if grid[i][j] != 'x':
            grid[i][j] = int(grid[i][j])
        else:
            grid[i][j] = None

# Get the missing numbers
missing_nums = [i for i in range(31, 68) if i not in [j for sub in grid for j in sub if j is not None]]

# Get the possible permutations of the missing numbers
perms = permutations(missing_nums)

# Try each permutation
for perm in perms:
    temp_grid = [row[:] for row in grid]
    perm_index = 0

    # Fill in the missing numbers
    for i in range(4):
        for j in range(4):
            if temp_grid[i][j] is None:
                temp_grid[i][j] = perm[perm_index]
                perm_index += 1

    # Check the column sums
    for j in range(4):
        if col_sums[j] is not None and sum(temp_grid[i][j] for i in range(4)) != col_sums[j]:
            break
    else:
        # Check the row sums
        for i in range(4):
            if row_sums[i] is not None and sum(temp_grid[i]) != row_sums[i]:
                break
        else:
            # Check the diagonal sum
            if sum(temp_grid[i][3-i] for i in range(4)) == diag_sum:
                # If all constraints are satisfied, print the solution
                solution = [(i, j, temp_grid[i][j]) for i in range(4) for j in range(4) if grid[i][j] is None]
                print(solution)
                break
