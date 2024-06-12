
import numpy as np

# Define the initial grid
grid = np.array([['x', 'x', '25', '28'],
                 ['x', 'x', '28', '31'],
                 ['15', 'x', '34', 'x'],
                 ['13', '34', 'x', 'x']])

# Define the range of possible numbers
numbers = set(map(str, range(13, 54)))

# Remove the numbers already in the grid from the set of possible numbers
for row in grid:
    numbers -= set(row)

# Convert the numbers back to integers and sort them
numbers = sorted(map(int, numbers))

# Define the positions of the 'x's
positions = [(i, j) for i in range(4) for j in range(4) if grid[i, j] == 'x']

# Define a function to check if a number can be placed at a position
def can_place(x, y, num):
    for i in range(4):
        if grid[i, y] != 'x' and int(grid[i, y]) >= num:
            return False
        if grid[x, i] != 'x' and int(grid[x, i]) >= num:
            return False
    return True

# Define a function to place the numbers
def place_numbers(i):
    if i == len(positions):
        return True
    x, y = positions[i]
    for num in numbers:
        if can_place(x, y, num):
            grid[x, y] = str(num)
            numbers.remove(num)
            if place_numbers(i + 1):
                return True
            grid[x, y] = 'x'
            numbers.append(num)
    return False

# Place the numbers
place_numbers(0)

# Print the solution
solution = [(x, y, int(grid[x, y])) for x, y in positions]
print(solution)
