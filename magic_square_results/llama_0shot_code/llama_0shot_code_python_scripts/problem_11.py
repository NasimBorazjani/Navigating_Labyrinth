
from itertools import product

# The grid with 'x's
grid = [['x', 'x', '48'],
        ['x', 'x', 'x'],
        ['x', 'x', 'x']]

# The range of numbers
numbers = range(35, 60)

# The indices of the 'x's in the grid
empty_places = [(i, j) for i, row in enumerate(grid) for j, x in enumerate(row) if x == 'x']

# All possible combinations of numbers to fill the empty places
combinations = product(numbers, repeat=len(empty_places))

# The solutions
solutions = []

# Check each combination
for combination in combinations:
    # Create a copy of the grid
    new_grid = [row.copy() for row in grid]
    # Fill in the empty places with the numbers from the combination
    for (i, j), num in zip(empty_places, combination):
        new_grid[i][j] = num
    # Check if the sums of the rows, columns, and diagonals are as required
    if (sum(new_grid[0]) == 144 and
            sum(new_grid[1]) == 127 and
            sum(new_grid[2]) == 127 and
            sum(new_grid[i][i] for i in range(3)) == 141):
        # If they are, add this configuration to the solutions
        solutions.append((combination, sum(map(sum, new_grid))))

# Return the solution with the smallest sum of all numbers in the grid
if solutions:
    solutions.sort(key=lambda x: x[1])
    print(solutions[0][0])
else:
    print("No solution found")
