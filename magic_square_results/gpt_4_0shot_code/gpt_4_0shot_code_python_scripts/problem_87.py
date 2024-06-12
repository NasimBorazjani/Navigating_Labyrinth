
import numpy as np

# Define the grid
grid = np.array([[72, 76, 68, 69],
                 [56, -1, -1, -1],
                 [49, -1, -1, 43],
                 [-1, -1, 61, -1]])

# Define the sums
col_sums = [None, 258, 247, None]
row_sums = [None, 233, 237, None]
diag_sum = 242

# Define the range of numbers
numbers = set(range(37, 84))

# Remove the numbers already in the grid from the set of numbers
for row in grid:
    for num in row:
        if num in numbers:
            numbers.remove(num)

# Define a function to check if a number can be placed at a position
def can_place(grid, row, col, num):
    # Check the row
    if row_sums[row] is not None and grid[row].sum() + num > row_sums[row]:
        return False
    # Check the column
    if col_sums[col] is not None and grid[:, col].sum() + num > col_sums[col]:
        return False
    # Check the diagonal
    if row == col and grid.diagonal().sum() + num > diag_sum:
        return False
    return True

# Define a function to solve the grid
def solve(grid, numbers):
    # Find the first empty position
    for i in range(4):
        for j in range(4):
            if grid[i, j] == -1:
                # Try to place a number at the position
                for num in list(numbers):
                    if can_place(grid, i, j, num):
                        grid[i, j] = num
                        numbers.remove(num)
                        if solve(grid, numbers):
                            return True
                        grid[i, j] = -1
                        numbers.add(num)
                return False
    return True

# Solve the grid
solve(grid, numbers)

# Print the solution
solution = []
for i in range(4):
    for j in range(4):
        solution.append((i, j, grid[i, j]))
print(solution)
