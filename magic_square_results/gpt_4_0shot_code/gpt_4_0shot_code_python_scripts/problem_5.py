
import numpy as np
import itertools

# Define the grid
grid = np.array([['x', 'x', 'x'], ['x', 'x', 'x'], [22, 'x', 'x']])

# Define the range of numbers
numbers = list(range(20, 40))

# Remove the known number from the list
numbers.remove(22)

# Generate all possible combinations of the remaining numbers
combinations = list(itertools.permutations(numbers, 6))

# Define the solution list
solution = []

# Iterate over all combinations
for combination in combinations:
    # Fill the grid with the current combination
    temp_grid = grid.copy()
    temp_grid[temp_grid == 'x'] = combination

    # Convert the grid to integers
    temp_grid = temp_grid.astype(int)

    # Check if the conditions are satisfied
    if np.sum(temp_grid[1, :]) == 82 and np.sum(temp_grid[:, 0]) == 82 and np.sum(np.diag(np.fliplr(temp_grid))) == 82:
        # If the conditions are satisfied, add the combination to the solution list
        solution.append(combination)

# Print the solution
for i in range(len(solution)):
    print([(0, j, solution[i][j]) for j in range(3)] + [(1, j, solution[i][j+3]) for j in range(3)] + [(2, 0, 22)])
