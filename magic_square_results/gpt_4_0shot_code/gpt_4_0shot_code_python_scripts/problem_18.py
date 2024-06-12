
import numpy as np
import itertools

# Define the grid
grid = np.array([['x', 'x', 'x'], ['x', 'x', 'x'], ['x', '70', 'x']])

# Define the range of numbers
numbers = list(range(48, 78))

# Remove the known numbers from the list
numbers.remove(70)

# Generate all possible combinations of the remaining numbers
combinations = list(itertools.combinations(numbers, 8))

# Define the target sums
target_sums = [191, 194, 186]

# Iterate over all combinations
for combination in combinations:
    # Create a copy of the grid
    grid_copy = np.copy(grid)
    
    # Replace the 'x's with the numbers in the combination
    for i, number in enumerate(combination):
        grid_copy[grid_copy == 'x'] = number
    
    # Check if the sums of the specified rows, columns, and diagonal are correct
    if np.sum(grid_copy[:, 0]) == target_sums[0] and np.sum(grid_copy[1, :]) == target_sums[1] and np.sum(grid_copy.diagonal()[::-1]) == target_sums[2]:
        # If the sums are correct, print the solution
        print(grid_copy)
        break
