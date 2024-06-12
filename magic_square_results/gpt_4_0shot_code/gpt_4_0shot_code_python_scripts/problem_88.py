
import numpy as np

# Initialize the grid
grid = np.array([[27, 48, 'x', 'x'],
                 ['x', 'x', 63, 'x'],
                 [28, 'x', 33, 26],
                 ['x', 'x', 'x', 39]])

# Initialize the constraints
col_sums = [None, 183, 202, None]
row_sums = [None, 190, 154, None]
diag_sum = 183

# Initialize the list of unique integers
numbers = list(range(22, 69))

# Remove the numbers already in the grid from the list
for row in grid:
    for cell in row:
        if cell != 'x' and cell in numbers:
            numbers.remove(cell)

# Define a function to check if the current grid satisfies the constraints
def check_grid(grid):
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
                for number in numbers:
                    grid[i, j] = number
                    numbers.remove(number)
                    if check_grid(grid):
                        if solve(grid, numbers):
                            return True
                    grid[i, j] = 'x'
                    numbers.append(number)
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
