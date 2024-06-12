
def solve_magic_square(grid):
    def backtrack(row=0, col=0):
        if row == len(grid):  # all cells are filled
            return True
        if col == len(grid[row]):  # move to next row
            return backtrack(row + 1, 0)
        if grid[row][col] != 'x':  # this cell is already filled
            return backtrack(row, col + 1)

        for num in range(35, 62):  # try possible numbers
            if num not in used_nums and is_valid(row, col, num):
                grid[row][col] = num
                used_nums.add(num)
                if backtrack(row, col + 1):  # try next cell
                    return True
                grid[row][col] = 'x'  # undo and try different number
                used_nums.remove(num)
        return False  # trigger backtracking

    def is_valid(row, col, num):
        # check row
        if row_sums[row] is not None and row_sums[row] - num != row_sum:
            return False
        # check column
        if col_sums[col] is not None and col_sums[col] - num != col_sum:
            return False
        # check diagonal
        if row == col and diag_sum - num != diag_sum_actual:
            return False
        return True

    row_sums = [None, 177, 160, None]
    col_sums = [None, 188, 188, None]
    diag_sum = 173
    diag_sum_actual = sum(grid[i][i] for i in range(len(grid)))
    row_sum = sum(grid[0][i] for i in range(len(grid)) if grid[0][i] != 'x')
    col_sum = sum(grid[i][0] for i in range(len(grid)) if grid[i][0] != 'x')
    used_nums = set(num for row in grid for num in row if num != 'x')

    if not backtrack():
        return None  # no solution found

    return [(row, col, num) for row in range(len(grid)) for col in range(len(grid[row])) for num in [grid[row][col]] if num != 'x']

grid = [['x', 'x', '39', 'x'], ['x', 'x', 'x', '43'], ['x', 'x', 'x', '47'], ['46', '49', 'x', '53']]
print(solve_magic_square(grid))
