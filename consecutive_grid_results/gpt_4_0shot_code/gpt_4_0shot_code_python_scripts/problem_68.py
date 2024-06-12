
import numpy as np

# Define the initial grid
grid = np.array([['x', 40, 'x', 65],
                 [34, 'x', 53, 'x'],
                 ['x', 'x', 'x', 63],
                 ['x', 56, 'x', 62]])

# Define the range of numbers
numbers = list(range(25, 71))

# Remove the numbers that are already in the grid from the list of numbers
for row in grid:
    for number in row:
        if number != 'x' and number in numbers:
            numbers.remove(number)

# Sort the remaining numbers in ascending order
numbers.sort()

# Define the positions of the 'x's in the grid
positions = [(i, j) for i in range(4) for j in range(4) if grid[i, j] == 'x']

# Define the function to check if a number can be placed at a certain position
def can_place(grid, row, col, num):
    # Check the row
    for i in range(4):
        if grid[row, i] == num:
            return False
    # Check the column
    for i in range(4):
        if grid[i, col] == num:
            return False
    # Check the order
    if row > 0 and grid[row - 1, col] != 'x' and grid[row - 1, col] >= num:
        return False
    if col > 0 and grid[row, col - 1] != 'x' and grid[row, col - 1] >= num:
        return False
    return True

# Define the function to solve the grid
def solve(grid, positions, numbers):
    if not positions:
        return True
    for num in numbers:
        row, col = positions[0]
        if can_place(grid, row, col, num):
            grid[row, col] = num
            numbers.remove(num)
            if solve(grid, positions[1:], numbers):
                return True
            grid[row, col] = 'x'
            numbers.append(num)
    return False

# Solve the grid
solve(grid, positions, numbers)

# Print the solution
solution = [(i, j, grid[i, j]) for i, j in positions]
print(solution)
