
import itertools

# The grid with 'x's
grid = [['x', '46', 'x'],
        ['39', 'x', 'x'],
        ['x', 'x', 'x']]

# The sums for each row, column, and diagonal
row_sums = [124, 126, 136]
col_sums = [126, 124, 136]
diag_sum = 136

# The range of numbers to fill in the grid
num_range = range(28, 58)

# Function to get the index of 'x' in the grid
def get_x_index(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'x':
                yield (i, j)

# Function to get the sum of each row, column, and diagonal
def get_sums(grid):
    rows = [sum(row) for row in grid]
    cols = [sum(grid[i][j] for i in range(len(grid))) for j in range(len(grid[0]))]
    diag1 = sum(grid[i][i] for i in range(len(grid)))
    diag2 = sum(grid[i][len(grid)-1-i] for i in range(len(grid)))
    return rows, cols, diag1 + diag2

# Function to check if the sums are correct
def check_sums(grid, row_sums, col_sums, diag_sum):
    grid_sums = get_sums(grid)
    return grid_sums == (row_sums, col_sums, diag_sum)

# Function to solve the problem
def solve(grid, row_sums, col_sums, diag_sum, num_range):
    solutions = []
    for nums in itertools.permutations(num_range, len(list(get_x_index(grid)))):
        new_grid = grid.copy()
        for (i, j), num in zip(get_x_index(new_grid), nums):
            new_grid[i][j] = num
        if check_sums(new_grid, row_sums, col_sums, diag_sum):
            solutions.append(new_grid)
    return solutions

# Print the solutions
for solution in solve(grid, row_sums, col_sums, diag_sum, num_range):
    print(solution)
