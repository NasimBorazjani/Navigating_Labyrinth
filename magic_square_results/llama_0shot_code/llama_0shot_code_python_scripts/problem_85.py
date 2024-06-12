
def solve_magic_square(grid):
    rows = [None, 221, 257, None]
    cols = [None, 252, 238, None]
    diag = 221
    total = sum(rows) + sum(cols)
    size = len(grid)
    solutions = []

    def is_valid(row, col, val):
        grid[row][col] = val
        row_sum = sum(grid[row])
        col_sum = sum(grid[i][col] for i in range(size))
        diag_sum = sum(grid[i][i] for i in range(size))
        anti_diag_sum = sum(grid[i][size - i - 1] for i in range(size))
        return (rows[row] is None or row_sum == rows[row]) and \
               (cols[col] is None or col_sum == cols[col]) and \
               (row == col or row + col != size - 1 or diag_sum == diag) and \
               (row == size - col - 1 or row + col != size - 1 or anti_diag_sum == diag)

    def backtrack(row=0, col=0):
        if row == size:
            solutions.append(grid[:])
            return
        if col == size:
            backtrack(row + 1, 0)
            return
        if grid[row][col] != 'x':
            backtrack(row, col + 1)
        else:
            min_val = 1 if row == col or row + col == size - 1 else 2
            max_val = total - sum(grid[i][col] for i in range(size))
            if row == col:
                max_val = min(max_val, 2 * rows[row] - (size - 1) * min_val)
            for val in range(min_val, max_val + 1):
                if is_valid(row, col, val):
                    grid[row][col] = val
                    backtrack(row, col + 1)
                    grid[row][col] = 'x'

    backtrack()
    return solutions

grid = [['x', 'x', '80', '72'],
        ['44', 'x', '39', 'x'],
        ['x', '70', '64', 'x'],
        ['x', '67', 'x', '42']]

solutions = solve_magic_square(grid)
solution = min(solutions, key=sum)
result = [(i, j, val) for i, row in enumerate(solution) for j, val in enumerate(row) if val != 'x']
print(result)
