
import numpy as np

# Initialize the grid
grid = np.array([['x', 'x', 'x'], ['x', 'x', 'x'], ['41', 'x', 'x']])

# Initialize the list of unique integers
numbers = list(range(31, 76))
numbers.remove(41)  # Remove the number already in the grid

# Define the target sums
target_sums = {'col1': 135, 'row1': 134, 'diag': 122}

# Define a function to check if a number can be placed at a certain position
def can_place(grid, row, col, num):
    # Check the column
    if 'x' not in grid[:, col] and grid[:, col].astype(int).sum() + num > target_sums['col1']:
        return False
    # Check the row
    if 'x' not in grid[row, :] and grid[row, :].astype(int).sum() + num > target_sums['row1']:
        return False
    # Check the diagonal
    if row == col and 'x' not in np.diag(grid) and np.diag(grid).astype(int).sum() + num > target_sums['diag']:
        return False
    return True

# Define a function to solve the grid
def solve(grid):
    # Find the first 'x' in the grid
    for i in range(3):
        for j in range(3):
            if grid[i, j] == 'x':
                # Try to place each number in the 'x'
                for num in numbers:
                    if can_place(grid, i, j, num):
                        grid[i, j] = str(num)
                        numbers.remove(num)
                        if solve(grid):
                            return True
                        grid[i, j] = 'x'
                        numbers.append(num)
                return False
    return True

# Solve the grid
solve(grid)

# Print the solution
solution = []
for i in range(3):
    for j in range(3):
        solution.append((i, j, int(grid[i, j])))
print(solution)
