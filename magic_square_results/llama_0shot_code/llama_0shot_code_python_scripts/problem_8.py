
from itertools import permutations

def solve_magic_square(grid, row_sums, col_sums, diag_sum):
    # Generate all permutations of numbers in the given range
    nums = list(range(35, 60))
    perms = permutations(nums, len(grid)*len(grid[0]))

    # Initialize the result set
    results = []

    # For each permutation
    for perm in perms:
        # Create a copy of the grid
        new_grid = [row.copy() for row in grid]

        # Place the numbers in the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'x':
                    new_grid[i][j] = perm.pop(0)

        # Calculate the sum of each row, column, and diagonal
        row_sums_new = [sum(row) for row in new_grid]
        col_sums_new = [sum(new_grid[i][j] for i in range(len(new_grid))) for j in range(len(new_grid[0]))]
        diag_sum_new = sum(new_grid[i][i] for i in range(len(new_grid))) \
                     + sum(new_grid[i][len(new_grid)-1-i] for i in range(len(new_grid)))

        # If the sums match the given amounts
        if row_sums_new == row_sums and col_sums_new == col_sums and diag_sum_new == diag_sum:
            # Add the permutation to the result set
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 'x':
                        results.append((i, j, new_grid[i][j]))

    return results

# The initial grid
grid = [['52', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]

# The given row, column, and diagonal sums
row_sums = [144]
col_sums = [130]
diag_sum = 123

# Call the function to solve the magic square
result = solve_magic_square(grid, row_sums, col_sums, diag_sum)

# Print the result
print(result)
