
from itertools import permutations

# Define the grid
grid = [['x', 'x', 'x', 'x'],
        ['x', '41', '17', 'x'],
        ['x', 'x', '13', '43'],
        ['9', '24', '27', '11']]

# Define the sums of columns and rows
col_sums = [None, 144, 76, None]
row_sums = [None, 116, 124, None]

# Define the sum of the diagonal
diag_sum = 75

# Define the range of numbers
numbers = [i for i in range(6, 48) if str(i) not in sum(grid, [])]

# Generate all permutations of the numbers
perms = permutations(numbers)

# Try each permutation
for perm in perms:
    # Fill the grid with the permutation
    filled_grid = [[int(grid[i][j]) if grid[i][j] != 'x' else perm.pop(0) for j in range(4)] for i in range(4)]
    
    # Check if the sums of columns, rows and diagonal are satisfied
    if all(sum(col) == col_sums[i] or col_sums[i] is None for i, col in enumerate(zip(*filled_grid))) and \
       all(sum(row) == row_sums[i] or row_sums[i] is None for i, row in enumerate(filled_grid)) and \
       sum(filled_grid[i][3-i] for i in range(4)) == diag_sum:
        # If all constraints are satisfied, print the solution
        solution = [(i, j, filled_grid[i][j]) for i in range(4) for j in range(4) if grid[i][j] == 'x']
        print(solution)
        break
