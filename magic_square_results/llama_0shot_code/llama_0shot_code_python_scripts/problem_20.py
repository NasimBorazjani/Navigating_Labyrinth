
from itertools import permutations

# The initial grid with 'x' values
grid = [['62', '82', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]

# The given sums for rows and columns
row_sums = [207, 233, 185]
col_sums = [233, 207, 185]

# The range of numbers to fill in the grid
num_range = range(50, 85)

# Generate all possible permutations of numbers within the range
perms = permutations(num_range, 3)

# To store the results
results = []

# For each permutation
for perm in perms:
    # Create a copy of the grid
    new_grid = [row.copy() for row in grid]
    # Replace the 'x' values with the numbers from the permutation
    new_grid[0][2] = perm[0]
    new_grid[1][0] = perm[1]
    new_grid[1][1] = perm[2]
    new_grid[2][0] = perm[2]
    new_grid[2][1] = perm[1]
    new_grid[2][2] = perm[0]
    # Check whether the sums match the given amounts
    if (sum(int(num) for num in new_grid[0]) == row_sums[0] and
            sum(int(num) for num in new_grid[1]) == row_sums[1] and
            sum(int(num) for num in new_grid[2]) == row_sums[2] and
            sum(new_grid[i][i] for i in range(3)) == col_sums[0] and
            sum(new_grid[i][2 - i] for i in range(3)) == col_sums[1]):
        # If they do, add this configuration to the results
        results.append(perm)

# Print the results
print(results)
