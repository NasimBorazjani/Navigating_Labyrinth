
import numpy as np

# Define the grid
grid = np.array([['x', 'x', 62],
                 ['x', 'x', 'x'],
                 ['x', 'x', 56]])

# Define the sums
sum_col_1 = 212
sum_row_1 = 193
sum_diag = 217

# Define the range of numbers
numbers = list(range(50, 85))

# Define the function to check if a number can be placed at a position
def can_place(grid, row, col, num):
    # Check if the number is already in the row or column
    for i in range(3):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    # Check if the number is already in the diagonal
    if row == col and sum(grid[i][i] for i in range(3) if grid[i][i] != 'x') + num > sum_diag:
        return False
    # Check if the sum of the row or column would exceed the required sum
    if sum(grid[row][i] for i in range(3) if grid[row][i] != 'x') + num > sum_row_1 or \
       sum(grid[i][col] for i in range(3) if grid[i][col] != 'x') + num > sum_col_1:
        return False
    return True

# Define the function to solve the grid
def solve(grid):
    for row in range(3):
        for col in range(3):
            if grid[row][col] == 'x':
                for num in numbers:
                    if can_place(grid, row, col, num):
                        grid[row][col] = num
                        numbers.remove(num)
                        if solve(grid):
                            return True
                        grid[row][col] = 'x'
                        numbers.append(num)
                return False
    return True

# Solve the grid
solve(grid)

# Print the solution
print(grid)
