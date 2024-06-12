
import itertools

# The initial grid with 'x's
grid = [['x', 'x', 'x'],
        ['x', 'x', 'x'],
        ['42', '45', 'x']]

# The given sums for the rows and columns
row_sums = [95, 115, 133]
col_sums = [115, 115, 133]

# The possible numbers to fill in the 'x's
numbers = list(range(48, 0, -1))

# The list to store the solutions
solutions = []

# Try every possible combination of numbers
for combination in itertools.permutations(numbers, 3):
    # Create a copy of the grid
    new_grid = [row.copy() for row in grid]
    
    # Fill in the 'x's with the numbers from the combination
    new_grid[0][0] = combination[0]
    new_grid[0][1] = combination[1]
    new_grid[0][2] = combination[2]
    
    # Calculate the sums for the rows and columns
    row_sums_new = [sum(row) for row in new_grid]
    col_sums_new = [sum(col) for col in zip(*new_grid)]
    
    # Check if the sums are as required
    if row_sums_new == row_sums and col_sums_new == col_sums:
        # Calculate the sum of the numbers in the grid
        grid_sum = sum(sum(row) for row in new_grid)
        # Add the configuration to the solutions
        solutions.append(((0, 0, combination[0]), (0, 1, combination[1]), (0, 2, combination[2]), grid_sum))

# Print the solutions
for solution in solutions:
    print(solution)
