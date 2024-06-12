
def solve_magic_square(grid, row_sums, col_sums, diag_sum):
    def is_valid(row, col, num):
        # Check the number doesn't exist in the same row, column or diagonal
        for i in range(4):
            if grid[row][i] == num or grid[i][col] == num:
                return False
        if row == col:
            for i in range(4):
                if grid[i][i] == num:
                    return False
        if row + col == 3:
            for i in range(4):
                if grid[i][3 - i] == num:
                    return False
        return True

    def backtrack(row, col, sum_):
        if row == 4:
            return sum_ == diag_sum
        if col == 4:
            return backtrack(row + 1, 0, sum_)
        if grid[row][col] == 'x':
            for num in range(34, 61):
                if is_valid(row, col, num):
                    grid[row][col] = num
                    new_sum = sum_ + num
                    if (col == 3 and row_sums[row] == new_sum) or \
                       (row == 3 and col_sums[col] == new_sum) or \
                       (row == col and new_sum == diag_sum):
                        if backtrack(row, col + 1, new_sum):
                            return True
                    grid[row][col] = 'x'
            return False
        else:
            return backtrack(row, col + 1, sum_)

    if backtrack(0, 0, 0):
        result = [(i, j, int(grid[i][j])) for i in range(4) for j in range(4) if grid[i][j] != 'x']
        return result
    else:
        return None

grid = [['37', 'x', 'x', '56'], ['52', 'x', 'x', 'x'], ['x', '50', 'x', 'x'], ['x', 'x', 'x', '46']]
row_sums = [None, 169, None]
col_sums = [None, 165, 155, None]
diag_sum = 201

print(solve_magic_square(grid, row_sums, col_sums, diag_sum))
