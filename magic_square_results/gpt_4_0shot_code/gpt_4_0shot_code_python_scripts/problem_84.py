
import numpy as np

# Initialize the grid
grid = np.array([[42, 53, 43, 72],
                 [None, 82, 54, None],
                 [None, 62, 44, None],
                 [None, None, None, None]])

# Initialize the constraints
col_sums = [None, 277, 204, None]
row_sums = [None, 253, 221, None]
diag_sum = 252

# Initialize the set of available numbers
available_numbers = set(range(37, 84)) - set(grid[~np.isnan(grid)])

def solve(grid, available_numbers):
    # Find the first empty cell
    for i in range(4):
        for j in range(4):
            if grid[i, j] is None:
                # Try all available numbers
                for num in list(available_numbers):
                    grid[i, j] = num
                    available_numbers.remove(num)

                    # Check if the current number satisfies the constraints
                    if ((col_sums[j] is None or np.nansum(grid[:, j]) <= col_sums[j]) and
                        (row_sums[i] is None or np.nansum(grid[i, :]) <= row_sums[i]) and
                        (i != j or np.trace(grid[::-1, :]) <= diag_sum)):
                        # Recursively solve the rest of the grid
                        if solve(grid, available_numbers):
                            return True

                    # Backtrack
                    grid[i, j] = None
                    available_numbers.add(num)

                return False

    # All cells are filled
    return True

# Solve the grid
solve(grid, available_numbers)

# Print the solution
solution = [(i, j, grid[i, j]) for i in range(4) for j in range(4) if not np.isnan(grid[i, j])]
print(solution)
