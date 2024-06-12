
import numpy as np

# Initialize the grid
grid = np.array([['x', 'x', 'x'], ['x', 'x', 66], ['x', 'x', 'x']])

# Initialize the list of available numbers
available_numbers = list(range(48, 78))
available_numbers.remove(66)  # Remove the number already in the grid

# Define the target sums
target_sums = {'row1': 191, 'col1': 200, 'diag': 201}

def solve(grid, available_numbers):
    # Find the first 'x' in the grid
    for i in range(3):
        for j in range(3):
            if grid[i, j] == 'x':
                # Try to fill the 'x' with each available number
                for number in available_numbers:
                    grid[i, j] = number
                    available_numbers.remove(number)

                    # Check if the current grid is valid
                    if is_valid(grid):
                        # If the grid is valid, try to solve the rest of the grid
                        result = solve(grid, available_numbers)
                        if result is not None:
                            return result

                    # If the number does not lead to a solution, backtrack
                    grid[i, j] = 'x'
                    available_numbers.append(number)

    # If all 'x's are filled and the grid is valid, return the grid
    if is_valid(grid):
        return [(i, j, grid[i, j]) for i in range(3) for j in range(3) if type(grid[i, j]) == int]

    # If no solution is found, return None
    return None

def is_valid(grid):
    # Check the sum of row 1
    if 'x' not in grid[1, :] and np.sum(grid[1, :]) != target_sums['row1']:
        return False

    # Check the sum of column 1
    if 'x' not in grid[:, 1] and np.sum(grid[:, 1]) != target_sums['col1']:
        return False

    # Check the sum of the diagonal
    if 'x' not in np.diag(np.fliplr(grid)) and np.sum(np.diag(np.fliplr(grid))) != target_sums['diag']:
        return False

    return True

# Solve the magic square problem
solution = solve(grid, available_numbers)
print(solution)
