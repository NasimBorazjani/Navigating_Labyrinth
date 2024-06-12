
import numpy as np

# Define the grid
grid = np.array([[45, 53, 'x', 'x'],
                 ['x', 'x', 'x', 'x'],
                 [47, 'x', 'x', 'x'],
                 [35, 'x', 52, 'x']])

# Define the constraints
col_sums = [None, 173, 166, None]
row_sums = [None, 166, 165, None]
diag_sum = 131

# Define the range of possible numbers
numbers = list(range(23, 55))

# Remove the numbers already in the grid from the list of possible numbers
for row in grid:
    for num in row:
        if num != 'x' and num in numbers:
            numbers.remove(num)

# Define a function to check if a number can be placed at a certain position
def is_valid(num, row, col):
    # Check the row
    if row_sums[row] is not None and (sum(grid[row]) + num > row_sums[row]):
        return False
    # Check the column
    if col_sums[col] is not None and (sum(grid[:, col]) + num > col_sums[col]):
        return False
    # Check the diagonal
    if row == col and (sum(np.diag(grid)) + num > diag_sum):
        return False
    return True

# Define a function to solve the grid
def solve():
    for row in range(4):
        for col in range(4):
            if grid[row][col] == 'x':
                for num in numbers:
                    if is_valid(num, row, col):
                        grid[row][col] = num
                        numbers.remove(num)
                        if solve():
                            return True
                        grid[row][col] = 'x'
                        numbers.append(num)
                return False
    return True

# Solve the grid
solve()

# Print the solution
solution = []
for row in range(4):
    for col in range(4):
        if type(grid[row][col]) is int:
            solution.append((row, col, grid[row][col]))
print(solution)
