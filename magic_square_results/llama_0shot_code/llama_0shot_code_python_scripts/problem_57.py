
def solve_magic_square(grid):
    def is_valid(row, col, num):
        # Check the number doesn't exist in the same row or column
        for i in range(4):
            if grid[row][i] == str(num) or grid[i][col] == str(num):
                return False

        # Check the number doesn't exist in the same 3x3 box
        start_row, start_col = row - row % 3, col - col % 3
        for i in range(3):
            for j in range(3):
                if grid[i + start_row][j + start_col] == str(num):
                    return False

        return True

    def backtrack(row, col, sum_rows, sum_cols, sum_diag):
        if row == 4:
            return True

        if col == 4:
            return backtrack(row + 1, 0, sum_rows, sum_cols, sum_diag)

        if grid[row][col] != 'x':
            return backtrack(row, col + 1, sum_rows, sum_cols, sum_diag)

        for num in range(28, 60):
            if is_valid(row, col, num):
                grid[row][col] = num
                new_sum_rows = sum_rows[:]
                new_sum_cols = sum_cols[:]
                new_sum_diag = sum_diag

                new_sum_rows[row] += num
                new_sum_cols[col] += num
                if row == col:
                    new_sum_diag += num

                if backtrack(row, col + 1, new_sum_rows, new_sum_cols, new_sum_diag):
                    return True

                grid[row][col] = 'x'

        return False

    sums = [None, 170, 162, None]
    backtrack(0, 0, sums, sums, 171)

    result = []
    for row in range(4):
        for col in range(4):
            if grid[row][col] != 'x':
                result.append((row, col, int(grid[row][col])))

    return result

grid = [['42', 'x', '41', 'x'],
        ['x', '48', 'x', 'x'],
        ['x', '39', '30', '52'],
        ['x', 'x', '40', 'x']]

print(solve_magic_square(grid))
