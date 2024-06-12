
def solve_magic_square(grid):
    def is_valid(row, col, num):
        # Check the number doesn't already exist in the row, column or square
        for i in range(4):
            if num == grid[row][i] or num == grid[i][col]:
                return False
        return True

    def solve(row, col, sum_rows, sum_cols, sum_diag):
        if row == 4:
            return True
        if col == 4:
            return solve(row + 1, 0, sum_rows, sum_cols, sum_diag)

        if grid[row][col] != 'x':
            return solve(row, col + 1, sum_rows, sum_cols, sum_diag)

        for num in range(11, 63):
            if is_valid(row, col, num):
                grid[row][col] = num
                new_sum_rows = sum_rows[:]
                new_sum_rows[row] -= num
                new_sum_cols = sum_cols[:]
                new_sum_cols[col] -= num
                new_sum_diag = sum_diag - num
                if col == row:
                    new_sum_diag = None
                if solve(row, col + 1, new_sum_rows, new_sum_cols, new_sum_diag):
                    return True

        # Backtrack
        grid[row][col] = 'x'
        return False

    solve_grid = [[None]*4 for _ in range(4)]
    solve_grid[1][1] = 52
    solve_grid[1][2] = 20
    solve_grid[2][0] = 41
    solve_grid[2][2] = 13
    solve_grid[3][1] = 54
    solve_grid[3][3] = 16
    solve_grid[3][0] = 11

    sum_rows = [None, 105, 115, None]
    sum_cols = [None, 148, 109, None]
    sum_diag = 134

    if not solve(0, 0, sum_rows, sum_cols, sum_diag):
        return None

    result = []
    for row in range(4):
        for col in range(4):
            if grid[row][col] != 'x':
                result.append((row, col, grid[row][col]))
    return result

print(solve_magic_square([['x', 'x', 'x', 'x'], ['x', '52', '20', 'x'], ['41', '13', 'x', 'x'], ['54', 'x', '16', '11']]))
