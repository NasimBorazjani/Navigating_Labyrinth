
import numpy as np

# Define the grid
grid = np.array([['x', 'x', 'x'], ['x', 'x', 'x'], [37, 'x', 'x']])

# Define the range of possible numbers
numbers = list(range(35, 60))

# Remove the numbers that are already in the grid
numbers = [num for num in numbers if num not in grid]

# Define the target sums
target_sums = {'col1': 125, 'row1': 157, 'diag': 138}

def solve(grid, numbers):
    # Find the first 'x' in the grid
    for i in range(3):
        for j in range(3):
            if grid[i, j] == 'x':
                # Try each possible number
                for num in numbers:
                    # Add the number to the grid
                    grid[i, j] = num
                    # Remove the number from the list of possible numbers
                    numbers.remove(num)
                    # Check if the current grid is valid
                    if is_valid(grid):
                        # If the grid is valid, continue with the next 'x'
                        if solve(grid, numbers):
                            return True
                    # If the grid is not valid or if we can't solve the rest of the grid, backtrack
                    grid[i, j] = 'x'
                    numbers.append(num)
                # If we tried all possible numbers and none of them worked, return False
                return False
    # If there are no 'x's left in the grid, return True
    return True

def is_valid(grid):
    # Check the sum of column 1
    if np.sum(grid[:, 1]) > target_sums['col1']:
        return False
    # Check the sum of row 1
    if np.sum(grid[1, :]) > target_sums['row1']:
        return False
    # Check the sum of the diagonal
    if np.sum(grid.diagonal()[::-1]) > target_sums['diag']:
        return False
    # If all conditions are met, return True
    return True

# Solve the grid
solve(grid, numbers)

# Print the solution
solution = [(i, j, grid[i, j]) for i in range(3) for j in range(3) if type(grid[i, j]) is not str]
print(solution)
