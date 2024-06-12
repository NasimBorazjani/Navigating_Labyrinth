
from itertools import permutations

# The grid with missing values represented as 'x'
grid = [['25', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]

# The given sums for the rows and columns
row_sums = [86, 99, 76]
col_sums = [99, 86, 76]

# The range of possible numbers to fill in the grid
num_range = range(20, 40)

# The best solution found so far
best_solution = None

# Generate all possible permutations of the numbers in the range
for perm in permutations(num_range):
    # Create a copy of the grid
    new_grid = [row.copy() for row in grid]
    
    # Fill in the missing values in the grid with the numbers from the permutation
    perm_iter = iter(perm)
    for row in range(3):
        for col in range(3):
            if new_grid[row][col] == 'x':
                new_grid[row][col] = next(perm_iter)
    
    # Check if the sums of the specified rows, columns, and diagonal match the given amounts
    if (sum(new_grid[0]) == row_sums[0] and
        sum(new_grid[1]) == row_sums[1] and
        sum(new_grid[2]) == row_sums[2] and
        sum(new_grid[0][i] for i in range(3)) == col_sums[0] and
        sum(new_grid[1][i] for i in range(3)) == col_sums[1] and
        sum(new_grid[2][i] for i in range(3)) == col_sums[2] and
        new_grid[0][0] + new_grid[1][1] + new_grid[2][2] == col_sums[2]):
        
        # If this is the first solution or the sum of all the numbers in the grid is lower than
        # the sum of all the numbers in the best solution so far, update the best solution
        if (best_solution is None or
            sum(map(int, sum(new_grid, []))) < sum(map(int, sum(best_solution, [])))):
            best_solution = new_grid

# Convert the best solution to the required format and print it
best_solution = [(row, col, int(val)) for row, row_vals in enumerate(best_solution) for col, val in enumerate(row_vals) if val != 'x']
print(best_solution)
