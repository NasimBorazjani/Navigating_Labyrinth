
import numpy as np

# Define the initial grid
grid = np.array([[37, 50, 'x', 70],
                 ['x', 46, 'x', 65],
                 [41, 43, 'x', 49],
                 ['x', 30, 'x', 'x']])

# Define the range of numbers
numbers = set(range(22, 73))

# Remove the numbers already in the grid from the set of numbers
for row in grid:
    for num in row:
        if num != 'x':
            numbers.remove(num)

# Define a function to check if a number can be placed at a certain position
def is_valid(num, row, col):
    # Check the row
    if 'x' not in grid[row] and (list(grid[row]).count(num) > 0 or not (np.all(np.diff(grid[row]) > 0) or np.all(np.diff(grid[row]) < 0))):
        return False
    # Check the column
    if 'x' not in grid[:, col] and (list(grid[:, col]).count(num) > 0 or not (np.all(np.diff(grid[:, col]) > 0) or np.all(np.diff(grid[:, col]) < 0))):
        return False
    return True

# Define a function to solve the grid
def solve():
    for row in range(4):
        for col in range(4):
            if grid[row, col] == 'x':
                for num in numbers:
                    if is_valid(num, row, col):
                        grid[row, col] = num
                        numbers.remove(num)
                        if solve():
                            return True
                        grid[row, col] = 'x'
                        numbers.add(num)
                return False
    return True

# Solve the grid
solve()

# Print the solution
print(grid)
