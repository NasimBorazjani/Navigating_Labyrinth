
def magic_square(grid):
    rows = [None, 156, 208, None]
    cols = [None, 217, 193, None]
    diag = 166
    total = sum(rows) + sum(cols) + diag
    def solve(grid, row, col, total):
        if total < 0:
            return False
        if row == len(grid):
            return True
        if col == len(grid[0]):
            return solve(grid, row + 1, 0, total - grid[row][col])
        if grid[row][col] == 'x':
            for i in range(31, 68):
                grid[row][col] = i
                if check(grid, row, col, rows, cols, diag):
                    if solve(grid, row, col + 1, total - i):
                        return True
            grid[row][col] = 'x'
        else:
            if solve(grid, row, col + 1, total - grid[row][col]):
                return True
        return False
    def check(grid, row, col, rows, cols, diag):
        for i in range(len(grid)):
            if sum(grid[i]) != rows[i]:
                return False
        for i in range(len(grid)):
            if sum(grid[i][j] for i in range(len(grid))) != cols[i]:
                return False
        if sum(grid[i][i] for i in range(len(grid))) != diag:
            return False
        return True
    if not solve(grid, 0, 0, total):
        return None
    return [(i, j, grid[i][j]) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] != 'x']

grid = [['x', 'x', '64', 'x'], ['34', '54', 'x', 'x'], ['x', '56', '53', 'x'], ['36', 'x', 'x', '49']]
print(magic_square(grid))
