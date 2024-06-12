
import numpy as np

# Define the initial grid
grid = np.array([['43', '48', 'x', 'x'],
                 ['x', 'x', 'x', '58'],
                 ['x', '37', '41', '60'],
                 ['x', '34', 'x', '61']])

# Define the set of possible numbers
numbers = set(map(str, range(22, 63)))

# Find the 'x's in the grid
xs = [(i, j) for i in range(4) for j in range(4) if grid[i, j] == 'x']

# Define a function to check if a number can be placed at a certain position
def can_place(x, i, j, num):
    # Check the row
    if any(grid[i, k] == num for k in range(4)):
        return False
    # Check the column
    if any(grid[k, j] == num for k in range(4)):
        return False
    # Check the diagonal
    if i == j and any(grid[k, k] == num for k in range(4)):
        return False
    return True

# Define a function to solve the grid
def solve(x):
    if not xs:
        return True
    i, j = xs[x]
    for num in numbers:
        if can_place(x, i, j, num):
            grid[i, j] = num
            numbers.remove(num)
            if solve(x + 1):
                return True
            grid[i, j] = 'x'
            numbers.add(num)
    return False

# Solve the grid
solve(0)

# Print the solution
print(grid)
