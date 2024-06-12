
import numpy as np

# Initialize the grid
grid = np.array([['x', 'x', 'x'], ['x', '61', '62'], ['x', 'x', '63']])
grid = np.where(grid=='x', -1, grid).astype(int)

# Initialize the list of used numbers
used_numbers = set(grid[grid!=-1])

# Define the function to check if a number can be placed at a certain position
def can_place(grid, row, col, num):
    # Check the row
    for i in range(3):
        if grid[row][i] == num:
            return False
    # Check the column
    for i in range(3):
        if grid[i][col] == num:
            return False
    # Check the order
    if row > 0 and grid[row-1][col] != -1 and grid[row-1][col] >= num:
        return False
    if col > 0 and grid[row][col-1] != -1 and grid[row][col-1] >= num:
        return False
    return True

# Define the function to solve the grid
def solve(grid):
    for row in range(3):
        for col in range(3):
            if grid[row][col] == -1:
                for num in range(40, 89):
                    if num not in used_numbers and can_place(grid, row, col, num):
                        grid[row][col] = num
                        used_numbers.add(num)
                        if solve(grid):
                            return True
                        grid[row][col] = -1
                        used_numbers.remove(num)
                return False
    return True

# Solve the grid
solve(grid)

# Print the solution
solution = []
for row in range(3):
    for col in range(3):
        if (row, col) not in [(1, 1), (1, 2), (2, 2)]:
            solution.append((row, col, grid[row][col]))
print(solution)
