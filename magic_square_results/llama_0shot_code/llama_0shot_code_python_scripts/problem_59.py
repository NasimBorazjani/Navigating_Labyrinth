
# Function to check if a number is valid in a cell
def is_valid(grid, row, col, num):
    # Check the number in the row
    for i in range(4):
        if grid[row][i] == num:
            return False

    # Check the number in the column
    for i in range(4):
        if grid[i][col] == num:
            return False

    # Check the number in the main diagonal
    if row == col:
        for i in range(4):
            if grid[i][i] == num:
                return False

    # Check the number in the counter diagonal
    if row + col == 3:
        for i in range(4):
            if grid[i][3 - i] == num:
                return False

    return True

# Function to solve the magic square
def solve_magic_square(grid):
    rows = [0, 138, None, None]
    cols = [None, 148, 157, None]
    diags = [None, None, 133, None]
    total = 0
    for row in range(4):
        for col in range(4):
            if grid[row][col] == 'x':
                for num in range(22, 54):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        total += num
                        break
                else:
                    return None
    return [(row, col, num) for row in range(4) for col in range(4) if grid[row][col] != 'x' for num in [grid[row][col]]]

# Test the function
grid = [['35', 'x', '51', 'x'], ['x', 'x', 'x', '23'], ['x', '32', '31', '52'], ['x', 'x', 'x', 'x']]
print(solve_magic_square(grid))
