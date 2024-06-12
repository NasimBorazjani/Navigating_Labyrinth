
from itertools import permutations

# Define the grid
grid = [['x', 51, 39, 'x'],
        ['x', 'x', 48, 37],
        [54, 'x', 'x', 'x'],
        ['x', 'x', 'x', 53]]

# Define the sums of rows, columns, and diagonal
row_sums = [None, 180, 202, None]
col_sums = [None, 212, 185, None]
diag_sum = 193

# Find all 'x' positions and existing numbers
x_positions = []
existing_numbers = []
for i in range(4):
    for j in range(4):
        if grid[i][j] == 'x':
            x_positions.append((i, j))
        else:
            existing_numbers.append(grid[i][j])

# Generate all possible numbers that can replace 'x'
possible_numbers = [i for i in range(35, 62) if i not in existing_numbers]

# Generate all permutations of possible numbers
perms = permutations(possible_numbers, len(x_positions))

# Check each permutation
for perm in perms:
    # Replace 'x' with numbers in the permutation
    for (i, j), num in zip(x_positions, perm):
        grid[i][j] = num
    # Check if the sums of rows, columns, and diagonal are correct
    if all(sum(row) == row_sum for row, row_sum in zip(grid, row_sums) if row_sum is not None) and \
       all(sum(col) == col_sum for col, col_sum in zip(zip(*grid), col_sums) if col_sum is not None) and \
       sum(grid[i][3-i] for i in range(4)) == diag_sum:
        # If the sums are correct, print the solution
        print([(i, j, grid[i][j]) for i, j in x_positions])
        break
