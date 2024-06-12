
import itertools

# The initial grid with 'x'
grid = [['35', 'x', '46'], ['x', 'x', 'x'], ['x', 'x', 'x']]

# The given sums for each row and column and the diagonal
row_sums = [103, 107, 124]
col_sums = [107, 103, 124]

# The list of numbers from 29 to 48
numbers = list(map(str, range(29, 49)))

# Function to calculate the sum of a row or a column
def calc_sum(row_col):
    return sum(map(int, row_col))

# Function to check if a combination is valid
def is_valid(combination):
    new_grid = []
    for i, row in enumerate(grid):
        new_row = []
        for j, val in enumerate(row):
            if val == 'x':
                new_row.append(combination.pop(0))
            else:
                new_row.append(val)
        new_grid.append(new_row)

    for i, row in enumerate(new_grid):
        if calc_sum(row) != row_sums[i]:
            return False

    for i, col in enumerate(zip(*new_grid)):
        if calc_sum(col) != col_sums[i]:
            return False

    if calc_sum(new_grid[0]) != calc_sum(new_grid[2]):
        return False

    return True

# Function to find the combination with the smallest sum
def find_combination():
    min_sum = float('inf')
    best_combination = None
    for combination in itertools.combinations(numbers, 5):
        if is_valid(list(combination)):
            combination_sum = sum(map(int, combination))
            if combination_sum < min_sum:
                min_sum = combination_sum
                best_combination = combination
    return best_combination

# Function to create the output format
def create_output(combination):
    output = []
    for i, val in enumerate(combination):
        row, col = divmod(i, 3)
        output.append((row, col, int(val)))
    return output

# Find the best combination and create the output
combination = find_combination()
output = create_output(combination)
print(output)
