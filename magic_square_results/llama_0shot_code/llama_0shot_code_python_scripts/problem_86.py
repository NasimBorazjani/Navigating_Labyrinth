
def solve_magic_square(grid):
    def is_valid(row, col, num):
        # Check the number doesn't exist in the same row or column
        for r in range(4):
            if grid[r][col] == num:
                return False
        for c in range(4):
            if grid[row][c] == num:
                return False

        # Check the number doesn't exist in the same 3x3 box
        start_row, start_col = row - row % 3, col - col % 3
        for r in range(3):
            for c in range(3):
                if grid[r + start_row][c + start_col] == num:
                    return False

        return True

    def solve(grid, row=0, col=0):
        if row == 4:
            row, col = 0, col + 1
            if col == 4:
                return grid

        if col == 4:
            col = 0
            row += 1

        if grid[row][col] != 'x':
            return solve(grid, row, col + 1)

        for num in range(37, 84):
            if is_valid(row, col, num):
                grid[row][col] = num
                solution = solve(grid, row, col + 1)
                if solution:
                    return solution
                grid[row][col] = 'x'

        return None

    def calculate_sums(grid):
        rows = [[0]*4 for _ in range(4)]
        cols = [[0]*4 for _ in range(4)]
        for r in range(4):
            for c in range(4):
                if grid[r][c] != 'x':
                    rows[r][c] = grid[r][c]
                    cols[c][r] = grid[r][c]

        return rows, cols

    rows_sums, cols_sums = calculate_sums(grid)
    for r in range(4):
        for c in range(4):
            if grid[r][c] == 'x':
                grid[r][c] = 'x'

    solution = solve(grid)
    result = []
    for r in range(4):
        for c in range(4):
            if solution[r][c] != 'x':
                result.append((r, c, solution[r][c]))

    return result

grid = [['x', '48', '64', '67'],
        ['x', '50', '61', 'x'],
        ['42', 'x', 'x', '74'],
        ['x', 'x', '72', 'x']]

print(solve_magic_square(grid))
