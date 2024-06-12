
import numpy as np

# Define the initial grid
grid = np.array([['33', '37', 'x', '58'],
                 ['44', '51', 'x', '63'],
                 ['x', '52', '62', '64'],
                 ['x', 'x', '65', 'x']])

# Define the range of possible numbers
numbers = set(map(str, range(33, 79)))

# Remove the numbers already in the grid from the set of possible numbers
for row in grid:
    for number in row:
        if number != 'x':
            numbers.remove(number)

# Convert the numbers back to integers and sort them
numbers = sorted(map(int, numbers))

# Define the positions of the 'x's
positions = [(i, j) for i in range(4) for j in range(4) if grid[i, j] == 'x']

# Define the function to check if a grid is valid
def is_valid(grid):
    for i in range(4):
        row = [int(x) for x in grid[i, :] if x != 'x']
        if row != sorted(row) and row != sorted(row, reverse=True):
            return False
        column = [int(x) for x in grid[:, i] if x != 'x']
        if column != sorted(column) and column != sorted(column, reverse=True):
            return False
    return True

# Try all possible combinations of numbers
from itertools import permutations
for perm in permutations(numbers, len(positions)):
    # Create a copy of the grid
    grid_copy = np.copy(grid)
    # Replace the 'x's with the numbers
    for (i, j), number in zip(positions, perm):
        grid_copy[i, j] = str(number)
    # Check if the grid is valid
    if is_valid(grid_copy):
        # Calculate the sum of the top row, right column, and diagonal
        sum_top_row = sum(map(int, grid_copy[0, :]))
        sum_right_column = sum(map(int, grid_copy[:, -1]))
        sum_diagonal = sum(int(grid_copy[i, i]) for i in range(4))
        total_sum = sum_top_row + sum_right_column + sum_diagonal
        # If the total sum is minimal, print the solution
        if total_sum == min_sum:
            solution = [(i, j, number) for (i, j), number in zip(positions, perm)]
            print(solution)
