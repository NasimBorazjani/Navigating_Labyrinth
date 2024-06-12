
def solve_magic_square(grid):
    rows = [None, 211, 161, None]
    cols = [None, 143, 170, None]
    diag = 146
    cells = [(r, c, min_sum, max_sum)
             for r, row in enumerate(rows)
             for c, col in enumerate(cols)
             for min_sum, max_sum in [(22, 68) if row is None and col is None else (row, row)]]
    cells.sort(key=lambda cell: cell[2])
    solutions = []

    def fill(cell_index, current_sum, current_grid):
        if cell_index == len(cells):
            if current_sum == diag and all(sum(row) == col for row, col in zip(current_grid, cols)) and all(sum(col) == row for col, row in zip(current_grid, rows)):
                solutions.append(current_grid[:2])
            return
        r, c, min_sum, max_sum = cells[cell_index]
        for value in range(min_sum, max_sum + 1):
            if current_sum + value > diag:
                break
            current_grid[r][c] = value
            fill(cell_index + 1, current_sum + value, current_grid)

    fill(0, 0, [[None] * 4 for _ in range(4)])
    return solutions

print(solve_magic_square([['x', 'x', 32, 'x'], [37, 61, 'x', 54], ['x', 'x', 'x', 62], ['x', 30, 'x', 44]]))
