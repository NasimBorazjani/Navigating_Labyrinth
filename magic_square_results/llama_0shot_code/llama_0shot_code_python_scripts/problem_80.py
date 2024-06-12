
def solve_magic_square(grid):
    numbers = list(range(35, 77))
    rows = [None, 231, 259, None]
    cols = [None, 247, 236, None]
    diag = 234
    solution = []

    def backtrack(row, col, nums):
        if row == 4:
            return True
        if col == 4:
            return backtrack(row + 1, 0, nums)
        if grid[row][col] != 'x':
            return backtrack(row, col + 1, nums)

        for num in nums:
            grid[row][col] = num
            row_sum = sum(grid[row])
            col_sum = sum(grid[i][col] for i in range(4))
            diag_sum = grid[0][0] + grid[1][1] + grid[2][2] + grid[3][3]

            if (rows[row] == row_sum == col_sum == diag_sum == diag) or \
               (rows[row] == row_sum == col_sum == diag_sum - num) or \
               (rows[row] == row_sum == col_sum - num == diag_sum) or \
               (rows[row] == row_sum - num == col_sum == diag_sum) or \
               (rows[row] == row_sum == col_sum == diag_sum + num) or \
               (rows[row] == row_sum == col_sum + num == diag_sum) or \
               (rows[row] == row_sum + num == col_sum == diag_sum) or \
               (rows[row] == row_sum == col_sum + num == diag_sum - num) or \
               (rows[row] == row_sum + num == col_sum - num == diag_sum) or \
               (rows[row] == row_sum - num == col_sum + num == diag_sum) or \
               (rows[row] == row_sum + num == col_sum + num == diag_sum + num):

                if backtrack(row, col + 1, [n for n in nums if n != num]):
                    solution.append((row, col, num))
                    return True
                grid[row][col] = 'x'
        return False

    backtrack(0, 0, numbers)
    return solution

grid = [['x', 'x', 'x', '60'],
        ['72', 'x', 'x', 'x'],
        ['63', '70', 'x', 'x'],
        ['61', '75', 'x', 'x']]

print(solve_magic_square(grid))
