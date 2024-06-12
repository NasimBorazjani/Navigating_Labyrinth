
import numpy as np

# Initialize the grid
grid = np.array([[44, 'x', 'x', 'x'],
                 [90, 52, 'x', 91],
                 ['x', 58, 'x', 62],
                 ['x', 80, 'x', 'x']])

# Initialize the list of unique integers
numbers = list(range(36, 93))

# Remove the numbers already in the grid from the list
for row in grid:
    for num in row:
        if num != 'x' and num in numbers:
            numbers.remove(num)

# Define the target sums
target_sums = {'cols': [None, 279, 306, None], 'rows': [None, 315, 234, None], 'diag': 264}

# Define a function to check if a number can be placed at a certain position
def can_place(grid, row, col, num):
    # Check the row
    if target_sums['rows'][row] is not None and np.sum([n for n in grid[row] if n != 'x']) + num > target_sums['rows'][row]:
        return False
    # Check the column
    if target_sums['cols'][col] is not None and np.sum([n for n in grid[:, col] if n != 'x']) + num > target_sums['cols'][col]:
        return False
    # Check the diagonal
    if row == col and target_sums['diag'] is not None and np.sum([grid[i][i] for i in range(4) if grid[i][i] != 'x']) + num > target_sums['diag']:
        return False
    return True

# Define a function to solve the problem using backtracking
def solve(grid, numbers):
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 'x':
                for num in numbers:
                    if can_place(grid, i, j, num):
                        grid[i][j] = num
                        numbers.remove(num)
                        if solve(grid, numbers):
                            return True
                        grid[i][j] = 'x'
                        numbers.append(num)
                return False
    return True

# Solve the problem
solve(grid, numbers)

# Print the solution
solution = [(i, j, grid[i][j]) for i in range(4) for j in range(4) if type(grid[i][j]) is not str]
print(solution)
