
from itertools import permutations

# Define the grid
grid = [['x', 'x', 27, 9],
        [21, 'x', 'x', 15],
        ['x', 16, 31, 'x'],
        [11, 'x', 32, 'x']]

# Define the sums of the columns and rows
col_sums = [None, 102, 100, None]
row_sums = [None, 72, 97, None]

# Define the sum of the diagonal
diag_sum = 46

# Define the range of numbers
numbers = list(range(9, 41))

# Remove the numbers already in the grid from the list of numbers
for row in grid:
    for num in row:
        if num != 'x' and num in numbers:
            numbers.remove(num)

# Generate all permutations of the remaining numbers
perms = permutations(numbers)

# Try each permutation
for perm in perms:
    # Copy the grid
    temp_grid = [row.copy() for row in grid]
    
    # Fill the grid with the permutation
    i = 0
    for row in range(4):
        for col in range(4):
            if temp_grid[row][col] == 'x':
                temp_grid[row][col] = perm[i]
                i += 1
    
    # Check if the sums of the columns, rows and diagonal are correct
    if all(sum(temp_grid[row]) == row_sums[row] or row_sums[row] is None for row in range(4)) and \
       all(sum(temp_grid[col][row] for col in range(4)) == col_sums[row] or col_sums[row] is None for row in range(4)) and \
       sum(temp_grid[i][3-i] for i in range(4)) == diag_sum:
        # If the grid is correct, print it and break the loop
        print(temp_grid)
        break
