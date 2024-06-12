
def solve_magic_square(grid):
    def is_valid(row, col, num):
        # Check the number doesn't exist in the same row, column, or square
        for i in range(4):
            if grid[row][i] == num or grid[i][col] == num:
                return False

        return True

    def solve(row, col, num_left):
        if num_left == 0:
            return True

        if row == 4:
            return solve(0, col + 1, num_left - 1)

        if col == 4:
            return solve(row + 1, 0, num_left - 1)

        if grid[row][col] != 'x':
            return solve(row, col + 1, num_left - 1)

        for num in range(33, 85):
            if is_valid(row, col, num):
                grid[row][col] = num
                if solve(row, col + 1, num_left - 1):
                    return True

        grid[row][col] = 'x'
        return False

    solve(0, 0, 16)

    result = []
    for i in range(4):
        for j in range(4):
            if grid[i][j] != 'x':
                result.append((i, j, int(grid[i][j])))

    return result


grid = [['68', 'x', 'x', '76'],
        ['74', 'x', 'x', 'x'],
        ['x', 'x', '82', 'x'],
        ['66', 'x', '35', 'x']]

print(solve_magic_square(grid))
