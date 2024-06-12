
def solve_magic_square(grid):
    def is_valid(row, col, num):
        # Check the number doesn't exist in the same row, column, or square
        for i in range(4):
            if grid[row][i] == num or grid[i][col] == num:
                return False

        return True

    def solve(row, col, numbers):
        if numbers == []:
            # Check the sum of rows and columns
            for i in range(4):
                if sum(grid[i]) != [None, 227, 215, None][i]:
                    return False
                if sum(grid[j][i] for j in range(4)) != [None, 207, 218, None][i]:
                    return False

            # Check the sum of the diagonal
            if sum(grid[i][i] for i in range(4)) != 195:
                return False

            return True

        if row == 4:
            return solve(0, col + 1, numbers)
        if col == 4:
            return solve(row + 1, 0, numbers)

        if grid[row][col] != 'x':
            return solve(row, col + 1, numbers)

        for num in numbers:
            if is_valid(row, col, num):
                grid[row][col] = num
                if solve(row, col + 1, numbers - {num}):
                    return True
                grid[row][col] = 'x'

        return False

    solve(0, 0, set(range(41, 67)))

    result = [(i, j, grid[i][j]) for i in range(4) for j in range(4) if grid[i][j] != 'x']
    return result

grid = [['x', '56', 'x', '40'], ['x', 'x', '44', '60'], ['x', '52', 'x', '45'], ['x', 'x', '62', '47']]
print(solve_magic_square(grid))
