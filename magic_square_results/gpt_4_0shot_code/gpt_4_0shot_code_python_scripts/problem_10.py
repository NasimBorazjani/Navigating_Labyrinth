
import numpy as np
import itertools

# Define the grid
grid = np.array([['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', '57']])

# Define the range of numbers
numbers = list(range(35, 59))

# Remove the known number from the list
numbers.remove(57)

# Generate all possible combinations of the remaining numbers
combinations = list(itertools.permutations(numbers, 8))

# Define the target sums
target_sums = [154, 151, 133]

# Iterate over all combinations
for combination in combinations:
    # Fill the grid with the current combination
    temp_grid = grid.copy()
    temp_grid[temp_grid == 'x'] = combination

    # Convert the grid to integers
    temp_grid = temp_grid.astype(int)

    # Check if the sums match the target sums
    if np.sum(temp_grid[:, 0]) == target_sums[0] and np.sum(temp_grid[1, :]) == target_sums[1] and np.sum(np.diag(np.fliplr(temp_grid))) == target_sums[2]:
        # If the sums match, print the solution
        solution = [(i, j, temp_grid[i, j]) for i in range(3) for j in range(3) if grid[i, j] == 'x']
        print(solution)
        break
