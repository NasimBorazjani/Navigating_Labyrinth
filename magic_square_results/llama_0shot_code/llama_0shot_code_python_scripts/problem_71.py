
# Function to check if a number is valid in a cell
def is_valid(grid, row, col, num):
    # Check the number in the row
    for i in range(4):
        if grid[row][i] == num:
            return False

    # Check the number in the column
    for i in range(4):
        if grid[i][col] == num:
            return False

    # Check the number in the main diagonal
    if row == col:
        for i in range(4):
            if grid[i][i] == num:
                return False

    # Check the number in the counter diagonal
    if row + col == 3:
        for i in range(4):
            if grid[i][3 - i] == num:
                return False

    return True

# Function to solve the magic square
def solve_magic_square(grid):
    rows = [186, None, 174, None]
    cols = [None, 218, 203, None]
    diags = [221]
    total = sum(filter(None, rows + cols + diags))
    min_sum = total
    solutions = []

    def backtrack(grid, row, col, sum_row, sum_col, sum_diag):
        nonlocal min_sum
        if row == 4:
            if sum_row == rows[row] and sum_col == cols[col] and sum_diag == diags[0] and sum_row + sum_col - sum_diag == 0:
                if sum_row + sum_col + sum_diag < min_sum:
                    min_sum = sum_row + sum_col + sum_diag
                    solutions.clear()
                elif sum_row + sum_col + sum_diag == min_sum:
                    solutions.append((row, col, num))
            return
        if col == 4:
            backtrack(grid, row + 1, 0, sum_row - grid[row][col], sum_col, sum_diag - grid[row][col])
        else:
            for num in range(28, 65):
                if is_valid(grid, row, col, num):
                    grid[row][col] = num
                    backtrack(grid, row, col + 1, sum_row + num, sum_col + num, sum_diag + num)
                    grid[row][col] = 'x'

    backtrack(grid, 0, 0, 0, 0, 0)
    return solutions

# Test the function
grid = [['55', 'x', '53', 'x'],
        ['x', '50', '52', 'x'],
        ['x', 'x', 'x', '35'],
        ['x', '62', 'x', 'x']]

print(solve_magic_square(grid))
