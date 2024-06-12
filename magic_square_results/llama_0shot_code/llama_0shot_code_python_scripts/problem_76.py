
def solve_magic_square():
    # Initialize the grid
    grid = [['x' for _ in range(4)] for _ in range(4)]

    # Fill in the numbers that must be in the grid because of the given row and column sums
    grid[0][0] = '26'
    grid[0][1] = '38'
    grid[0][2] = '27'
    grid[1][3] = '19'
    grid[2][1] = '43'
    grid[3][0] = '42'
    grid[3][2] = '34'
    grid[3][3] = '20'

    # Function to check if a number is valid in a position
    def is_valid(number, row, col):
        # Check the number's row
        for i in range(4):
            if grid[row][i] == number:
                return False

        # Check the number's column
        for i in range(4):
            if grid[i][col] == number:
                return False

        # Check the number's diagonal
        if row == col:
            for i in range(4):
                if grid[i][i] == number:
                    return False

        return True

    # Function to solve the magic square
    def solve(row, col):
        if row == 4:
            return True

        if col == 4:
            return solve(row + 1, 0)

        if grid[row][col] != 'x':
            return solve(row, col + 1)

        for number in range(6, 48):
            if is_valid(str(number), row, col):
                grid[row][col] = str(number)

                if solve(row, col + 1):
                    return True

                grid[row][col] = 'x'

        return False

    # Solve the magic square
    solve(0, 0)

    # Extract the solution as a list of tuples
    solution = [(row, col, int(grid[row][col])) for row in range(4) for col in range(4) if grid[row][col] != 'x']

    return solution

print(solve_magic_square())
