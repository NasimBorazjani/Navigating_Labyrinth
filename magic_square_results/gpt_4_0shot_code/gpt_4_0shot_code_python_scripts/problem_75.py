
import numpy as np

# Define the grid
grid = np.array([['x', 'x', 'x', 'x'],
                 ['28', '33', 'x', 'x'],
                 ['16', 'x', 'x', '37'],
                 ['36', '18', '7', '23']])

# Define the sums of columns and rows
col_sums = [None, 125, 51, None]
row_sums = [None, 101, 108, None]

# Define the sum of the diagonal
diag_sum = 90

# Define the range of unique integers
unique_ints = list(map(str, range(6, 48)))

# Remove the numbers already in the grid from the list of unique integers
for row in grid:
    for num in row:
        if num in unique_ints:
            unique_ints.remove(num)

# Define a function to check the validity of the grid
def is_valid(grid, row, col, num):
    # Check the column
    if col_sums[col] is not None:
        if np.sum([int(x) for x in grid[:, col] if x != 'x']) + num > col_sums[col]:
            return False

    # Check the row
    if row_sums[row] is not None:
        if np.sum([int(x) for x in grid[row, :] if x != 'x']) + num > row_sums[row]:
            return False

    # Check the diagonal
    if row == col:
        if np.sum([int(grid[i, i]) for i in range(4) if grid[i, i] != 'x']) + num > diag_sum:
            return False

    return True

# Define a function to solve the magic square problem
def solve_magic_square(grid):
    # Find the first 'x' in the grid
    for i in range(4):
        for j in range(4):
            if grid[i, j] == 'x':
                # Try all possible numbers
                for num in unique_ints:
                    num = int(num)
                    if is_valid(grid, i, j, num):
                        grid[i, j] = str(num)
                        unique_ints.remove(str(num))

                        if solve_magic_square(grid):
                            return True

                        # Undo the current cell for backtracking
                        grid[i, j] = 'x'
                        unique_ints.append(str(num))

                return False

    return True

# Solve the magic square problem
solve_magic_square(grid)

# Print the solution
solution = []
for i in range(4):
    for j in range(4):
        if grid[i, j] != 'x':
            solution.append((i, j, int(grid[i, j])))

print(solution)
