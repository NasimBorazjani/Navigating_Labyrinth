
import itertools

# Problem constraints
row_sums = [None, 247, 238, None]
col_sums = [None, 188, 234, None]
diag_sum = 215

# Empty grid
grid = [['61', 'x', '50', 'x'],
        ['x', 'x', 'x', 'x'],
        ['68', '40', '57', 'x'],
        ['x', '42', 'x', 'x']]

# Function to calculate the sum of each row, column, and diagonal
def calc_sums(grid):
    row_sums_res = [sum(map(int, row)) for row in grid]
    col_sums_res = [sum(map(int, col)) for col in zip(*grid)]
    diag_sum_res = sum(map(int, [grid[i][i] for i in range(4)])) + sum(map(int, [grid[i][3 - i] for i in range(4)])) - 2 * int(grid[2][2])
    return row_sums_res, col_sums_res, diag_sum_res

# Replace 'x' with a number from the range [35, 76]
grid = [[val if val != 'x' else str(num) for val in row] for row in grid for num in range(35, 77) if num not in map(int, row)]

# Initialize the minimum sum and result
min_sum = float('inf')
result = None

# Loop through each possible grid
for grid_perm in itertools.product(*grid):
    grid_new = [list(map(str, row)) for row in zip(*grid_perm)]
    row_sums_new, col_sums_new, diag_sum_new = calc_sums(grid_new)
    
    # Check if the sums match the problem constraints
    if row_sums_new == row_sums and col_sums_new == col_sums and diag_sum_new == diag_sum:
        # Calculate the total sum
        total_sum = sum(map(int, [val for sublist in grid_new for val in sublist]))
        
        # Update the minimum sum and result
        if total_sum < min_sum:
            min_sum = total_sum
            result = [(row_idx, col_idx, int(val)) for row_idx, row in enumerate(grid_new) for col_idx, val in enumerate(row) if val != 'x']

# Print the result
print(result)
