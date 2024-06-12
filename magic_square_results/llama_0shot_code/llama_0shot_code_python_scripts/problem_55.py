
def solve_magic_square(grid):
    def is_valid(row, col, num):
        # Check the number doesn't exist in the same row, column, or square
        for i in range(4):
            if grid[row][i] == str(num) or grid[i][col] == str(num):
                return False
        return True

    def solve(row, col, num_left):
        if num_left == 0:
            return True
        if row == 4:
            return False
        if grid[row][col] != 'x':
            return solve(row + (col + 1) // 4, (col + 1) % 4, num_left - 1)
        for num in range(28, 60):
            if is_valid(row, col, num):
                grid[row][col] = str(num)
                if solve(row + (col + 1) // 4, (col + 1) % 4, num_left - 1):
                    return True
                grid[row][col] = 'x'
        return False

    solve(0, 0, 10)

    result = []
    for i in range(4):
        for j in range(4):
            if grid[i][j] != 'x':
                result.append((i, j, int(grid[i][j])))
    return result


grid = [['46', 'x', '58', '45'], ['x', 'x', '54', 'x'], ['x', 'x', 'x', 'x'], ['28', '53', '34', 'x']]
print(solve_magic_square(grid))
