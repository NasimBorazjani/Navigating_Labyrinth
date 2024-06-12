
import numpy as np

# Define the grid
grid = np.array([[14, 35, 'x', 'x'],
                 ['x', 'x', 'x', 18],
                 ['x', 31, 27, 21],
                 [30, 'x', 'x', 19]])

# Define the sums of columns and rows
col_sums = [None, 121, 107, None]
row_sums = [None, 89, 103, None]

# Define the sum of the diagonal
diag_sum = 102

# Define the range of numbers
numbers = list(range(9, 41))

# Remove the numbers already in the grid from the list of numbers
for i in range(4):
    for j in range(4):
        if grid[i, j] != 'x':
            numbers.remove(grid[i, j])

# Define a function to check if a number can be placed at a cell
def is_safe(i, j, num):
    # Check the column
    if col_sums[j] is not None and (grid[:, j][grid[:, j] != 'x'].sum() + num > col_sums[j]):
        return False
    # Check the row
    if row_sums[i] is not None and (grid[i, :][grid[i, :] != 'x'].sum() + num > row_sums[i]):
        return False
    # Check the diagonal
    if i == j and (np.diag(grid)[np.diag(grid) != 'x'].sum() + num > diag_sum):
        return False
    return True

# Define a function to solve the grid
def solve_grid():
    for i in range(4):
        for j in range(4):
            if grid[i, j] == 'x':
                for num in numbers:
                    if is_safe(i, j, num):
                        grid[i, j] = num
                        numbers.remove(num)
                        if solve_grid():
                            return True
                        grid[i, j] = 'x'
                        numbers.append(num)
                return False
    return True

# Solve the grid
solve_grid()

# Print the solution
solution = []
for i in range(4):
    for j in range(4):
        if type(grid[i, j]) == np.int64:
            solution.append((i, j, grid[i, j]))
print(solution)
