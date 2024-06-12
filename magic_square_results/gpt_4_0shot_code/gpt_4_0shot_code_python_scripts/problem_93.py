
import numpy as np

# Initialize the grid
grid = np.array([[53, 57, 'x', 'x'],
                 [77, 78, 'x', 56],
                 [51, 62, 88, 'x'],
                 ['x', 'x', 'x', 'x']])

# Initialize the constraints
col_sums = [None, 244, 295, None]
row_sums = [None, 266, 261, None]
diag_sum = 265

# Initialize the list of unique integers
numbers = list(range(41, 93))

# Remove the numbers already in the grid from the list
for row in grid:
    for num in row:
        if num != 'x' and num in numbers:
            numbers.remove(num)

# Define a function to check if the current grid satisfies the constraints
def check_grid(grid, col_sums, row_sums, diag_sum):
    for i in range(4):
        if col_sums[i] is not None and np.sum(grid[:, i]) != col_sums[i]:
            return False
        if row_sums[i] is not None and np.sum(grid[i, :]) != row_sums[i]:
            return False
    if np.sum(np.diag(np.fliplr(grid))) != diag_sum:
        return False
    return True

# Define a function to solve the problem using backtracking
def solve(grid, numbers):
    for i in range(4):
        for j in range(4):
            if grid[i, j] == 'x':
                for num in numbers:
                    grid[i, j] = num
                    numbers.remove(num)
                    if check_grid(grid, col_sums, row_sums, diag_sum):
                        if solve(grid, numbers):
                            return True
                    grid[i, j] = 'x'
                    numbers.append(num)
                return False
    return True

# Solve the problem
solve(grid, numbers)

# Print the solution
solution = []
for i in range(4):
    for j in range(4):
        if type(grid[i, j]) == int:
            solution.append((i, j, grid[i, j]))
print(solution)
