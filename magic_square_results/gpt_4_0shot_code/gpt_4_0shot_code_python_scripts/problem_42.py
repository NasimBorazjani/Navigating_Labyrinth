
from itertools import permutations

# Define the grid
grid = [['x', 42, 'x', 'x'],
        ['x', 38, 'x', 'x'],
        ['x', 36, 46, 'x'],
        [49, 25, 24, 'x']]

# Define the sums of columns and rows
col_sums = [None, 141, 134, None]
row_sums = [None, 133, 150, None]

# Define the sum of the diagonal
diag_sum = 155

# Define the range of unique integers
numbers = list(set(range(24, 51)) - set([42, 38, 36, 46, 49, 25, 24]))

# Generate all permutations of the numbers
perms = permutations(numbers)

# Try each permutation
for perm in perms:
    # Fill the grid with the permutation
    k = 0
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 'x':
                grid[i][j] = perm[k]
                k += 1

    # Check the sums of columns and rows
    if all(sum(grid[i][j] for i in range(4)) == col_sums[j] or col_sums[j] is None for j in range(4)) and \
       all(sum(grid[i][j] for j in range(4)) == row_sums[i] or row_sums[i] is None for i in range(4)) and \
       sum(grid[i][3-i] for i in range(4)) == diag_sum:
        # If the sums are correct, print the solution
        solution = [(i, j, grid[i][j]) for i in range(4) for j in range(4) if isinstance(grid[i][j], int)]
        print(solution)
        break

    # If the sums are not correct, reset the grid
    k = 0
    for i in range(4):
        for j in range(4):
            if not isinstance(grid[i][j], int):
                grid[i][j] = 'x'
