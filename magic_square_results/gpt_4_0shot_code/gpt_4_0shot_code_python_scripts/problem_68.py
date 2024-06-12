
from itertools import permutations

# Define the grid
grid = [['x', 40, 'x', 'x'],
        ['x', 58, 'x', 37],
        [47, 'x', 'x', 44],
        [45, 'x', 'x', 42]]

# Define the sums of columns and rows
col_sums = [None, 224, 226, None]
row_sums = [None, 220, 216, None]

# Define the sum of the diagonal
diag_sum = 211

# Define the range of numbers
numbers = list(range(31, 68))

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
    temp_grid = [row[:] for row in grid]
    
    # Fill the grid with the permutation
    i = 0
    for row in range(4):
        for col in range(4):
            if temp_grid[row][col] == 'x':
                temp_grid[row][col] = perm[i]
                i += 1
    
    # Check the sums of the columns
    for col in range(4):
        if col_sums[col] is not None and sum(temp_grid[row][col] for row in range(4)) != col_sums[col]:
            break
    else:
        # Check the sums of the rows
        for row in range(4):
            if row_sums[row] is not None and sum(temp_grid[row]) != row_sums[row]:
                break
        else:
            # Check the sum of the diagonal
            if sum(temp_grid[i][3-i] for i in range(4)) == diag_sum:
                # If all constraints are satisfied, print the solution
                solution = [(row, col, temp_grid[row][col]) for row in range(4) for col in range(4) if grid[row][col] == 'x']
                print(solution)
                break
