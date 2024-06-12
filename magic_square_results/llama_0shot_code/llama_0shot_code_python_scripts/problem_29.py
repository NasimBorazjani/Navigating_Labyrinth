
from itertools import combinations

# The initial grid with 'x' values
grid = [['x', '77', 'x'], ['49', 'x', 'x'], ['x', 'x', 'x']]

# The given sums for each row and column
row_sums = [156, 180, 127]
col_sums = [180, 156, 127]

# The range of numbers to fill in the grid
num_range = range(34, 79)

# Function to get the index of 'x' in the grid
def get_x_index(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'x':
                yield (i, j)

# Function to check if the conditions are met
def check_conditions(grid, row_sums, col_sums):
    for i in range(len(grid)):
        if sum(int(val) for val in grid[i] if val != 'x') != row_sums[i]:
            return False
    for i in range(len(grid)):
        if sum(int(val[i]) for val in grid if val != 'x') != col_sums[i]:
            return False
    if sum(grid[i][i] for i in range(len(grid))) != col_sums[-1]:
        return False
    if sum(grid[i][-i-1] for i in range(len(grid))) != row_sums[-1]:
        return False
    return True

# Function to solve the problem
def solve_problem(grid, row_sums, col_sums, num_range):
    best_solution = None
    for nums in combinations(map(str, num_range), len(list(get_x_index(grid)))):
        new_grid = grid.copy()
        x_index = list(get_x_index(new_grid))
        for num, (i, j) in zip(nums, x_index):
            new_grid[i][j] = num
        if check_conditions(new_grid, row_sums, col_sums):
            new_sum = sum(int(val) for row in new_grid for val in row if val != 'x')
            if best_solution is None or new_sum < best_solution[0]:
                best_solution = (new_sum, sorted((i, j, int(num)) for (i, j), num in zip(x_index, nums)))
    return best_solution

print(solve_problem(grid, row_sums, col_sums, num_range))
