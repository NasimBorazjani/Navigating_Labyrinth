
import numpy as np
import itertools

# Define the grid
grid = np.array([['x', 'x', 'x'], ['x', 'x', 'x'], ['40', 'x', '71']])

# Define the range of numbers
numbers = list(range(40, 90))

# Remove the numbers already in the grid from the list of numbers
for i in range(3):
    for j in range(3):
        if grid[i][j] != 'x':
            numbers.remove(int(grid[i][j]))

# Generate all possible combinations of the remaining numbers
combinations = list(itertools.permutations(numbers, 6))

# Check each combination
for combination in combinations:
    # Fill the grid with the current combination
    temp_grid = grid.copy()
    k = 0
    for i in range(3):
        for j in range(3):
            if temp_grid[i][j] == 'x':
                temp_grid[i][j] = str(combination[k])
                k += 1

    # Check if the conditions are satisfied
    if np.sum(temp_grid.astype(int), axis=0)[0] == 183 and np.sum(temp_grid.astype(int), axis=1)[1] == 194 and np.trace(temp_grid.astype(int)[::-1]) == 161:
        # If the conditions are satisfied, print the solution
        solution = []
        k = 0
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 'x':
                    solution.append((i, j, combination[k]))
                    k += 1
        print(solution)
        break
