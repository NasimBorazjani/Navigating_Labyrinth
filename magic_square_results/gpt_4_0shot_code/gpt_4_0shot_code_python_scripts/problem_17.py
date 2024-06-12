
import numpy as np

# Initialize the grid
grid = np.array([['x', 52, 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']])

# Initialize the list of numbers
numbers = list(range(48, 78))

# Remove the given numbers from the list
numbers.remove(52)

# Define the target sums
target_sums = [166, 192, 184]

def solve(grid, numbers, target_sums):
    # Find the first 'x' in the grid
    for i in range(3):
        for j in range(3):
            if grid[i, j] == 'x':
                # Try each number
                for number in numbers:
                    # Check if the number can be placed in the current position
                    if is_valid(grid, i, j, number, target_sums):
                        # Place the number
                        grid[i, j] = number
                        # Remove the number from the list
                        numbers.remove(number)
                        # Continue with the next 'x'
                        if solve(grid, numbers, target_sums):
                            return True
                        # If not successful, backtrack
                        grid[i, j] = 'x'
                        numbers.append(number)
                return False
    return True

def is_valid(grid, row, col, number, target_sums):
    # Check the row sum
    if 'x' not in grid[row, :] and np.sum(grid[row, :]) != target_sums[1]:
        return False
    # Check the column sum
    if 'x' not in grid[:, col] and np.sum(grid[:, col]) != target_sums[0]:
        return False
    # Check the diagonal sum
    if row == col and 'x' not in np.diag(grid) and np.sum(np.diag(grid)) != target_sums[2]:
        return False
    return True

# Solve the problem
solve(grid, numbers, target_sums)

# Print the solution
solution = [(i, j, grid[i, j]) for i in range(3) for j in range(3) if grid[i, j] != 'x']
print(solution)
