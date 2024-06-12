
def solve_magic_square(grid):
    # List of all possible numbers in the grid
    numbers = list(range(37, 84))

    # Function to check if a number is valid in a cell
    def is_valid(row, col, num):
        # Check the number is not already in the current row or column
        for i in range(4):
            if num in rows[row][i] or num in cols[col][i]:
                return False
        # Check the number is not in the diagonal
        if num in diagonal[row - col]:
            return False
        return True

    # Function to solve the magic square
    def solve(row, col):
        if row == 4:
            return True
        if col == 4:
            return solve(row + 1, 0)

        if grid[row][col] != 'x':
            rows[row][col] = grid[row][col]
            cols[col][row] = grid[row][col]
            diagonal[row - col] = grid[row][col]
            sum_rows[row] -= int(grid[row][col])
            sum_cols[col] -= int(grid[row][col])
            sum_diag -= int(grid[row][col])
            return solve(row, col + 1)
        else:
            for num in numbers:
                if is_valid(row, col, num):
                    rows[row][col] = num
                    cols[col][row] = num
                    diagonal[row - col] = num
                    sum_rows[row] -= num
                    sum_cols[col] -= num
                    sum_diag -= num

                    if solve(row, col + 1):
                        return True

                    rows[row][col] = 'x'
                    cols[col][row] = 'x'
                    diagonal[row - col] = 'x'
                    sum_rows[row] += num
                    sum_cols[col] += num
                    sum_diag += num

            return False

    rows = [['x'] * 4 for _ in range(4)]
    cols = [['x'] * 4 for _ in range(4)]
    diagonal = ['x'] * 4
    sum_rows = [None, 253, 221, None]
    sum_cols = [None, 277, 204, None]
    sum_diag = 252

    if not solve(0, 0):
        return None

    result = []
    for row in range(4):
        for col in range(4):
            if grid[row][col] == 'x':
                result.append((row, col, rows[row][col]))

    return result

grid = [['42', '53', '43', '72'],
        ['x', '82', '54', 'x'],
        ['x', '62', '44', 'x'],
        ['x', 'x', 'x', 'x']]

print(solve_magic_square(grid))
