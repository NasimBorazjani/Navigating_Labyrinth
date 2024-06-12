
def solve_magic_square(grid):
    def backtrack(cells, row_sums, col_sums, diag_sum, total, index):
        if total > sum(sum(int(cell) for cell in row) for row in grid):
            return None
        if index == len(cells):
            if row_sums == [None, 185, 162, None] and col_sums == [None, 134, 166, None] and diag_sum == 173:
                return [(row, col, val) for (row, col, val) in cells]
            return None
        row, col, vals = cells[index]
        for val in vals:
            new_cells = cells[:index] + [(row, col, [val])] + cells[index + 1:]
            new_row_sums = row_sums[:row] + [row_sums[row] + val] + row_sums[row + 1:]
            new_col_sums = col_sums[:col] + [col_sums[col] + val] + col_sums[col + 1:]
            new_diag_sum = diag_sum + val if row == col else diag_sum - val
            solution = backtrack(new_cells, new_row_sums, new_col_sums, new_diag_sum, total + val, index + 1)
            if solution:
                return solution
        return None

    cells = [(row, col, [val for val in range(28, 60) if val not in grid[row]])
             for row in range(4)
             for col in range(4)
             if grid[row][col] == 'x']
    cells.sort(key=lambda cell: len(cell[2]))
    row_sums = [sum(int(cell) for cell in row) for row in grid]
    col_sums = [sum(int(grid[row][col]) for row in range(4)) for col in range(4)]
    diag_sum = sum(grid[i][i] for i in range(4)) - sum(grid[i][3 - i] for i in range(4))
    return backtrack(cells, row_sums, col_sums, diag_sum, 0, 0)

grid = [['50', 'x', 'x', '42'],
        ['x', 'x', '44', 'x'],
        ['47', 'x', '49', 'x'],
        ['53', 'x', 'x', '30']]

print(solve_magic_square(grid))
