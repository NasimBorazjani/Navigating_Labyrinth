
def solve_magic_square(grid):
    # Define the grid and the list of numbers
    grid = [['x' if cell == 'x' else int(cell) for cell in row] for row in grid]
    numbers = list(range(30, 67))

    # Define the row and column constraints
    row_constraints = [None, 192, 173, None]
    col_constraints = [None, 191, 190, None]
    diagonal_constraint = 180

    # Function to check if a number can be placed in a cell
    def can_place(row, col, num):
        # Check the row
        if row_constraints[row] is not None and grid[row].count(None) == 0 and sum(grid[row]) + num > row_constraints[row]:
            return False

        # Check the column
        if col_constraints[col] is not None and [grid[i][col] for i in range(4)].count(None) == 0 and sum(grid[i][col] for i in range(4)) + num > col_constraints[col]:
            return False

        # Check the diagonal
        if row + col == 3 and grid[0][0] is not None and grid[0][0] + num > diagonal_constraint:
            return False

        return True

    # Function to solve the magic square
    def solve(row, col, nums):
        if len(nums) == 0:
            return True

        for i in range(row, 4):
            for j in range(col, 4):
                if grid[i][j] is None:
                    for num in nums:
                        if can_place(i, j, num):
                            grid[i][j] = num
                            nums.remove(num)

                            if solve(i, j, nums):
                                return True

                            grid[i][j] = None
                            nums.append(num)

                    return False

        return False

    # Solve the magic square
    solve(0, 0, numbers)

    # Return the numbers placed in the 'x' cells
    return [(i, j, grid[i][j]) for i in range(4) for j in range(4) if grid[i][j] is not None]

# Test the function
grid = [['x', '65', '49', '35'],
        ['40', 'x', '52', 'x'],
        ['x', 'x', '34', 'x'],
        ['x', 'x', '55', '61']]

print(solve_magic_square(grid))
