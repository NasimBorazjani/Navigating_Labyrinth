
def solve_magic_square(grid, row_sums, col_sums, diag_sum):
    def is_valid(i, j, num):
        # Check the number doesn't exist in the same row, column or diagonals
        for x in range(3):
            for y in range(3):
                if grid[x][y] == num:
                    return False
        return True

    def backtrack(row=0, col=0, sum_=0):
        if row == 3:  # If all rows are filled
            return True  # We found a solution
        if col == 3:  # If we finished a row
            col = 0
            row += 1
        if grid[row][col] != 'x':  # If the cell is already filled
            return backtrack(row, col + 1, sum_)
        for num in range(48, 78):  # Try a number
            if is_valid(row, col, num):  # If the number is valid
                grid[row][col] = num  # Put the number in the cell
                new_sum = sum_ + num
                if backtrack(row, col + 1, new_sum):  # If this leads to a solution
                    return True
        grid[row][col] = 'x'  # Undo the move
        return False

    backtrack()
    result = [(i, j, grid[i][j]) for i in range(3) for j in range(3) if grid[i][j] != 'x']
    return result

grid = [['x', 'x', 'x'], ['x', 'x', '55'], ['x', 'x', 'x']]
row_sums = [167, 190, 172]
col_sums = [190, 167, 172]
diag_sum = 349

print(solve_magic_square(grid, row_sums, col_sums, diag_sum))
