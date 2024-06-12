
import numpy as np

# Define the grid
grid = np.array([['x', 'x', 'x'], ['x', '73', '47'], ['x', 'x', 'x']])

# Define the range of possible numbers
numbers = list(range(34, 79))

# Remove the numbers already in the grid from the list of possible numbers
for row in grid:
    for num in row:
        if num != 'x' and int(num) in numbers:
            numbers.remove(int(num))

# Define the target sums
target_sums = {'col1': 177, 'row1': 180, 'diag': 183}

# Define the positions of the 'x's
positions = [(i, j) for i in range(3) for j in range(3) if grid[i, j] == 'x']

# Sort the positions by the target sums of their corresponding rows, columns and diagonal
positions.sort(key=lambda pos: target_sums.get('col' + str(pos[1]), 0) + target_sums.get('row' + str(pos[0]), 0) + (target_sums['diag'] if pos[0] + pos[1] == 2 else 0))

# Assign the smallest possible numbers to the 'x's
solution = []
for pos in positions:
    num = min(numbers)
    numbers.remove(num)
    solution.append((pos[0], pos[1], num))

print(solution)
