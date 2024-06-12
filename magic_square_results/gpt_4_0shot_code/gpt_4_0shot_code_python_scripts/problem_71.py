
import numpy as np

# Define the grid
grid = np.array([[55, 'x', 53, 'x'],
                 ['x', 50, 52, 'x'],
                 ['x', 'x', 'x', 35],
                 ['x', 62, 'x', 'x']])

# Define the constraints
row_sums = [None, 186, 174, None]
col_sums = [None, 218, 203, None]
diag_sum = 221

# Define the range of numbers
numbers = list(range(28, 65))

# Remove the numbers already in the grid from the list of numbers
for row in grid:
    for num in row:
        if num != 'x' and num in numbers:
            numbers.remove(num)

# Define a function to check if a number can be placed at a position
def is_safe(grid, row, col, num):
    # Check the row
    if row_sums[row] is not None and np.sum([n for n in grid[row] if n != 'x']) + num > row_sums[row]:
        return False
    # Check the column
    if col_sums[col] is not None and np.sum([n for n in grid[:, col] if n != 'x']) + num > col_sums[col]:
        return False
    # Check the diagonal
    if row == col and np.sum([grid[i][i] for i in range(4) if grid[i][i] != 'x']) + num > diag_sum:
        return False
    return True

# Define a function to solve the grid
def solve_grid(grid, numbers):
    # Find the first 'x' in the grid
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 'x':
                # Try placing each number at the position
                for num in numbers:
                    if is_safe(grid, i, j, num):
                        grid[i][j] = num
                        numbers.remove(num)
                        if solve_grid(grid, numbers):
                            return True
                        grid[i][j] = 'x'
                        numbers.append(num)
                return False
    return True

# Solve the grid
solve_grid(grid, numbers)

# Print the solution
solution = []
for i in range(4):
    for j in range(4):
        if type(grid[i][j]) == int:
            solution.append((i, j, grid[i][j]))
print(solution)
