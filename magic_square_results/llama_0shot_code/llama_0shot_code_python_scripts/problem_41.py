
# Define the grid and the constraints
grid = [['x', 'x', '40', 'x'],
        ['x', '31', 'x', '43'],
        ['37', 'x', 'x', '32'],
        ['34', '29', 'x', 'x']]

rows_constraints = [None, 125, None, 164]
cols_constraints = [None, 135, 160, None]
diag_constraint = 146

# Function to calculate the sum of a row or column
def calc_sum(lst):
    return sum([val if val != 'x' else 0 for val in lst])

# Function to place a number and update the sums
def place_num(row, col, num):
    grid[row][col] = num
    rows[row] -= num
    cols[col] -= num
    if row == col:
        diagonal -= num
    if row == len(grid) - col - 1:
        anti_diagonal -= num

# Function to remove a number and restore the sums
def remove_num(row, col, num):
    grid[row][col] = 'x'
    rows[row] += num
    cols[col] += num
    if row == col:
        diagonal += num
    if row == len(grid) - col - 1:
        anti_diagonal += num

# Recursive function to fill the grid
def solve(pos):
    row, col = divmod(pos, len(grid))
    if grid[row][col] != 'x':
        return solve(pos + 1)
    for num in range(24, 51):
        if num not in rows[row] and num not in cols[col]:
            place_num(row, col, num)
            if solve(pos + 1):
                return True
            remove_num(row, col, num)
    return False

# Initialize the sums
rows = [calc_sum(row) for row in grid]
cols = [calc_sum(col) for col in zip(*grid)]
diagonal = calc_sum(diagonal_positions(grid))
anti_diagonal = calc_sum(anti_diagonal_positions(grid))

# Solve the problem
solve(0)

# Print the result
for row in grid:
    print(row)
