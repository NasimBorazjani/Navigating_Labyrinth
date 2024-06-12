
import numpy as np

# Initialize the grid
grid = np.array([[68, 50, 47, 65],
                 [0, 91, 0, 71],
                 [0, 0, 0, 60],
                 [0, 0, 0, 84]])

# Initialize the constraints
col_sums = [None, 262, 272, None]
row_sums = [None, 291, 301, None]
diag_sum = 256

# Initialize the list of available numbers
available_numbers = list(range(41, 93))
for num in grid.flatten():
    if num in available_numbers:
        available_numbers.remove(num)

# Define the function to check the constraints
def check_constraints(grid, col_sums, row_sums, diag_sum):
    for i in range(4):
        if col_sums[i] is not None and grid[:, i].sum() > col_sums[i]:
            return False
        if row_sums[i] is not None and grid[i, :].sum() > row_sums[i]:
            return False
    if grid.diagonal()[::-1].sum() > diag_sum:
        return False
    return True

# Define the function to solve the problem
def solve(grid, available_numbers):
    for i in range(4):
        for j in range(4):
            if grid[i, j] == 0:
                for num in available_numbers:
                    grid[i, j] = num
                    available_numbers.remove(num)
                    if check_constraints(grid, col_sums, row_sums, diag_sum):
                        if solve(grid, available_numbers):
                            return True
                    grid[i, j] = 0
                    available_numbers.append(num)
                return False
    return True

# Solve the problem
solve(grid, available_numbers)

# Print the solution
solution = []
for i in range(4):
    for j in range(4):
        if (i, j) not in [(0, 0), (0, 1), (0, 2), (0, 3), (1, 1), (1, 3), (2, 3), (3, 3)]:
            solution.append((i, j, grid[i, j]))
print(solution)
