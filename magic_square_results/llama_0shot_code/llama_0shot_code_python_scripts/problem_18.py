
import itertools

# The initial grid with 'x's
grid = [['x', 'x', 'x'],
        ['x', 'x', 'x'],
        ['x', '70', 'x']]

# The given sums for each row, column, and diagonal
row_sums = [194, 191, 186]
col_sums = [191, 194, 186]
diag_sum = 186

# The range of values that can be placed in the grid
values_range = range(48, 78)

# The best solution found so far
best_solution = None

# Try every possible combination of numbers in the given range
for combination in itertools.permutations(values_range, 3):
    # Create a copy of the grid
    new_grid = [row.copy() for row in grid]
    
    # Replace the 'x's with the numbers from the combination
    new_grid[0][0] = combination[0]
    new_grid[0][1] = combination[1]
    new_grid[0][2] = combination[2]
    
    # Calculate the sum of each row, column, and diagonal
    row_sums_new = [sum(row) for row in new_grid]
    col_sums_new = [sum(col) for col in zip(*new_grid)]
    diag_sum_new = new_grid[0][2] + new_grid[1][1] + new_grid[2][0]
    
    # Check if the conditions are met
    if row_sums_new == row_sums and col_sums_new == col_sums and diag_sum_new == diag_sum:
        # If this is the first solution or it has a lower sum than the best solution so far,
        # store it as the best solution
        if best_solution is None or sum(new_grid) < sum(best_solution[0]):
            best_solution = [(combination[0], 0, 0), (combination[1], 0, 1), (combination[2], 0, 2)]

# Print the best solution
print(best_solution)
