
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

        # Check grid
        for r in range(4):
            for c in range(4):
                if grid[r][c] == num:
                    return False

        return True

    def backtrack(row, col, num_list):
        if row == 4:
            return num_list

        if col == 4:
            return backtrack(row + 1, 0, num_list)

        if grid[row][col] != 'x':
            return backtrack(row, col + 1, num_list)

        for num in range(35, 62):
            if is_valid(row, col, num):
                num_list.append((row, col, num))
                grid[row][col] = num

                new_num_list = backtrack(row, col + 1, num_list)
                if new_num_list is not None:
                    return new_num_list

                num_list.pop()
                grid[row][col] = 'x'

        return None

    return backtrack(0, 0, [])


grid = [['x', '50', 'x', 'x'],
        ['58', 'x', 'x', 'x'],
        ['x', '49', 'x', '59'],
        ['39', '41', 'x', 'x']]

row_sums = [None, 183, None, None]
col_sums = [None, 177, 196, None]
diag_sum = 188

result = solve_magic_square(grid, row_sums, col_sums, diag_sum)
print(result)
