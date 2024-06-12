
def solve_magic_square(grid):
    def backtrack(row, col):
        if row == 4:
            return True
        if col == 4:
            return backtrack(row + 1, 0)
        if grid[row][col] != 'x':
            return backtrack(row, col + 1)

        for num in range(28, 65):
            grid[row][col] = num
            if (col == 0 and row % 2 == 0 and num % 2 != 0) or \
               (col == 1 and row % 2 != 0 and num % 2 == 0) or \
               (col == 2 and row % 2 == 0 and num % 2 == 0) or \
               (col == 3 and row % 2 != 0 and num % 2 != 0):
                continue
            if (row == 0 and col == 1 and num != 28) or \
               (row == 0 and col == 2 and num != 47) or \
               (row == 1 and col == 1 and num != 28) or \
               (row == 1 and col == 3 and num != 40) or \
               (row == 2 and col == 1 and num != 33) or \
               (row == 3 and col == 0 and num != 50):
                continue
            if check_constraints(grid):
                if backtrack(row, col + 1):
                    return True
        grid[row][col] = 'x'
        return False

    def check_constraints(grid):
        rows_sum = [0, 0, 0, 0]
        cols_sum = [0, 0, 0, 0]
        for row in range(4):
            for col in range(4):
                if grid[row][col] != 'x':
                    rows_sum[row] += int(grid[row][col])
                    cols_sum[col] += int(grid[row][col])
        if rows_sum[0] != 152 or rows_sum[1] != 158 or rows_sum[2] != 156 or rows_sum[3] != 185 or \
           cols_sum[0] != 152 or cols_sum[1] != 158 or cols_sum[2] != 156 or cols_sum[3] != 185 or \
           int(grid[0][2]) + int(grid[1][1]) + int(grid[2][0]) + int(grid[3][1]) != 165:
            return False
        return True

    backtrack(0, 0)
    result = [(i, j, int(grid[i][j])) for i in range(4) for j in range(4) if grid[i][j] != 'x']
    return result

grid = [['36', '47', 'x', 'x'], ['x', '28', '40', 'x'], ['x', '33', 'x', 'x'], ['50', 'x', 'x', 'x']]
print(solve_magic_square(grid))
