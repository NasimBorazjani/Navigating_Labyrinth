
def magic_square(grid, numbers):
    def is_valid(row, col, num):
        # Check the number in the row
        for i in range(4):
            if grid[row][i] == num:
                return False
        # Check the number in the column
        for i in range(4):
            if grid[i][col] == num:
                return False
        # Check the number in the same diagonal
        for i in range(4):
            if grid[i][i] == num:
                return False
        return True

    def solve(row=0, col=0):
        if row == 4:
            row, col = 0, 0
            while col < 4:
                if grid[row][col] == 'x':
                    col += 1
                    continue
                col += 1
            row += 1
        if row == 4:
            # Check the sums of rows, columns and diagonal
            row_sums = [sum(grid[i]) for i in range(4)]
            col_sums = [sum(grid[i][j] for i in range(4)) for j in range(4)]
            diagonal_sum = grid[0][0] + grid[1][1] + grid[2][2] + grid[3][3]
            if row_sums[1] == 187 and row_sums[2] == 186 and col_sums[1] == 187 and col_sums[2] == 186 and diagonal_sum == 160:
                return grid
            else:
                return False
        if grid[row][col] != 'x':
            return solve(row + (col + 1) // 4, (col + 1) % 4)
        for num in numbers:
            if is_valid(row, col, num):
                grid[row][col] = num
                result = solve(row + (col + 1) // 4, (col + 1) % 4)
                if result:
                    return result
        grid[row][col] = 'x'
        return False

    numbers.sort()
    result = solve()
    if result is False:
        return "No solution found"
    else:
        return [(i, j, val) for i in range(4) for j in range(4) if grid[i][j] != 'x' for val in numbers if grid[i][j] == val]

grid = [['x', 'x', 'x', 'x'], ['24', 'x', '27', '41'], ['22', '37', 'x', 'x'], ['29', 'x', 'x', '46']]
numbers = list(range(22, 69))
print(magic_square(grid, numbers))
