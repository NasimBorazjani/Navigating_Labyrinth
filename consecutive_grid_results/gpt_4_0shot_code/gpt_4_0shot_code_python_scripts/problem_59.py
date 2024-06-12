
import numpy as np
from itertools import permutations

# Define the initial grid
grid = np.array([['x', 'x', 'x', 'x'],
                 ['37', 'x', '49', 'x'],
                 ['x', '44', 'x', 'x'],
                 ['42', 'x', '51', '61']])

# Define the range of numbers
numbers = list(map(str, range(24, 65)))

# Remove the numbers already in the grid from the list of numbers
for row in grid:
    for number in row:
        if number in numbers:
            numbers.remove(number)

# Generate all possible permutations of the remaining numbers
perms = list(permutations(numbers))

# Define a function to check if a list is strictly increasing or decreasing
def check_strictly_increasing_decreasing(lst):
    return (all(x<y for x, y in zip(lst, lst[1:])) or
            all(x>y for x, y in zip(lst, lst[1:])))

# Iterate over all permutations
for perm in perms:
    # Create a copy of the grid
    grid_copy = np.copy(grid)
    # Replace the 'x's with the numbers in the permutation
    for i, number in enumerate(perm):
        row, col = np.where(grid_copy == 'x')
        grid_copy[row[i]][col[i]] = number
    # Check if each row and column is strictly increasing or decreasing
    if (all(check_strictly_increasing_decreasing(row) for row in grid_copy) and
        all(check_strictly_increasing_decreasing(col) for col in grid_copy.T)):
        # If the grid is valid, calculate the sum of the top row, right column, and diagonal
        sum_top_row = sum(int(x) for x in grid_copy[0])
        sum_right_col = sum(int(x) for x in grid_copy[:, -1])
        sum_diag = sum(int(grid_copy[i][i]) for i in range(4))
        total_sum = sum_top_row + sum_right_col + sum_diag
        # If the total sum is minimal, store the grid and the total sum
        if 'min_sum' not in locals() or total_sum < min_sum:
            min_sum = total_sum
            min_grid = grid_copy

# Print the solution
solution = []
for i, number in enumerate(numbers):
    row, col = np.where(grid == 'x')
    solution.append((row[i], col[i], min_grid[row[i]][col[i]]))
print(solution)
