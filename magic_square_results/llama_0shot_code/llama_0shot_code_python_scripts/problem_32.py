
import itertools

# The grid with 'x's
grid = [['x', 'x', 'x'],
        ['x', 'x', 'x'],
        ['41', 'x', 'x']]

# The given sums for the rows and columns
row_sums = [134, 135, 122]
col_sums = [135, 134, 122]

# The range of numbers to fill in the grid
num_range = range(31, 76)

# Function to get the diagonal elements
def get_diag(matrix):
    return [matrix[i][i] for i in range(len(matrix))]

# Function to check if a configuration is valid
def is_valid(grid, row_sums, col_sums):
    for i in range(len(grid)):
        if sum(int(x) for x in grid[i]) != row_sums[i]:
            return False
        if sum(int(x[i]) for x in grid) != col_sums[i]:
            return False
    if sum(get_diag(grid)) != col_sums[0]:  # The sum of the diagonal
        return False
    return True

# Function to get the solutions
def get_solutions(grid, row_sums, col_sums, num_range):
    solutions = []
    for combination in itertools.product(num_range, repeat=len(grid)):
        # Replace the 'x's with the numbers in the combination
        new_grid = [[str(combination[i*3 + j]) if x == 'x' else x for j, x in enumerate(row)] for i, row in enumerate(grid)]
        if is_valid(new_grid, row_sums, col_sums):
            # Add the configuration to the solutions
            solutions.append((combination[0], 0, 0, combination[1], 1, 0, combination[2], 2, 0))
    return solutions

print(get_solutions(grid, row_sums, col_sums, num_range))
