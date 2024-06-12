
import numpy as np

# Initialize the grid
grid = np.array([['x', 'x', 'x'], ['x', 'x', 'x'], [42, 45, 'x']])

# Initialize the list of possible numbers
numbers = list(range(9, 49))

# Remove the numbers that are already in the grid
for row in grid:
    for num in row:
        if num != 'x' and num in numbers:
            numbers.remove(num)

# Define the target sums
target_sums = {'col1': 115, 'row1': 95, 'diag': 133}

# Define a function to check if the current grid is valid
def is_valid(grid, numbers):
    # Check the sum of column 1
    if 'x' not in grid[:, 1] and np.sum(grid[:, 1]) != target_sums['col1']:
        return False

    # Check the sum of row 1
    if 'x' not in grid[1, :] and np.sum(grid[1, :]) != target_sums['row1']:
        return False

    # Check the sum of the diagonal
    if 'x' not in np.diag(np.fliplr(grid)) and np.sum(np.diag(np.fliplr(grid))) != target_sums['diag']:
        return False

    return True

# Define a function to solve the magic square problem
def solve(grid, numbers):
    # Find the first 'x' in the grid
    for i in range(3):
        for j in range(3):
            if grid[i, j] == 'x':
                # Try to fill the 'x' with each possible number
                for num in numbers:
                    grid[i, j] = num
                    numbers.remove(num)

                    # If the current grid is valid, continue with the next 'x'
                    if is_valid(grid, numbers):
                        solution = solve(grid, numbers)
                        if solution is not None:
                            return solution

                    # If the current grid is not valid, backtrack and try the next number
                    grid[i, j] = 'x'
                    numbers.append(num)

                # If no number can fill the 'x', return None
                return None

    # If there are no 'x's in the grid, return the grid
    return grid

# Solve the magic square problem
solution = solve(grid, numbers)

# Print the solution
print(solution)
