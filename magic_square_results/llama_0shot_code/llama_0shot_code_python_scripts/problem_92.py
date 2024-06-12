
def solve_magic_square():
    # Initialize the grid
    grid = [[0]*4 for _ in range(4)]
    # Fill in the cells where the sum of the rows or columns is given
    grid[0][1] = 41
    grid[0][2] = 67
    grid[1][1] = 73
    grid[1][3] = 91
    grid[2][1] = 43
    grid[2][3] = 76
    grid[3][0] = 80
    grid[3][2] = 86
    # Define the sums of rows and columns
    row_sums = [None, 298, 222, None]
    col_sums = [None, 240, 266, None]
    # Define the sum of the diagonal
    diagonal_sum = 299
    # Start backtracking from the first cell
    if backtrack(grid, 0, 0, row_sums, col_sums, diagonal_sum):
        return grid
    else:
        return "No solution found"

def backtrack(grid, row, col, row_sums, col_sums, diagonal_sum):
    if row == 4:
        # Check the sum of the diagonal
        if sum(grid[i][i] for i in range(4)) != diagonal_sum:
            return False
        # If the grid is filled correctly, return True
        return True
    if col == 4:
        return backtrack(grid, row+1, 0, row_sums, col_sums, diagonal_sum)
    if grid[row][col] != 0:
        return backtrack(grid, row, col+1, row_sums, col_sums, diagonal_sum)
    for num in range(41, 93):
        # Check if the number can be placed in the current cell
        if (row_sums[row] is not None and grid[row].count(0) == 1 and
            grid[row].count(num) == 0 and
            row_sums[row] - grid[row][col] + num == 0):
            # Try placing the number in the current cell
            grid[row][col] = num
            # Move on to the next cell
            if backtrack(grid, row, col+1, row_sums, col_sums, diagonal_sum):
                return True
            # If no solution is found, undo the fill
            grid[row][col] = 0
        if (col_sums[col] is not None and grid[:, col].count(0) == 1 and
            [grid[i][col] for i in range(4)].count(num) == 0 and
            col_sums[col] - grid[row][col] + num == 0):
            grid[row][col] = num
            if backtrack(grid, row, col+1, row_sums, col_sums, diagonal_sum):
                return True
            grid[row][col] = 0
    return False

# Call the function to solve the magic square
print(solve_magic_square())
