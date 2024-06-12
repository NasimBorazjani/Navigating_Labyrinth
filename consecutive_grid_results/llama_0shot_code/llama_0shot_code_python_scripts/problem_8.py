
# Function to check if the grid is valid
def is_valid(grid, row, col, num):
    # Check the number in the row
    for i in range(3):
        if grid[row][i] != 'x' and grid[row][i] > num:
            return False

    # Check the number in the column
    for i in range(3):
        if grid[i][col] != 'x' and grid[i][col] > num:
            return False

    # Check the number in the diagonal
    if row == col and grid[0][0] != 'x' and grid[0][0] > num:
        return False

    return True

# Function to solve the problem
def solve_grid():
    grid = [['x', 'x', 'x'], ['x', '36', '44'], ['x', '34', 'x']]
    remaining_nums = list(range(19, 52))

    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'x':
                for num in remaining_nums:
                    if is_valid(grid, i, j, num):
                        grid[i][j] = num
                        remaining_nums.remove(num)
                        break

    # Calculate the sum of the numbers in the top row, rightmost column and diagonal
    top_row_sum = sum(grid[0])
    rightmost_col_sum = sum(grid[i][2] for i in range(3))
    diagonal_sum = grid[0][0] + grid[1][1] + grid[2][2]

    # Return the replacement tuples
    return [(0, 0, grid[0][0]), (0, 1, grid[0][1]), (0, 2, grid[0][2]),
            (1, 2, grid[1][2]), (2, 1, grid[2][1]), (2, 2, grid[2][2])]

print(solve_grid())
