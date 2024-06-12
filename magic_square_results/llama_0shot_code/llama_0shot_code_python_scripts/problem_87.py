
def solve_magic_square(grid):
    def backtrack(row, col, num):
        if num == 0:
            return True
        if row == 4:
            row = 0
            col += 1
        if col == 4:
            return False
        if grid[row][col] != 'x':
            return backtrack(row + 1, col, num - grid[row][col])
        for n in range(max_num, 37, -1):
            if n not in used and n - grid[row][col] not in row_sums[row] and n - grid[row][col] not in col_sums[col] and (row != col or n - grid[row][col] not in diagonal_sum):
                used.add(n)
                grid[row][col] = n
                row_sums[row].add(n - grid[row][col])
                col_sums[col].add(n - grid[row][col])
                if row == col:
                    diagonal_sum.add(n - grid[row][col])
                if backtrack(row + 1, col, num - grid[row][col]):
                    return True
                used.remove(n)
                row_sums[row].remove(n - grid[row][col])
                col_sums[col].remove(n - grid[row][col])
                if row == col:
                    diagonal_sum.remove(n - grid[row][col])
                grid[row][col] = 'x'
        return False

    max_num = 83
    grid = [['72', '76', '68', '69'],
            ['56', 'x', 'x', 'x'],
            ['49', 'x', 'x', '43'],
            ['x', 'x', '61', 'x']]
    row_sums = [{max_num}, {max_num}, {max_num}, {max_num}]
    col_sums = [{max_num}, {max_num}, {max_num}, {max_num}]
    diagonal_sum = {max_num}
    used = set()
    for r in range(4):
        for c in range(4):
            if grid[r][c] != 'x':
                used.add(int(grid[r][c]))
                row_sums[r].add(int(grid[r][c]))
                col_sums[c].add(int(grid[r][c]))
                if r == c:
                    diagonal_sum.add(int(grid[r][c]))
    backtrack(0, 0, sum(row_sums[0]) + sum(col_sums[0]) + sum(diagonal_sum))
    return [(r, c, int(grid[r][c])) for r in range(4) for c in range(4) if grid[r][c] != 'x']

print(solve_magic_square(None))
