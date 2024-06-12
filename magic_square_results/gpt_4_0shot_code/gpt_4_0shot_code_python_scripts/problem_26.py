
import numpy as np
import itertools

# Define the grid
grid = np.array([['x', 'x', 'x'], ['x', 'x', 'x'], ['x', '32', 'x']])

# Define the range of numbers
numbers = list(range(26, 66))

# Remove the numbers already in the grid from the list of numbers
for row in grid:
    for num in row:
        if num != 'x':
            numbers.remove(int(num))

# Generate all possible combinations of the remaining numbers
combinations = list(itertools.permutations(numbers, 6))

# Define the sums for the rows, columns and diagonal
sums = {'row1': 135, 'col1': 150, 'diag': 119}

# Iterate over all combinations
for combination in combinations:
    # Create a copy of the grid
    grid_copy = np.copy(grid)
    
    # Replace the 'x's in the grid with the numbers in the combination
    grid_copy[grid_copy == 'x'] = combination
    
    # Convert the elements in the grid to integers
    grid_copy = grid_copy.astype(int)
    
    # Check if the sums of the rows, columns and diagonal match the given sums
    if np.sum(grid_copy[1, :]) == sums['row1'] and np.sum(grid_copy[:, 1]) == sums['col1'] and np.trace(grid_copy[::-1, :]) == sums['diag']:
        # If they match, print the combination and break the loop
        print([(i, j, grid_copy[i, j]) for i in range(3) for j in range(3) if grid[i, j] == 'x'])
        break
