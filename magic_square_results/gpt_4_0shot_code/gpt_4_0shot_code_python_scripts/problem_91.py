
import numpy as np

# Initialize the grid
grid = np.array([[62, 'x', 'x', 'x'],
                 ['x', 35, 60, 'x'],
                 ['x', 39, 'x', 54],
                 ['x', 55, 34, 'x']])

# Initialize the constraints
col_sums = [None, 177, 192, None]
row_sums = [None, 217, 193, None]
diag_sum = 149

# Initialize the range of numbers
numbers = list(range(22, 69))

# Remove the numbers already in the grid from the list of numbers
for row in grid:
    for num in row:
        if num != 'x' and num in numbers:
            numbers.remove(num)

# Function to check if a number can be placed at grid[row][col]
def is_safe(grid, row, col, num):
    # Check the row
    if row_sums[row] is not None and (grid[row].sum() + num > row_sums[row]):
        return False
    # Check the column
    if col_sums[col] is not None and (grid[:, col].sum() + num > col_sums[col]):
        return False
    # Check the diagonal
    if row == col and (np.diagonal(grid).sum() + num > diag_sum):
        return False
    return True

# Function to solve the magic square problem
def solve_magic_square(grid, numbers):
    # Find the first 'x' in the grid
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 'x':
                # Try all numbers one by one
                for num in numbers:
                    # Check if the number can be placed at grid[i][j]
                    if is_safe(grid, i, j, num):
                        # Place the number
                        grid[i][j] = num
                        # Remove the number from the list
                        numbers.remove(num)
                        # Recur to fill the rest of the grid
                        if solve_magic_square(grid, numbers):
                            return True
                        # If placing num doesn't lead to a solution, then undo the move
                        grid[i][j] = 'x'
                        numbers.append(num)
                return False
    return True

# Solve the magic square problem
solve_magic_square(grid, numbers)

# Print the solution
solution = []
for i in range(4):
    for j in range(4):
        if type(grid[i][j]) == int:
            solution.append((i, j, grid[i][j]))
print(solution)
