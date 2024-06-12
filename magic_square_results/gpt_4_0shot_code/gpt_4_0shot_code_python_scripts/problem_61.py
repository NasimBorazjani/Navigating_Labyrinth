
from itertools import permutations

# Define the grid
grid = [['x', 31, 'x', 'x'],
        ['x', 'x', 'x', 'x'],
        ['x', 'x', 42, 'x'],
        ['x', 49, 30, 27]]

# Define the sums
col_sums = [None, 135, 149, None]
row_sums = [None, 156, 156, None]
diag_sum = 149

# Define the range of numbers
numbers = list(range(23, 55))

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
    if all(sum(temp_grid[row]) == row_sums[row] or row_sums[row] is None for row in range(4)) and \
       all(sum(temp_grid[col][row] for col in range(4)) == col_sums[row] or col_sums[row] is None for row in range(4)) and \
       sum(temp_grid[i][3-i] for i in range(4)) == diag_sum:
        # If the sums are correct, print the solution
        solution = [(row, col, temp_grid[row][col]) for row in range(4) for col in range(4) if grid[row][col] == 'x']
        print(solution)
        break
