
import numpy as np

# Define the grid
grid = np.array([[51, 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']])

# Define the sums
sums = {'row1': 124, 'col1': 107, 'diag': 108}

# Define the range of numbers
numbers = list(range(26, 66))

# Remove the known numbers from the list
numbers.remove(51)

# Define a function to check the sums
def check_sums(grid, sums):
    if 'x' not in grid[1, :] and np.sum(grid[1, :].astype(int)) != sums['row1']:
        return False
    if 'x' not in grid[:, 0] and np.sum(grid[:, 0].astype(int)) != sums['col1']:
        return False
    if 'x' not in np.diag(np.fliplr(grid)) and np.sum(np.diag(np.fliplr(grid)).astype(int)) != sums['diag']:
        return False
    return True

# Define a function to solve the problem
def solve(grid, numbers):
    for i in range(3):
        for j in range(3):
            if grid[i, j] == 'x':
                for number in numbers:
                    grid[i, j] = number
                    numbers.remove(number)
                    if check_sums(grid, sums) and solve(grid, numbers):
                        return True
                    grid[i, j] = 'x'
                    numbers.append(number)
                return False
    return True

# Solve the problem
solve(grid, numbers)

# Print the solution
solution = [(i, j, grid[i, j]) for i in range(3) for j in range(3) if isinstance(grid[i, j], int)]
print(solution)
