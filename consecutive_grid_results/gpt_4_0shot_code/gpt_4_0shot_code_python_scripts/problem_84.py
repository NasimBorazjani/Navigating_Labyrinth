
import numpy as np

# Define the grid
grid = np.array([[91, 57, 'x', 45],
                 [41, 49, 'x', 'x'],
                 ['x', 'x', 49, 'x'],
                 ['x', 46, 47, 73]])

# Define the range of numbers
numbers = set(range(39, 95))

# Remove the numbers already in the grid from the set of numbers
for row in grid:
    for num in row:
        if num != 'x':
            numbers.remove(num)

# Define a function to check if a number can be placed at a certain position
def can_place(x, y, num):
    # Check the row
    for i in range(4):
        if grid[x][i] == num:
            return False
    # Check the column
    for i in range(4):
        if grid[i][y] == num:
            return False
    return True

# Define a function to solve the grid
def solve():
    for x in range(4):
        for y in range(4):
            if grid[x][y] == 'x':
                for num in numbers:
                    if can_place(x, y, num):
                        grid[x][y] = num
                        numbers.remove(num)
                        if solve():
                            return True
                        grid[x][y] = 'x'
                        numbers.add(num)
                return False
    return True

# Solve the grid
solve()

# Print the solution
for x in range(4):
    for y in range(4):
        if (x, y) in [(0, 2), (1, 2), (1, 3), (2, 0), (2, 1), (2, 3), (3, 0)]:
            print((x, y, grid[x][y]))
