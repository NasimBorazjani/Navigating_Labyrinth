
import numpy as np

def solve_magic_square(grid, row_sums, col_sums, diag_sum, used_numbers):
    # Find an empty cell
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 'x':
                # Try to fill the cell with a number from the given range
                for num in range(24, 51):
                    if num not in used_numbers:
                        grid[i][j] = num
                        used_numbers.add(num)
                        # Check if the current grid satisfies the constraints
                        if check_constraints(grid, row_sums, col_sums, diag_sum):
                            # Recursively try to fill the next empty cell
                            if solve_magic_square(grid, row_sums, col_sums, diag_sum, used_numbers):
                                return True
                        # Backtrack
                        grid[i][j] = 'x'
                        used_numbers.remove(num)
                return False
    return True

def check_constraints(grid, row_sums, col_sums, diag_sum):
    # Check row sums
    for i in range(4):
        if row_sums[i] is not None and np.sum(grid[i]) != row_sums[i]:
            return False
    # Check column sums
    for j in range(4):
        if col_sums[j] is not None and np.sum(grid[:, j]) != col_sums[j]:
            return False
    # Check diagonal sum
    if np.sum(grid.diagonal()) != diag_sum:
        return False
    return True

# Initialize the grid
grid = np.array([['x', 'x', 40, 'x'],
                 ['x', 31, 'x', 43],
                 [37, 'x', 'x', 32],
                 [34, 29, 'x', 'x']], dtype=object)

# Initialize the row and column sums and the diagonal sum
row_sums = [None, 125, 164, None]
col_sums = [None, 135, 160, None]
diag_sum = 146

# Initialize the set of used numbers
used_numbers = set(grid[grid != 'x'])

# Solve the magic square
solve_magic_square(grid, row_sums, col_sums, diag_sum, used_numbers)

# Print the solution
for i in range(4):
    for j in range(4):
        if type(grid[i][j]) == int:
            print((i, j, grid[i][j]))
