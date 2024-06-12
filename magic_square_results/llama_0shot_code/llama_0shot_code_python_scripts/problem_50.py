
def solve_magic_square(grid, row_sums, col_sums, diag_sum):
    def is_valid(row, col, num):
        # Check row
        if row_sums[row] is not None and grid[row][col] + num > row_sums[row]:
            return False
        # Check column
        if col_sums[col] is not None and sum(grid[i][col] + (num if i == row else 0) for i in range(4)) > col_sums[col]:
            return False
        # Check diagonal
        if row == col and sum(grid[i][i] + (num if i == row else 0) for i in range(4)) > diag_sum:
            return False
        return True

    def backtrack(row, col, sum_so_far):
        nonlocal best_sum, best_grid
        if sum_so_far > best_sum:
            return
        if row == 4:
            if col == 4:
                best_sum = sum_so_far
                best_grid = [list(row) for row in grid]
            else:
                backtrack(0, col + 1, sum_so_far)
        elif grid[row][col] == 'x':
            for num in range(9, 41):
                if is_valid(row, col, num):
                    grid[row][col] = num
                    backtrack(row + 1, col, sum_so_far + num)
                    grid[row][col] = 'x'
        else:
            backtrack(row + 1, col, sum_so_far + grid[row][col])

    best_sum = float('inf')
    best_grid = None
    backtrack(0, 0, 0)
    return [(row, col, val) for row in range(4) for col in range(4) if (row, col) != (3, 3) and (val := best_grid[row][col]) != 'x']

grid = [['x', 'x', 'x', '39'], ['28', 'x', 'x', 'x'], ['x', '11', '33', 'x'], ['18', '20', '38', '35']]
row_sums = [None, 114, None, None]
col_sums = [None, 77, 110, None]
diag_sum = 98

print(solve_magic_square(grid, row_sums, col_sums, diag_sum))
