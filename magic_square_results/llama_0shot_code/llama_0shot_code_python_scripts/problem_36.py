
import itertools

# The initial grid with 'x's
grid = [['x', 'x', 'x'],
        ['x', 'x', 'x'],
        ['69', '71', 'x']]

# The given sums for the rows and columns
row_sums = [152, 198, 195]
col_sums = [198, 152, 195]

# The range of possible numbers to fill in the 'x's
num_range = range(40, 90)

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
    if sum(get_diag(grid)) != row_sums[2]:
        return False
    if sum(get_diag([list(reversed(row)) for row in grid])) != col_sums[2]:
        return False
    return True

# Function to solve the problem
def solve(grid, row_sums, col_sums, num_range):
    solutions = []
    for values in itertools.product(num_range, repeat=3):
        new_grid = [row[:] for row in grid]
        new_grid[2][0] = values[0]
        new_grid[1][1] = values[1]
        new_grid[0][2] = values[2]
        if is_valid(new_grid, row_sums, col_sums):
            solutions.append(((0, 0, values[0]), (0, 1, values[1]), (0, 2, values[2])))
    return solutions

print(solve(grid, row_sums, col_sums, num_range))
