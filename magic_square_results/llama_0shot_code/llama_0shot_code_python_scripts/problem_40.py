
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

        # Check if number already exists in the grid
        for r, row_data in enumerate(grid):
            for c, val in enumerate(row_data):
                if val == num:
                    return False

        return True

    def backtrack(row, col, nums_left):
        if nums_left == 0:
            return True, grid

        if row == len(grid):
            row, col = 0, col + 1

        if col == len(grid):
            return backtrack(row + 1, 0, nums_left)

        if grid[row][col] != 'x':
            return backtrack(row, col + 1, nums_left)

        for num in range(24, 51):
            if is_valid(row, col, num):
                grid[row][col] = num
                new_row_sums = [sums - num if sums is not None else None for sums in row_sums]
                new_col_sums = [sums - num if sums is not None else None for sums in col_sums]
                new_diag_sum = diag_sum - num if diag_sum is not None else None

                success, result = backtrack(row, col + 1, nums_left - 1)
                if success:
                    return True, result

                grid[row][col] = 'x'
                row_sums[:] = new_row_sums
                col_sums[:] = new_col_sums
                diag_sum = new_diag_sum

        return False, []

    nums_left = grid[0].count('x')
    success, result = backtrack(0, 0, nums_left)
    return result if success else "No solution found"


grid = [['38', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x'],
        ['x', '39', '40', '27'],
        ['32', '46', 'x', '25']]

row_sums = [None, 135, None]
col_sums = [None, 149, 178, None]
diag_sum = 151

result = solve_magic_square(grid, row_sums, col_sums, diag_sum)
print(result)
