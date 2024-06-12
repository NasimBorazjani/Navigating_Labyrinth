
import itertools

# The grid with 'x's
grid = [['x', '20', 'x'],
        ['x', 'x', 'x'],
        ['x', 'x', '33']]

# The total for each row, column, and diagonal
totals = {'row0': 82, 'row1': 82, 'row2': 82,
          'col0': 82, 'col1': 82, 'col2': 82,
          'diag0': 96, 'diag1': 96}

# The range of numbers to fill in the grid
num_range = range(19, 44)

# Function to get the index of 'x' in the grid
def get_x_index(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'x':
                yield (i, j)

# Function to get the new grid with a combination of numbers
def get_new_grid(grid, combination):
    new_grid = grid.copy()
    for (i, j), num in zip(get_x_index(grid), combination):
        new_grid[i][j] = num
    return new_grid

# Function to check if the sums of the new grid meet the requirement
def check_grid(new_grid, totals):
    for i in range(len(new_grid)):
        if sum(new_grid[i]) != totals[f'row{i}']:
            return False
    for j in range(len(new_grid)):
        if sum(new_grid[i][j] for i in range(len(new_grid))) != totals[f'col{j}']:
            return False
    if sum(new_grid[i][i] for i in range(len(new_grid))) != totals['diag0']:
        return False
    if sum(new_grid[i][len(new_grid)-1-i] for i in range(len(new_grid))) != totals['diag1']:
        return False
    return True

# Get all possible combinations
combinations = list(itertools.product(num_range, repeat=len(list(get_x_index(grid)))))

# Get the valid grids
valid_grids = [get_new_grid(grid, combination) for combination in combinations if check_grid(get_new_grid(grid, combination), totals)]

# Get the grid with the minimum sum
min_sum_grid = min(valid_grids, key=lambda grid: sum(sum(row) for row in grid))

# Get the solution as a list of tuples
solution = [(i, j, num) for (i, j), num in zip(get_x_index(grid), min_sum_grid)]

print(solution)
