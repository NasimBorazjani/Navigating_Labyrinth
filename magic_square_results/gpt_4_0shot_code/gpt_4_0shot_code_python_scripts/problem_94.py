
import numpy as np

# Initialize the grid
grid = np.array([[48, 'x', 'x', 'x'],
                 [54, 'x', 'x', 'x'],
                 ['x', 64, 44, 83],
                 [82, 68, 51, 'x']])

# Define the constraints
row_sums = [None, 270, 234, None]
col_sums = [None, 267, 236, None]
diag_sum = 301

# Define the range of possible numbers
numbers = set(range(41, 93))

# Remove the numbers already in the grid from the set of possible numbers
for row in grid:
    for num in row:
        if num != 'x':
            numbers.remove(num)

# Define a function to check if the current grid satisfies the constraints
def check_grid(grid):
    for i in range(4):
        if row_sums[i] is not None and np.sum(grid[i, :]) != row_sums[i]:
            return False
        if col_sums[i] is not None and np.sum(grid[:, i]) != col_sums[i]:
            return False
    if np.sum(grid.diagonal()) != diag_sum:
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
                    if check_grid(grid):
                        if solve(grid, numbers):
                            return True
                    grid[i, j] = 'x'
                    numbers.add(num)
                return False
    return True

# Solve the problem
solve(grid, numbers)

# Print the solution
solution = []
for i in range(4):
    for j in range(4):
        if grid[i, j] != 'x':
            solution.append((i, j, grid[i, j]))
print(solution)
