
def solve_magic_square(grid):
    def is_valid(row, col, num):
        # Check the number doesn't exist in the same row, column, or square
        for i in range(4):
            if grid[row][i] == num or grid[i][col] == num:
                return False

        return True

    def solve(row, col, numbers):
        if numbers == []:
            # Check the sum of the diagonal
            if grid[0][0] + grid[1][1] + grid[2][2] + grid[3][3] != 155:
                return False
            return True

        if row == 4:
            return solve(0, col + 1, numbers)

        if grid[row][col] != 'x':
            return solve(row + 1, col, numbers)

        for num in numbers:
            if is_valid(row, col, num):
                grid[row][col] = num
                new_numbers = [n for n in numbers if n != num]
                if solve(row + 1, col, new_numbers):
                    return True

                grid[row][col] = 'x'

        return False

    solve(0, 0, [n for n in range(24, 51)])

    result = [(row, col, grid[row][col]) for row in range(4) for col in range(4) if grid[row][col] != 'x']
    return result

grid = [['x', '42', 'x', 'x'],
        ['x', '38', 'x', 'x'],
        ['x', '36', '46', 'x'],
        ['49', '25', '24', 'x']]

print(solve_magic_square(grid))
