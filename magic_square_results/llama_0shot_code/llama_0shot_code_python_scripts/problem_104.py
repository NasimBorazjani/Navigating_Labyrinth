
def solve_magic_square(grid):
    def is_valid(row, col, num):
        # Check the number doesn't already exist in the row, column or square
        for i in range(4):
            if num in rows[row][i] or num in cols[col][i] or num in squares[row//2][col//2][i]:
                return False
        return True

    def solve(row=0, col=0):
        if row == 4:  # If finished, check if solution is correct
            return grid_sum() == total_sum
        if col == 4:  # Move to next row
            return solve(row + 1, 0)
        if grid[row][col] != 'x':  # If cell is not empty, move to next cell
            return solve(row, col + 1)

        for num in range(min_val, max_val + 1):  # Try all possible numbers
            if is_valid(row, col, num):
                grid[row][col] = num
                rows[row][num//10 - 2] = num
                cols[col][num%10 - 2] = num
                squares[row//2][col//2][(num//10 - 2)//2 + (num%10 - 2)//2] = num
                if solve(row, col + 1):  # If solution found, return True
                    return True
        grid[row][col] = 'x'  # Reset cell
        rows[row][num//10 - 2] = 'x'
        cols[col][num%10 - 2] = 'x'
        squares[row//2][col//2][(num//10 - 2)//2 + (num%10 - 2)//2] = 'x'
        return False  # No solution found

    def grid_sum():
        return sum(sum(cell for cell in row if cell != 'x') for row in grid)

    rows = [['x', 'x', 'x', 'x'] for _ in range(4)]
    cols = [['x', 'x', 'x', 'x'] for _ in range(4)]
    squares = [[['x', 'x', 'x', 'x'] for _ in range(2)] for _ in range(2)]
    min_val = 36
    max_val = 92
    total_sum = 214 + 240 + 300 + 191 + 249
    solve()
    return [(i, j, grid[i][j]) for i in range(4) for j in range(4) if grid[i][j] != 'x']

grid = [['x', '69', 'x', 'x'], ['x', '62', 'x', 'x'], ['x', '82', '40', 'x'], ['x', '87', '78', '80']]
print(solve_magic_square(grid))
