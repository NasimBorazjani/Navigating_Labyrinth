
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

    def backtrack(row, col, best):
        if row == 4:
            row, col = 0, col + 1
            if col == 4:
                return best
        if grid[row][col] == 'x':
            for num in range(31, 68):
                if is_valid(row, col, num):
                    grid[row][col] = num
                    new_best = backtrack(row + (col == 3), col, min(best, sum(map(sum, grid))))
                    if new_best < best:
                        best = new_best
                    grid[row][col] = 'x'
        else:
            backtrack(row + (col == 3), col, best)
        return best

    return backtrack(0, 0, float('inf'))

grid = [['x', '40', 'x', 'x'],
        ['x', '58', 'x', '37'],
        ['47', 'x', 'x', '44'],
        ['45', 'x', 'x', '42']]

row_sums = [None, 220, None, None]
col_sums = [None, 224, 226, None]
diag_sum = 211

print(solve_magic_square(grid, row_sums, col_sums, diag_sum))
