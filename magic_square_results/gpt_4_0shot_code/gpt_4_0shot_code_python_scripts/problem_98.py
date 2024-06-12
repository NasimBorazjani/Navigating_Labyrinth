
from itertools import permutations

# Define the grid
grid = [['x', 'x', 'x', 40],
        ['x', 'x', 'x', 'x'],
        [49, 61, 'x', 'x'],
        [33, 48, 'x', 54]]

# Define the sums
col_sums = [None, 259, 252, None]
row_sums = [None, 269, 234, None]
diag_sum = 178

# Define the range of numbers
numbers = list(range(33, 85))

# Remove the known numbers from the list
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
    # Check the sums
    if all(sum(row) == row_sums[i] or row_sums[i] is None for i, row in enumerate(temp_grid)) and \
       all(sum(temp_grid[j][i] for j in range(4)) == col_sums[i] or col_sums[i] is None for i in range(4)) and \
       sum(temp_grid[i][3-i] for i in range(4)) == diag_sum:
        # If the sums are correct, print the solution
        solution = [(row, col, temp_grid[row][col]) for row in range(4) for col in range(4) if grid[row][col] == 'x']
        print(solution)
        break
