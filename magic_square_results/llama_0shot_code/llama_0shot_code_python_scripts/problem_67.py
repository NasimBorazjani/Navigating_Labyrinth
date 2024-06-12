
def solve_magic_square(grid):
    numbers = list(range(31, 68))
    solution = []

    def is_valid(row, col, num):
        # Check the number doesn't exist in the same row or column
        for i in range(4):
            if grid[row][i] == num or grid[i][col] == num:
                return False

        # Check the number doesn't exist on the diagonal
        if row == col and grid[0][0] == num or row == 3 - col and grid[0][3] == num:
            return False

        return True

    def solve(row=0, col=0):
        if row == 4:
            # Check the sums of rows, columns and diagonal
            row_sums = [sum(grid[i]) for i in range(4)]
            col_sums = [sum(grid[i][j] for i in range(4)) for j in range(4)]
            diagonal_sum = grid[0][0] + grid[1][1] + grid[2][2] + grid[3][3]
            if row_sums == [None, 187, None, 203] and col_sums == [None, 204, 206, None] and diagonal_sum == 199:
                return solution
            return None

        if col == 4:
            return solve(row + 1, 0)

        if grid[row][col] == 'x':
            for num in numbers:
                if is_valid(row, col, num):
                    grid[row][col] = num
                    solution.append((row, col, num))
                    result = solve(row, col + 1)
                    if result is not None:
                        return result
                    solution.pop()  # Backtrack
            return None

        else:
            return solve(row, col + 1)

    result = solve()
    return result

grid = [['x', '59', '52', '54'],
        ['x', 'x', 'x', '62'],
        ['x', '58', 'x', 'x'],
        ['x', 'x', '63', '42']]

print(solve_magic_square(grid))
