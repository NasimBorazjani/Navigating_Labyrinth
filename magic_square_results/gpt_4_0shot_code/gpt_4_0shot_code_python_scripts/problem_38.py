
import numpy as np

# Initialize the grid
grid = np.array([['x', 56, 'x', 40],
                 ['x', 'x', 44, 60],
                 ['x', 52, 'x', 45],
                 ['x', 'x', 62, 47]])

# Initialize the constraints
col_sums = [None, 227, 215, None]
row_sums = [None, 207, 218, None]
diag_sum = 195

# Initialize the set of available numbers
available_numbers = set(range(40, 67)) - {56, 40, 44, 60, 52, 45, 62, 47}

def solve(grid, available_numbers):
    # Find the first 'x' in the grid
    for i in range(4):
        for j in range(4):
            if grid[i, j] == 'x':
                # Try all available numbers
                for num in list(available_numbers):
                    grid[i, j] = num
                    available_numbers.remove(num)

                    # Check if the current grid is valid
                    if is_valid(grid):
                        # If the grid is full, return the solution
                        if 'x' not in grid:
                            return [(i, j, num) for i in range(4) for j in range(4) if grid[i, j] == num]
                        # Otherwise, continue with the next 'x'
                        else:
                            result = solve(grid, available_numbers)
                            if result is not None:
                                return result

                    # If the number does not lead to a solution, backtrack
                    grid[i, j] = 'x'
                    available_numbers.add(num)

    # If no solution is found, return None
    return None

def is_valid(grid):
    # Check the column sums
    for j in range(4):
        if col_sums[j] is not None and 'x' not in grid[:, j] and grid[:, j].sum() != col_sums[j]:
            return False

    # Check the row sums
    for i in range(4):
        if row_sums[i] is not None and 'x' not in grid[i, :] and grid[i, :].sum() != row_sums[i]:
            return False

    # Check the diagonal sum
    if 'x' not in np.diag(np.fliplr(grid)) and np.diag(np.fliplr(grid)).sum() != diag_sum:
        return False

    return True

# Print the solution
print(solve(grid, available_numbers))
