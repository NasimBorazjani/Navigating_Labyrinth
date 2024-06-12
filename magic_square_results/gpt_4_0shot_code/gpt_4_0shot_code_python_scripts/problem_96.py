
import numpy as np

# Define the grid
grid = np.array([['x', 'x', 'x', 'x'],
                 ['x', '52', '20', 'x'],
                 ['41', '13', 'x', 'x'],
                 ['54', 'x', '16', '11']])

# Define the sums
col_sums = [None, 148, 109, None]
row_sums = [None, 105, 115, None]
diag_sum = 134

# Define the range of numbers
numbers = set(range(11, 63))

# Remove the numbers already in the grid from the set of numbers
for row in grid:
    for num in row:
        if num != 'x':
            numbers.remove(int(num))

# Define a function to check if a number can be placed at a position
def can_place(grid, row, col, num):
    # Check the row
    if row_sums[row] is not None and sum(int(x) for x in grid[row] if x != 'x') + num > row_sums[row]:
        return False

    # Check the column
    if col_sums[col] is not None and sum(int(grid[i][col]) for i in range(4) if grid[i][col] != 'x') + num > col_sums[col]:
        return False

    # Check the diagonal
    if row == col and sum(int(grid[i][i]) for i in range(4) if grid[i][i] != 'x') + num > diag_sum:
        return False

    return True

# Define a function to solve the grid
def solve(grid, numbers):
    for row in range(4):
        for col in range(4):
            if grid[row][col] == 'x':
                for num in sorted(numbers):
                    if can_place(grid, row, col, num):
                        grid[row][col] = str(num)
                        numbers.remove(num)

                        if solve(grid, numbers):
                            return True

                        grid[row][col] = 'x'
                        numbers.add(num)

                return False

    return True

# Solve the grid
solve(grid, numbers)

# Print the solution
solution = [(i, j, int(grid[i][j])) for i in range(4) for j in range(4) if grid[i][j] != 'x']
print(solution)
