
from itertools import permutations

# Define the grid
grid = [['x', 50, 'x', 'x'],
        [58, 'x', 'x', 'x'],
        ['x', 49, 'x', 59],
        [39, 41, 'x', 'x']]

# Define the sums of columns and rows
col_sums = [None, 177, 196, None]
row_sums = [None, 183, 190, None]

# Define the sum of the diagonal
diag_sum = 188

# Define the range of numbers
numbers = list(range(35, 62))

# Remove the numbers already in the grid from the list of numbers
for row in grid:
    for num in row:
        if num != 'x' and num in numbers:
            numbers.remove(num)

# Generate all possible permutations of the remaining numbers
perms = permutations(numbers)

# Try each permutation
for perm in perms:
    # Copy the grid
    grid_copy = [row.copy() for row in grid]
    # Fill the grid with the permutation
    i = 0
    for row in range(4):
        for col in range(4):
            if grid_copy[row][col] == 'x':
                grid_copy[row][col] = perm[i]
                i += 1
    # Check if the sums of the columns, rows and diagonal are correct
    if all(sum(row) == row_sums[i] or row_sums[i] is None for i, row in enumerate(grid_copy)) and \
       all(sum(grid_copy[i][j] for i in range(4)) == col_sums[j] or col_sums[j] is None for j in range(4)) and \
       sum(grid_copy[i][3-i] for i in range(4)) == diag_sum:
        # If the sums are correct, print the solution
        solution = [(row, col, grid_copy[row][col]) for row in range(4) for col in range(4) if grid[row][col] == 'x']
        print(solution)
        break
