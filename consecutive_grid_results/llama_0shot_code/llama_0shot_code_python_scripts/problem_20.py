
def solve_grid(grid):
    # Define the range of numbers
    num_range = range(48, 91)

    # Initialize the grid
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'x':
                grid[i][j] = None

    # Function to check if a number can be placed at a position
    def is_valid(num, row, col):
        # Check the number in the row
        for r in range(3):
            if grid[row][r] is not None and num < grid[row][r]:
                return False

        # Check the number in the column
        for c in range(3):
            if grid[c][col] is not None and num < grid[c][col]:
                return False

        # Check the number on the diagonal
        if row == col and grid[row][col] is not None and num < grid[row][col]:
            return False

        return True

    # Function to solve the grid
    def solve(row=0, col=0):
        if row == 3:
            return True
        if col == 3:
            return solve(row + 1, 0)

        if grid[row][col] is not None:
            return solve(row, col + 1)

        for num in num_range:
            if is_valid(num, row, col):
                grid[row][col] = num
                if solve(row, col + 1):
                    return True

        grid[row][col] = None
        return False

    # Call the function to solve the grid
    solve()

    # Create the result list
    result = []
    for i in range(3):
        for j in range(3):
            if grid[i][j] is not None:
                result.append((i, j, grid[i][j]))

    return result

# Test the function
grid = [['80', 'x', 'x'], ['56', 'x', '64'], ['51', 'x', '76']]
print(solve_grid(grid))
