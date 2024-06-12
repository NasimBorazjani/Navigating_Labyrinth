
def solve_magic_square(grid):
    def is_valid(row, col, num):
        # Check the number doesn't exist in the same row or column
        for i in range(4):
            if grid[row][i] == num or grid[i][col] == num:
                return False

        # Check the number doesn't exist in the same 3x3 box
        start_row, start_col = row - row % 3, col - col % 3
        for i in range(3):
            for j in range(3):
                if grid[i + start_row][j + start_col] == num:
                    return False

        return True

    def solve(row=0, col=0):
        if row == 4:
            return True
        if col == 4:
            return solve(row + 1, 0)

        if grid[row][col] != 'x':
            return solve(row, col + 1)

        for num in range(28, 65):
            if is_valid(row, col, num):
                grid[row][col] = num
                if solve(row, col + 1):
                    return True
                grid[row][col] = 'x'

        return False

    if not solve():
        return None

    result = []
    for i in range(4):
        for j in range(4):
            if grid[i][j] != 'x':
                result.append((i, j, grid[i][j]))

    return result

grid = [['x', 'x', '60', '63'],
        ['35', 'x', 'x', 'x'],
        ['x', 'x', 'x', '50'],
        ['34', 'x', '37', 'x']]

print(solve_magic_square(grid))
