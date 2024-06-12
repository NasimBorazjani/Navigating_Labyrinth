
import numpy as np
from itertools import permutations

# Define the grid
grid = np.array([['x', 'x', 48],
                 ['x', 'x', 'x'],
                 ['x', 'x', 'x']])

# Define the range of numbers
numbers = list(range(35, 60))

# Remove the numbers already in the grid
numbers.remove(48)

# Generate all possible combinations of the remaining numbers
combinations = permutations(numbers, 8)

# Check each combination
for combination in combinations:
    # Fill the grid with the current combination
    temp_grid = grid.copy()
    temp_grid[temp_grid == 'x'] = combination

    # Convert the grid to integers
    temp_grid = temp_grid.astype(int)

    # Check the conditions
    if np.sum(temp_grid[:, 0]) == 127 and np.sum(temp_grid[1, :]) == 144 and np.trace(temp_grid[::-1, :]) == 141:
        # If the conditions are met, print the solution
        solution = []
        for i in range(3):
            for j in range(3):
                if grid[i, j] == 'x':
                    solution.append((i, j, temp_grid[i, j]))
        print(solution)
        break
