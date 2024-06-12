
def solve_magic_square(grid, row_sums, col_sums, diag_sum):
    def is_valid(row, col, num):
        # Check row
        if row_sums[row] is not None and row_sums[row] - num < 0:
            return False

        # Check column
        if col_sums[col] is not None and col_sums[col] - num < 0:
            return False

        # Check diagonal
        if row == col and diag_sum - num < 0:
            return False

        # Check if number already exists in row or column
        for r in range(4):
            if grid[r][col] == str(num):
                return False
        for c in range(4):
            if grid[row][c] == str(num):
                return False

        return True

    def backtrack(row, col, min_num, max_num):
        if row == 4:
            return True
        if col == 4:
            return backtrack(row + 1, 0, min_num, max_num)

        if grid[row][col] != 'x':
            return backtrack(row, col + 1, min_num, max_num)

        for num in range(max_num, min_num - 1, -1):
            if is_valid(row, col, num):
                grid[row][col] = str(num)
                if backtrack(row, col + 1, min_num, num - 1):
                    return True
                grid[row][col] = 'x'
        return False

    min_num, max_num = 36, 92
    backtrack(0, 0, min_num, max_num)

    result = []
    for row in range(4):
        for col in range(4):
            if grid[row][col] != 'x':
                result.append((row, col, int(grid[row][col])))
    return result

grid = [['44', 'x', 'x', 'x'],
        ['90', '52', 'x', '91'],
        ['x', '58', 'x', '62'],
        ['x', '80', 'x', 'x']]

row_sums = [None, 315, None, None]
col_sums = [None, 279, 306, None]
diag_sum = 264

print(solve_magic_square(grid, row_sums, col_sums, diag_sum))
