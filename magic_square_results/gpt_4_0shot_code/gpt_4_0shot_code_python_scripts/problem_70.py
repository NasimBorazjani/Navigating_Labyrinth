
import numpy as np

# Initialize the grid
grid = np.array([[36, 47, 'x', 'x'],
                 ['x', 28, 40, 'x'],
                 ['x', 33, 'x', 'x'],
                 [50, 'x', 'x', 'x']])

# Initialize the constraints
col_sums = [None, 156, 185, None]
row_sums = [None, 152, 158, None]
diag_sum = 165

# Initialize the set of available numbers
available_numbers = set(range(28, 65)) - {36, 47, 28, 40, 33, 50}

# Initialize the solution
solution = []

def solve(grid, row, col):
    # If we have filled the last cell, check the diagonal sum
    if row == 4:
        if np.trace(grid[::-1]) == diag_sum:
            return True
        else:
            return False

    # If we have filled the last cell in the row, move to the next row
    if col == 4:
        if row_sums[row] is None or np.sum(grid[row]) == row_sums[row]:
            return solve(grid, row + 1, 0)
        else:
            return False

    # If the cell is not 'x', move to the next cell
    if grid[row][col] != 'x':
        return solve(grid, row, col + 1)

    # Try all available numbers
    for num in available_numbers:
        # Check the column sum
        if col_sums[col] is not None and np.sum(grid[:, col]) + num > col_sums[col]:
            continue

        # Place the number in the cell
        grid[row][col] = num
        available_numbers.remove(num)

        # Recursively try to fill the next cell
        if solve(grid, row, col + 1):
            solution.append((row, col, num))
            return True

        # If we can't fill the next cell, backtrack
        grid[row][col] = 'x'
        available_numbers.add(num)

    return False

# Solve the problem
solve(grid, 0, 0)

# Print the solution
print(solution)
