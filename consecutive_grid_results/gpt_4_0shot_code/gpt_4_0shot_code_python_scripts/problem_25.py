
import numpy as np

# Define the initial grid
grid = np.array([['x', 'x', 'x'], ['39', 'x', '52'], ['60', 'x', 'x']])

# Define the range of possible numbers
numbers = set(str(i) for i in range(29, 73))

# Define the positions of the 'x's
positions = [(i, j) for i in range(3) for j in range(3) if grid[i, j] == 'x']

# Define a function to check if a number can be placed at a certain position
def is_valid(number, position):
    i, j = position
    if i > 0 and grid[i - 1, j] != 'x' and int(grid[i - 1, j]) >= number:
        return False
    if j > 0 and grid[i, j - 1] != 'x' and int(grid[i, j - 1]) >= number:
        return False
    if i < 2 and grid[i + 1, j] != 'x' and int(grid[i + 1, j]) <= number:
        return False
    if j < 2 and grid[i, j + 1] != 'x' and int(grid[i, j + 1]) <= number:
        return False
    return True

# Define a function to solve the problem
def solve(positions):
    if not positions:
        return []
    i, j = positions[0]
    for number in sorted(numbers - set(grid.flatten())):
        if is_valid(int(number), (i, j)):
            grid[i, j] = number
            solution = solve(positions[1:])
            if solution is not None:
                return [(i, j, int(number))] + solution
            grid[i, j] = 'x'
    return None

# Solve the problem and print the solution
solution = solve(positions)
print(solution)
