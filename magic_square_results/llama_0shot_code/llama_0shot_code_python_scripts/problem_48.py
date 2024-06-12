
def solve_magic_square(grid):
    def is_valid(row, col, num):
        # Check row
        if grid[row][col] != 'x' and grid[row][col] != num:
            return False
        for i in range(4):
            if grid[row][i] == num:
                return False
        for i in range(4):
            if grid[i][col] == num:
                return False
        # Check diagonal
        if row == col:
            for i in range(4):
                if grid[i][i] == num:
                    return False
        if row == 3 - col:
            for i in range(4):
                if grid[i][3 - i] == num:
                    return False
        return True

    def backtrack(row, col, sum_rows, sum_cols, sum_diag):
        if row == 4:
            return sum_rows == [None, 179, 190, None] and \
                   sum_cols == [None, 179, 194, None] and \
                   sum_diag == 205
        if col == 4:
            return backtrack(row + 1, 0, sum_rows, sum_cols, sum_diag)
        if grid[row][col] != 'x':
            return backtrack(row, col + 1, sum_rows, sum_cols, sum_diag)

        for num in range(34, 61):
            if is_valid(row, col, num):
                grid[row][col] = num
                if row == col:
                    sum_diag -= num
                if row == 3 - col:
                    sum_diag -= num
                if row in (0, 1):
                    sum_rows[row] -= num
                if col in (0, 1):
                    sum_cols[col] -= num
                if backtrack(row, col + 1, sum_rows, sum_cols, sum_diag):
                    return True
                grid[row][col] = 'x'
                if row == col:
                    sum_diag += num
                if row == 3 - col:
                    sum_diag += num
                if row in (0, 1):
                    sum_rows[row] += num
                if col in (0, 1):
                    sum_cols[col] += num
        return False

    if not backtrack(0, 0, [None, 179, 190, None], [None, 179, 194, None], 205):
        return None
    result = []
    for row in range(4):
        for col in range(4):
            if grid[row][col] != 'x':
                result.append((row, col, grid[row][col]))
    return result

grid = [['x', 'x', 'x', 'x'],
        ['x', '46', 'x', '41'],
        ['x', '57', '55', 'x'],
        ['x', '37', 'x', 'x']]

print(solve_magic_square(grid))
