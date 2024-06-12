
from itertools import permutations

# Define the grid
grid = [['x', 51, 'x', 65],
        ['x', 'x', 'x', 68],
        ['x', 'x', 64, 75],
        ['x', 'x', 'x', 'x']]

# Define the constraints
column_sums = [None, 240, 226, None]
row_sums = [None, 255, 268, None]
diagonal_sum = 264

# Find the 'x' positions and the possible numbers
x_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
possible_numbers = list(set(range(43, 85)) - set([grid[i][j] for i in range(4) for j in range(4) if grid[i][j] != 'x']))

# Try all possible combinations
for numbers in permutations(possible_numbers, len(x_positions)):
    # Fill the 'x' positions with the numbers
    for (i, j), number in zip(x_positions, numbers):
        grid[i][j] = number
    # Check the constraints
    if all(sum(grid[i][j] for i in range(4) if grid[i][j] != 'x') == column_sums[j] for j in range(4) if column_sums[j] is not None) and \
       all(sum(grid[i][j] for j in range(4) if grid[i][j] != 'x') == row_sums[i] for i in range(4) if row_sums[i] is not None) and \
       sum(grid[i][3-i] for i in range(4) if grid[i][3-i] != 'x') == diagonal_sum:
        # If the constraints are satisfied, print the solution
        print([(i, j, grid[i][j]) for (i, j) in x_positions])
        break
