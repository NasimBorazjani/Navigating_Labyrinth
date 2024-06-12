
import itertools

# The grid with 'x's
grid = [['x', 'x', 'x'],
        ['x', 'x', 'x'],
        ['x', 'x', '57']]

# The given sums for the rows and columns
row_sums = [151, 154, 133]
col_sums = [154, 151, 133]

# The range of numbers to fill in the grid
num_range = range(35, 60)

# Function to get the diagonal elements
def get_diag(matrix):
    return [matrix[i][i] for i in range(len(matrix))]

# Function to check if a configuration is valid
def is_valid(grid, row_sums, col_sums):
    for i in range(len(grid)):
        if sum(grid[i]) != row_sums[i]:
            return False
        if sum(grid[j][i] for j in range(len(grid))) != col_sums[i]:
            return False
    if sum(get_diag(grid)) != col_sums[-1]:
        return False
    if sum(get_diag([list(reversed(row)) for row in grid])) != row_sums[-1]:
        return False
    return True

# Function to get the solutions
def get_solutions(grid, row_sums, col_sums, num_range):
    solutions = []
    for values in itertools.product(num_range, repeat=len(grid)):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 'x':
                    grid[i][j] = values[i*len(grid)+j]
        if is_valid(grid, row_sums, col_sums):
            solutions.append((grid[:]))
            for v in values:
                solutions[-1][solutions[-1].index('x')] = v
    return solutions

# Print the solutions
for solution in get_solutions(grid, row_sums, col_sums, num_range):
    print(solution)
