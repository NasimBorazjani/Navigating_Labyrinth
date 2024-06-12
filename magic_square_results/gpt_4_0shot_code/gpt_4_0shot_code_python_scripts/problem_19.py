
import numpy as np
from itertools import combinations

# Define the grid
grid = np.array([[64, 78, 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']])

# Define the range of numbers
numbers = list(range(50, 85))

# Remove the numbers already in the grid from the list of numbers
for i in range(3):
    for j in range(3):
        if grid[i][j] != 'x':
            numbers.remove(grid[i][j])

# Generate all possible combinations of the remaining numbers
combinations = list(combinations(numbers, 6))

# Check each combination
for combination in combinations:
    # Create a copy of the grid
    grid_copy = np.copy(grid)
    
    # Fill the grid with the combination
    for i in range(3):
        for j in range(3):
            if grid_copy[i][j] == 'x':
                grid_copy[i][j] = combination[0]
                combination = combination[1:]
    
    # Check if the conditions are satisfied
    if np.sum(grid_copy[:, 0]) == 234 and np.sum(grid_copy[1, :]) == 201 and np.trace(grid_copy[::-1, :]) == 213:
        # If the conditions are satisfied, print the solution
        solution = []
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 'x':
                    solution.append((i, j, grid_copy[i][j]))
        print(solution)
        break
